from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MeetingRoom, MeetingRoomBinding

# Create your views here.
def index(request):
    rooms = MeetingRoom.objects.all()
    paginator = Paginator(rooms, 2)
    page_num = request.GET.get('page')
    page_objs = paginator.get_page(page_num)
    context = {'rooms': page_objs}
    return render(request, 'ro/index.html', context)
