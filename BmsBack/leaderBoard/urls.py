from django.contrib import admin
from django.urls import path,re_path
from . import views


urlpatterns = [
    path('register', views.PostLeaderBoardData.as_view(), name="register"),
    path('get-leaderboard', views.get_leaderboard_elements.as_view(), name="getleaderboard"),

]