from django.contrib import admin
from .models import Conference, Submission
admin.site.site_title="Gestion Conference 25/26"
admin.site.site_header="Gestion Conference"
admin.site.index_title="django app Conference"


# Register your models here.
admin.site.register(Conference)

admin.site.register(Submission)
