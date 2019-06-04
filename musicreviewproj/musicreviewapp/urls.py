from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getalbums/', views.getalbums, name='albums'),
    path('albumdetails/<int:id>', views.albumdetails, name='albumdetails'),
    path('newAlbum/', views.newAlbum, name='newalbum'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    path('newReview/', views.newReview, name='newreview'),
]