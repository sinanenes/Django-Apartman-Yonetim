from django.http import HttpResponse
from django.shortcuts import render

from content.models import Menu
from home.models import UserProfile


def index(request):
    menu = Menu.objects.all()
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'menu': menu,
               'profile': profile
               }
    return render(request, 'user_profile.html', context)
