from .views import (
    SeekerCreateView,
    JobCreateView,
    SeekerDetailView,
    SeekerListView,
    JobDetailView,
    JobListView,
)
from django.urls import path


urlpatterns = [
    path(
        "companies/<company_profile_slug>/jobs/",
        JobListView.as_view(),
        name="company-jobs",
    ),
    path("jobs/", JobListView.as_view(), name="jobs"),
    path(
        "companies/<company_profile_slug>/create-job/",
        JobCreateView.as_view(),
        name="create-company",
    ),
    path("jobs/<slug>/", JobDetailView.as_view(), name="company"),
    path("jobs/<job_slug>/seekers/", SeekerListView.as_view(), name="job-seekers"),
    path("seekers/", SeekerListView.as_view(), name="seekers"),
    path(
        "jobs/<job_slug>/create-seeker/",
        SeekerCreateView.as_view(),
        name="create-seeker",
    ),
    path("seekers/<slug>/", SeekerDetailView.as_view(), name="seeker"),
]
