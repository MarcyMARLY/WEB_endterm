from django.urls import path

from . import views

app_name = 'templates_api'

urlpatterns = [
    path('blogs/', views.blog_list),
    path('blogs/<int:id>/', views.blog_detail),

]
