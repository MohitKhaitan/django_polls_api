from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    """
    Poll Model to store Polls data
    """
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now=True)

    def __str__(self: str) -> str:
        """
        Returns the questions associated with a poll
        :return: Question associated with the poll
        """
        return self.question


class Choice(models.Model):
    """
    Choice model to store choices of a Poll
    """
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self: str) -> str:
        """
        Returns the choice_text associated with the poll question
        :return:
        """
        return self.choice_text


class Vote(models.Model):
    """
    Vote model to store the count of vote per poll
    """
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("poll", "voted_by")

