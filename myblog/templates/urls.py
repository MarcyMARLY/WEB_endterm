from django.urls import path

from . import views
app_name = 'templates'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('newblog/',views.newblog, name = 'newblog'),
    path('createblog/',views.blogFunc, name = 'createblog'),
    path('<int:id>/editblog/',views.updateblog, name = 'editblog'),
    path('<int:id>/save/',views.save, name = 'save'),
    path('<int:id>/delete/',views.delete, name = 'delete'),

]
