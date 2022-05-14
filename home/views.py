import json

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from content.models import Content, Menu, Imagen, Comment
from home.forms import SearchFormu
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
    menu = Menu.objects.all()
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
            messages.success(request, "Mesajınız Başarıyla Gönderilmiştir. Teşekkür Ederiz.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    # setting = Setting.objects.all()
    form = ContactFormu()
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
    comments = Comment.objects.filter(content_id=id, status='True')
    # menudata = Menu.objects.get(pk=content.menu_id)
    context = {'content': content,
               'menu': menu,
               'imagens': imagens,
               'comments': comments
               # 'menudata': menudata
               }
    return render(request, 'content_detail.html', context)


def content_search(request):
    menu = Menu.objects.all()
    if request.method == 'POST':  # Check form post
        form = SearchFormu(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']  # Get form data
            contents = Content.objects.filter(title__icontains=query)
            # select * from contents where title like '%query%'
            # return HttpResponse(contents)
            context = {'contents': contents,
                       'menu': menu,
                       }
            return render(request, 'content_search.html', context)

    return HttpResponseRedirect('/')


def content_search_auto(request):
    # if request.is_ajax():
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        q = request.GET.get('term', '')
        contentler = Content.objects.filter(title__icontains=q)
        results = []
        for rs in contentler:
            content_json = {}
            content_json = rs.title  # + "," + rs.type
            results.append(content_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
