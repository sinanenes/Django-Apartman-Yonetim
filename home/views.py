from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from content.models import Content, Menu, Imagen
from home.models import Setting, ContactFormu, ContactFormMessage


def index(request):
    # setting = Setting.objects.all()
    setting = Setting.objects.get(pk=1)
    sliderdata = Content.objects.all()[:4]
    menu = Menu.objects.all()
    lastcontents = Content.objects.all().order_by('-id')[:4]
    randomcontents = Content.objects.all().order_by('?')[:4]

    context = {'setting': setting,
               'menu': menu,
               'page': 'home',
               'sliderdata': sliderdata,
               'lastcontents': lastcontents,
               'randomcontents': randomcontents
               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    # setting = Setting.objects.all()
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    context = {'setting': setting, 'menu': menu, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    # setting = Setting.objects.all()
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    context = {'setting': setting, 'menu': menu, 'page': 'referanslar'}
    return render(request, 'referanslar.html', context)


def iletisim(request):
    if request.method == 'POST':  # form post edildiyse
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # model ile baglanti
            data.name = form.cleaned_data['name']  # formdan bilgi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # veritabanina kaydet
            messages.success(request, "Mesajınız başarıyla gönderilmiştir. Teşekkür Ederiz.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    # setting = Setting.objects.all()
    form = ContactFormu()
    menu = Menu.objects.all()
    context = {'setting': setting, 'menu': menu, 'form': form}
    # context = {'setting': setting, 'page': 'iletisim'}
    return render(request, 'iletisim.html', context)


def menu_contents(request, id, slug):
    contents = Content.objects.filter(menu_id=id)
    menudata = Menu.objects.get(pk=id)
    menu = Menu.objects.all()
    context = {'contents': contents,
               'menu': menu,
               'menudata': menudata
               }
    return render(request, 'contents.html', context)


def content_detail(request, id, slug):
    menu = Menu.objects.all()
    content = Content.objects.get(pk=id)
    imagens = Imagen.objects.filter(content_id=id)
    # menudata = Menu.objects.get(pk=content.menu_id)
    context = {'content': content,
               'menu': menu,
               'imagens': imagens
               # 'menudata': menudata
               }
    return render(request, 'content_detail.html', context)
