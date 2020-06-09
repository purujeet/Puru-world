from django.urls import path

from . import views

urlpatterns=[
        path('',views.index,name='index'),
        path('videos',views.videos,name='video'),
        path('apps',views.apps,name='app'),
        ]
