from django.urls import path
from . import views


app_name = "plants"

urlpatterns = [
    path('create', views.create_view, name="create_view"),
    path('edit', views.update_view, name="update_view"),

]