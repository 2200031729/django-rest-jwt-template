from .views import ExampleProtectedView, ExampleAdminOnlyView
from django.urls import path

urlpatterns = [
    path("healthcheck/", ExampleProtectedView.as_view(), name="example"),
    path("adminonly/", ExampleAdminOnlyView.as_view(), name="admin-only"),
]
