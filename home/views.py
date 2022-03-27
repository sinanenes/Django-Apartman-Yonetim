from django.shortcuts import render


# Create your views here.
def index(request):
    text = "Merhaba Django (context)!!! <br> Django Kurulumu: python -m pip install Django <br> Proje Olusturma: " \
           "django-admin startproject mysite <br> App Ekleme: python manage.py startapp polls"
    context = {'text': text}
    return render(request, 'index.html', context)
    # return HttpResponse("Su anda home_views.py index metodundan ilk karsilama mesajini gormektesiniz: %s" % text)
