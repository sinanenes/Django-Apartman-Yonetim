from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from content.models import Menu, Comment
from home.models import UserProfile
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
