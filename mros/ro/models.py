from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class MeetingRoom(models.Model):
    name = models.CharField(max_length=50)


class MeetingRoomBinding(models.Model):
    meeting_room = models.ForeignKey("MeetingRoom", on_delete=models.CASCADE)
    date = models.DateField()
    start = models.IntegerField(
            default=0,
            validators=[MaxValueValidator(24), MinValueValidator(0)])

    end = models.IntegerField(
            default=1,
            validators=[MaxValueValidator(24), MinValueValidator(0)])

    # approved or not
    status = models.BooleanField(default=False)
    applyed_by = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='applier')
    approved_by = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='approver')

