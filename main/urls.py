from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assignments/', views.assignments, name='assignments'),
    path('statistics/', views.statistics, name='statistics'),
    path('rounds/', views.rounds, name='rounds'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('create_rounds/', views.create_rounds, name='create_rounds'),
    path('delete_round/', views.delete_round, name='delete_round'),
]