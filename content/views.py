from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from content.models import CommentFormu, Comment


def index(request):
    return HttpResponse("Content Page")


@login_required(login_url='/login')  # Check Login
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    if request.method == 'POST':  # check if form posted
        form = CommentFormu(request.POST)
        if form.is_valid():
            current_user = request.user  # Access User Session information
            data = Comment()  # connect to model
            data.user_id = current_user.id
            data.content_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')  # Client computer ip address
            data.save()  # save in to database
            messages.success(request, "Yorumunuz Başarıyla Gönderilmiştir. Teşekkür Ederiz.")
            return HttpResponseRedirect(url)
    messages.warning(request, "Kaydetme İşlemi Başarısız!")
    return HttpResponseRedirect(url)
