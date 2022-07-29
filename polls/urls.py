from django.urls import path

from polls import views

urlpatterns = [
    path('', views.polls_list, name='polls_list'),
    path('pool/<int:pk>/', views.poll_details, name='poll_details'),
    path('poll_edit/', views.poll_create, name='poll_create'),
    path('my_polls/', views.polls_user, name='my_polls'),
    path('results/', views.results, name='results'),
    path('results/<int:pk>/', views.result_details, name='result_details')
]
