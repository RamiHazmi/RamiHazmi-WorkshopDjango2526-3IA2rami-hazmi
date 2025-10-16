from django.contrib import admin
from .models import Conference, Submission

# Customize admin site titles
admin.site.site_title = "Gestion Conference 25/26"
admin.site.site_header = "Gestion Conference"
admin.site.index_title = "Django App Conference"

# Register Submission model
admin.site.register(Submission)

# Inline for Submissions inside Conference admin
class SubmissionInline(admin.TabularInline):
    model = Submission
    extra = 1
    readonly_fields = ("Submission_date",)

# Conference admin with inline
@admin.register(Conference)
class AdminConferenceModel(admin.ModelAdmin):
    list_display = ("name", "theme", "start_date", "end_date", "duration")
    ordering = ("start_date",)
    search_fields = ("name", "theme")
    list_filter = ("theme",)
    date_hierarchy = "start_date"

    fieldsets = (
        ("Information générale", {
            "fields": ("conference_id", "name", "theme", "description")
        }),
        ("Informations logistiques", {
            "fields": ("location", "start_date", "end_date")
        }),
    )

    readonly_fields = ("conference_id",)

    inlines = [SubmissionInline]

    # Custom column for duration
    def duration(self, obj):
        if obj.start_date and obj.end_date:
            return (obj.end_date - obj.start_date).days
        return "RAS"
    duration.short_description = "Durée (jours)"



#personalisation attributs sans actions