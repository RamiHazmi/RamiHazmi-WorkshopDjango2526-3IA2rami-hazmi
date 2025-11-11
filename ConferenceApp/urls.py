from django.urls import path
from . import views
from .views import *
urlpatterns =[
 #path("liste/", views.list_conferences, name="liste_conferences"),
    path("liste/",ConferenceList.as_view(),name="liste_conferences"),
    path("<int:pk>/",ConferenceDetails.as_view(),name="conference_details"),
    path("add/",ConferenceCreate.as_view(),name="conference_add"),
    path("edit/<int:pk>/",ConferenceUpdate.as_view(),name="conference_update"),
     path("delete/<int:pk>/",ConferenceDelete.as_view(),name="conference_delete"),

     
path("submissions/liste/", SubmissionList.as_view(), name="submission_list"),
path("submissions/add/", SubmissionCreate.as_view(), name="submission_add"),
path("submissions/<str:pk>/update/", SubmissionUpdate.as_view(), name="submission_update"),
path("submissions/<str:pk>/", SubmissionDetails.as_view(), name="submission_details"),

]