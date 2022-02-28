from django.urls import path
from watchlist.api import views


app_name = 'watchlist'

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', views.StreamPlatformList.as_view(), name='stream'),
]