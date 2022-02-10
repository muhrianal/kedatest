from django.contrib import admin
from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('material/create', views.add_material, name='add-material'),
    path('materials', views.view_materials, name='view-materials'),
    path('material/update/<str:pk>', views.update_material, name='update-material'),
    path('material/delete/<str:pk>', views.delete_material, name='delete-material'),
]