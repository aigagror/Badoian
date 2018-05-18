from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player/<int:user_id>/', views.player, name='player'),
    path('assignments/', views.assignments, name='assignments'),

    path('create_assignment/', views.create_assignment, name='create_assignment'),
    path('delete_assignment/', views.delete_assignment, name='delete_assignment'),

    path('submission/<int:submission_id>/', views.submission, name='submission'),
    path('create_submission/', views.create_submission, name='create_submission'),
    path('delete_submission/', views.delete_submission, name='delete_submission'),
    path('submit_submission/', views.submit_submission, name='submit_submission'),

    path('scores/', views.scores, name='scores'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('rounds/', views.rounds, name='rounds'),
    path('round_file/<int:round_id>/', views.round_file, name='round_file'),
    path('create_rounds/', views.create_rounds, name='create_rounds'),
    path('delete_round/', views.delete_round, name='delete_round'),
]
