from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

import lettings.views as lt_views
import profiles.views as pf_views
import oc_lettings_site.views as views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", lt_views.lettings_index, name="lettings_index"),
    path("lettings/<int:letting_id>/", lt_views.letting, name="letting"),
    path("profiles/", pf_views.profiles_index, name="profiles_index"),
    path("profiles/<str:username>/", pf_views.profile, name="profile"),
    path("admin/", admin.site.urls),
    path("page-404/", TemplateView.as_view(template_name="404.html"), name="page_404"),
    path("page-500/", TemplateView.as_view(template_name="500.html"), name="page_500"),
    path("error-test-500/", views.server_error, name="error_test_500"),
]

# test
