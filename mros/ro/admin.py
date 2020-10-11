from django.contrib import admin
from .models import MeetingRoom
from .models import MeetingRoomBinding

# Register your models here.
admin.site.register(MeetingRoom)
admin.site.register(MeetingRoomBinding)
