from django.urls import path
from .views import polls_list, polls_details

urlpatterns = [
    path('polls/', polls_list, name='polls_list'),
    path('polls/<int:pk>/', polls_details, name='polls_details')
]
