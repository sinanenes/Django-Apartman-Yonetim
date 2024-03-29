from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from content.models import Menu, Comment, Content, ContentFormu, ContentImageFormu, Imagen
from demand.models import Demand, DemandFormu
from home.models import UserProfile
from payment.models import Payment, PaymentFormu
from user.forms import UserUpdateFormu, ProfileUpdateFormu


@login_required(login_url='/login')  # Check login
def index(request):
    menu = Menu.objects.all()
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'menu': menu,
               'profile': profile
               }
    return render(request, 'user_profile.html', context)


@login_required(login_url='/login')  # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateFormu(request.POST, instance=request.user)  # request.user is user data
        # "instance=request.user.userprofile" comes from "userprofile" model -> OneToOneField relation
        profile_form = ProfileUpdateFormu(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(user_form.errors) + str(profile_form.errors))
            return HttpResponseRedirect('/user/update')
    else:
        menu = Menu.objects.all()
        # current_user = request.user  # access user information
        user_form = UserUpdateFormu(instance=request.user)
        profile_form = ProfileUpdateFormu(instance=request.user.userprofile)  # "userprofile" model -> OneToOneField relation with user
        context = {
            'menu': menu,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


@login_required(login_url='/login')  # Check login
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        menu = Menu.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form, 'menu': menu})


@login_required(login_url='/login')  # Check login
def comments(request):
    menu = Menu.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        'menu': menu,
        'comments': comments,
    }
    return render(request, 'user_comments.html', context)


@login_required(login_url='/login')  # Check login
def deletecomment(request, id):
    try:
        current_user = request.user
        HttpResponse(current_user.id)
        Comment.objects.filter(id=id, user_id=current_user.id).delete()
        messages.success(request, 'Comment Successfully Deleted!')
        return HttpResponseRedirect('/user/comments')
    except:
        messages.warning(request, "Hata! Yorum Silinemedi!")
        return HttpResponseRedirect('/error')


@login_required(login_url='/login')  # Check login
def contents(request):
    menu = Menu.objects.all()
    current_user = request.user
    contents = Content.objects.filter(user_id=current_user.id)
    context = {
        'menu': menu,
        'comments': comments,
        'contents': contents,
    }
    return render(request, 'user_contents.html', context)


@login_required(login_url='/login')  # Check login
def addcontent(request):
    if request.method == 'POST':
        form = ContentFormu(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Content()  # model ile baglanti
            data.user_id = current_user.id
            data.menu = form.cleaned_data['menu']
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.type = form.cleaned_data['type']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save()  # veri tabanina kaydet
            messages.success(request, "Your Content Inserted Successfully!")
            return HttpResponseRedirect('/user/contents')
        else:
            messages.error(request, 'Content Form Error:' + str(form.errors))
            return HttpResponseRedirect('/user/addcontent')
    else:
        menu = Menu.objects.all()
        form = ContentFormu()
        context = {
            'menu': menu,
            'form': form
        }
        return render(request, 'user_addcontent.html', context)


@login_required(login_url='/login')  # Check login
def contentedit(request, id):
    content = Content.objects.get(id=id)
    if request.method == 'POST':
        form = ContentFormu(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Content Updated Successfully!")
            return HttpResponseRedirect('/user/contents')
        else:
            messages.error(request, 'Content Form Error:' + str(form.errors))
            return HttpResponseRedirect('/user/contentedit/' + str(id))
    else:
        menu = Menu.objects.all()
        form = ContentFormu(instance=content)
        context = {
            'menu': menu,
            'form': form
        }
        return render(request, 'user_addcontent.html', context)


@login_required(login_url='/login')  # Check login
def contentdelete(request, id):
    current_user = request.user
    Content.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Content deleted..')
    return HttpResponseRedirect('/user/contents')


def contentaddimage(request, id):
    if request.method == 'POST':
        lasturl = request.META.get('HTTP_REFERER')
        form = ContentImageFormu(request.POST, request.FILES)
        if form.is_valid():
            data = Imagen()
            data.title = form.cleaned_data['title']
            data.content_id = id
            data.image = form.cleaned_data['image']
            data.save()
            messages.success(request, 'Your image has been successfully uploaded!')
            return HttpResponseRedirect(lasturl)
        else:
            messages.warning(request, 'Form Error :' + str(form.errors))
            return HttpResponseRedirect(lasturl)
    else:
        content = Content.objects.get(id=id)
        images = []
        try:
            images = Imagen.objects.filter(content_id=id)
        except:
            pass
        form = ContentImageFormu()
        context = {
            'content': content,
            'images': images,
            'form': form
        }
        return render(request, 'content_gallery.html', context)


@login_required(login_url='/login')  # Check login
def demands(request):
    menu = Menu.objects.all()
    current_user = request.user
    userdemands = Demand.objects.filter(user_id=current_user.id)
    context = {
        'menu': menu,
        'userdemands': userdemands,
    }
    return render(request, 'user_demands.html', context)


@login_required(login_url='/login')  # Check login
def adddemand(request):
    if request.method == 'POST':
        demandForm = DemandFormu(request.POST, request.FILES)
        if demandForm.is_valid():
            current_user = request.user
            data = Demand()  # model ile baglanti
            data.user_id = current_user.id
            data.type = demandForm.cleaned_data['type']
            data.subject = demandForm.cleaned_data['subject']
            data.detail = demandForm.cleaned_data['detail']
            data.status = 'New'
            data.save()  # veri tabanina kaydet
            messages.success(request, "Your Demand Inserted Successfully!")
            return HttpResponseRedirect('/user/demands')
        else:
            messages.error(request, 'Demand Form Error:' + str(demandForm.errors))
            return HttpResponseRedirect('/user/adddemand')
    else:
        menu = Menu.objects.all()
        demandForm = DemandFormu()
        context = {
            'menu': menu,
            'demandForm': demandForm
        }
        return render(request, 'user_adddemand.html', context)


@login_required(login_url='/login')  # Check login
def demandedit(request, id):
    demand = Demand.objects.get(id=id)
    if request.method == 'POST':
        demandForm = DemandFormu(request.POST, request.FILES, instance=demand)
        if demandForm.is_valid():
            demandForm.save()
            messages.success(request, "Your Demand Updated Successfully!")
            return HttpResponseRedirect('/user/demands')
        else:
            messages.error(request, 'Demand Form Error:' + str(demandForm.errors))
            return HttpResponseRedirect('/user/demandedit/' + str(id))
    else:
        menu = Menu.objects.all()
        demandForm = DemandFormu(instance=demand)
        context = {
            'menu': menu,
            'demandForm': demandForm
        }
        return render(request, 'user_adddemand.html', context)


@login_required(login_url='/login')  # Check login
def demanddelete(request, id):
    current_user = request.user
    Demand.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Demand deleted..')
    return HttpResponseRedirect('/user/demands')


@login_required(login_url='/login')  # Check login
def payments(request):
    menu = Menu.objects.all()
    current_user = request.user
    userpayments = Payment.objects.filter(user_id=current_user.id)
    context = {
        'menu': menu,
        'userpayments': userpayments,
    }
    return render(request, 'user_payments.html', context)


@login_required(login_url='/login')  # Check login
def addpayment(request):
    if request.method == 'POST':
        paymentForm = PaymentFormu(request.POST, request.FILES)
        if paymentForm.is_valid():
            current_user = request.user
            data = Payment()  # model ile baglanti
            data.user_id = current_user.id
            data.type = paymentForm.cleaned_data['type']
            data.year = paymentForm.cleaned_data['year']
            data.month = paymentForm.cleaned_data['month']
            data.payment = paymentForm.cleaned_data['payment']
            data.status = 'Yeni'
            data.save()  # veri tabanina kaydet
            messages.success(request, "Your Payment Inserted Successfully!")
            return HttpResponseRedirect('/user/payments')
        else:
            messages.error(request, 'Payment Form Error:' + str(paymentForm.errors))
            return HttpResponseRedirect('/user/addpayment')
    else:
        menu = Menu.objects.all()
        paymentForm = PaymentFormu()
        context = {
            'menu': menu,
            'paymentForm': paymentForm
        }
        return render(request, 'user_addpayment.html', context)


@login_required(login_url='/login')  # Check login
def paymentedit(request, id):
    payment = Payment.objects.get(id=id)
    if request.method == 'POST':
        paymentForm = PaymentFormu(request.POST, request.FILES, instance=payment)
        if paymentForm.is_valid():
            paymentForm.save()
            messages.success(request, "Your Payment Updated Successfully!")
            return HttpResponseRedirect('/user/payments')
        else:
            messages.error(request, 'Payment Form Error:' + str(paymentForm.errors))
            return HttpResponseRedirect('/user/paymentedit/' + str(id))
    else:
        menu = Menu.objects.all()
        paymentForm = PaymentFormu(instance=payment)
        context = {
            'menu': menu,
            'paymentForm': paymentForm
        }
        return render(request, 'user_addpayment.html', context)


@login_required(login_url='/login')  # Check login
def paymentdelete(request, id):
    current_user = request.user
    Payment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Payment deleted..')
    return HttpResponseRedirect('/user/payments')
