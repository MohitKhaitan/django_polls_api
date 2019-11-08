from django.urls import path
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path('polls/<int:pk>/choice/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choice/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
]
