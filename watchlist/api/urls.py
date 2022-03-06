from django.urls import path
from watchlist.api import views


app_name = 'watchlist'

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', views.StreamPlatformList.as_view(), name='stream-list'),
    path('stream/<int:pk>/', views.StreamDetail.as_view(), name='stream-detail'),
    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review/', views.ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),

    #path('reviews/<str:username>/', views.ReviewUser.as_view(), name='review-user'),

    path('reviews/', views.ReviewUser.as_view(), name='review-user'),

]
