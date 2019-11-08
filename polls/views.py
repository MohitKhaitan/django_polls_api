from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Poll

MAX_OBJECTS = 20


def polls_list(request):
    """
    Fetches a list of polls. MAX LENGTH = 20
    :param request: Http Headers
    :return: List of polls. MAX = 20
    """

    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {
        'result': list(polls.values('question', 'created_by__username', 'pub_date'))
    }
    return JsonResponse(data)


def polls_details(request, pk):
    """
    To get details for specific poll
    :param request: Http Headers
    :param pk: Poll id for which the details needs to be returned
    :return: Details associated with the passed poll id (pk)
    """
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        'result': {
            'question': poll.question,
            'created_by': poll.created_by.username,
            'pub_date': poll.pub_date
        }
    }
    return JsonResponse(data)
