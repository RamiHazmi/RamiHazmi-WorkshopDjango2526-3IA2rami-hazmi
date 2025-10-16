from django.contrib import admin
from .models import Session
from django.utils import timezone
from datetime import datetime, timedelta
# Register your models here.
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("title", "topic", "session_day", "start_time", "end_time", "room", "conference", "duration")
    list_editable = ("room",)
    ordering = ("session_day", "start_time")
    list_filter = ("conference", "session_day")
    search_fields = ("title", "topic", "room")
    date_hierarchy = "session_day"
    readonly_fields = ("session_id",)
    list_per_page = 10

    fieldsets = (
        ("Informations générales", {
            "fields": ("title", "topic", "conference","room")
        }),
        ("Informations de l'horaire", {
            "fields": ("session_day", "start_time", "end_time")
        }),
    )

    def duration(self, objet):
        """Retourne la durée de la session en heures et minutes"""
        if objet.start_time and objet.end_time:
            start = datetime.combine(objet.session_day, objet.start_time)
            end = datetime.combine(objet.session_day, objet.end_time)
            delta = end - start
            hours, remainder = divmod(delta.seconds, 3600)
            minutes = remainder // 60
            return f"{hours}h {minutes}min"
        return "N/A"
    
    duration.short_description = "Durée"