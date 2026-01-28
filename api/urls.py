from .views import *
from django.urls import path

urlpatterns = [
    path('v1/keep-alive',keep_alive,name='keep-alive'),
    path('v1/home',home,name='home'),
    path('v1/sermons',sermon_list,name='sermon-list'),
    path('v1/sermons/<int:pk>/',sermon_detail,name='sermon-detail'),
    path('v1/visit-us',visit_us,name='visit-us'),
    path('v1/reach-us',reach_us,name='reach-us'),
    path('v1/preacher/<int:pk>/',preacher_bio,name='bio'),
]