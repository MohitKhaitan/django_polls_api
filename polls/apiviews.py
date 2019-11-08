from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


class PollList(APIView):
    """
    To get the list of polls. MAX 20
    """
    @staticmethod
    def get(request: Request) -> Response:
        """
        GET method to fetch a list of polls. MAX 20 polls
        :param request: Http request object
        :return: Response Object. List of polls. MAX 20
        """
        polls = Poll.objects.all()[:20]
        data = PollSerializer(polls, many=True).data
        return Response(data=data, status=status.HTTP_200_OK, content_type=request.content_type)


class PollDetail(APIView):
    """
    To get details of a specific poll.
    """
    @staticmethod
    def get(request: Request, pk: int) -> Response:
        """
        GET method to fetch specific poll details
        :param request: Http request object
        :param pk: Poll id for which details need to be fetched
        :return: Response Object. Poll details
        """
        poll = get_object_or_404(Poll, pk=pk)
        data = PollSerializer(poll).data
        return Response(data=data, status=status.HTTP_200_OK, content_type=request.content_type)


class ChoiceList(APIView):
    """
    To get the list of choices associated with a poll
    """
    @staticmethod
    def get(request: Request, pk: int) -> Response:
        """
        GET method to fetch a list of choices with a poll
        :param request: Http request object
        :param pk: Poll id for which choices needs to be fetched
        :return: Response Object. Choice list
        """
        choice = Choice.objects.filter(poll_id=pk)
        data = ChoiceSerializer(choice, many=True).data
        return Response(data=data, status=status.HTTP_200_OK, content_type=request.content_type)


class CreateVote(APIView):
    """
    Registers a vote for a poll's choice
    """
    @staticmethod
    def post(request: Request, pk: int, choice_pk: int) -> Response:
        """
        POST method to allow user to vote for a poll
        :param request: HTTP Request
        :param pk: Poll id for which vote needed to be cast
        :param choice_pk: Choice id for which vote needed to be cast
        :return: Response Object. Success message
        """
        voted_by = request.data.get('voted_by')
        data = {
            'choice': choice_pk,
            'poll': pk,
            'voted_by': voted_by
        }
        vote_serializer = VoteSerializer(data=data)
        if vote_serializer.is_valid():
            vote_serializer.save()
            return Response(vote_serializer.data, status=status.HTTP_200_OK, content_type=request.content_type)
        else:
            return Response(vote_serializer.errors, status=status.HTTP_400_BAD_REQUEST,
                            content_type=request.content_type)
