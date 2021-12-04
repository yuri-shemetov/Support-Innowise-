from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user'),
    path('tickets/', views.TicketList.as_view(), name='tickets'),
    path('tickets/<int:pk>/', views.TicketDetail.as_view(), name='ticket'),
    path('comments/', views.CommentList.as_view(), name='comments'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment'),
    path('', views.MainPage.as_view(), name='main'),
]

urlpatterns = format_suffix_patterns(urlpatterns)