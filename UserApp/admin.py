from django.contrib import admin
from .models import User, OrganizingCommittee

# Register your models here.

admin.site.register(OrganizingCommittee)

class CommiteeInlineAdmin(admin.StackedInline):
    model = OrganizingCommittee
    extra = 1
    readonly_fields = ("committee_role", "join_date")  # ✅ corrected spelling

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "first_name", "last_name", "email", "role")
    list_editable = ("role",)
    ordering = ("first_name", "last_name")
    list_filter = ("role",)
    search_fields = ("first_name", "last_name", "email")
    readonly_fields = ("user_id",)
    list_per_page = 10

    inlines = [CommiteeInlineAdmin]
