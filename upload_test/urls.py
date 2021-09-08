from . import views
from django.urls import path


app_name = 'upload_test'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    path('upload/results/', views.results, name='results'),
]