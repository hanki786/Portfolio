from django.conf.urls import url
from music import views
from django.views.generic.edit import CreateView,UpdateView,DeleteView

app_name = 'music'

urlpatterns = [

	#/music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    url(r'^register/', views.UserFormView.as_view(), name='register'),
    
    #/music/1
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    
    #/music/1/album/add/
    url(r'^album/add/$', views.CreateAlbum.as_view(), name='album-add'),
    
    #/music/1/album/1/
    url(r'^album/(?P<pk>[0-9]+)/$', views.UpdateAlbum.as_view(), name='album-update'),
    
    #/music/1/album/1/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.DeleteAlbum.as_view(), name='album-delete'),


]





