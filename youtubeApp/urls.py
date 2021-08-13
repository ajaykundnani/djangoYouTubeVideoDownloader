from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('dowload/<str:id>',views.dowload,name='dowload')
   
]
