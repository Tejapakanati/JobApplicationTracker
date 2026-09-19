from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_job_application, name="add_job"),
    path("edit/", views.edit_applications, name="edit_applications"),
    path("edit/<int:id>/", views.edit_application, name="edit_application"),
    path("delete/<int:id>/", views.delete_application, name="delete_application"),
    #path("search/" , views.search_application , name="search_application"),
]