# views.py
from django import forms
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from .models import UserProfile
import json
import base64
from Crypto.PublicKey import RSA
from Crypto import Random
import binascii

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            private = RSA.generate(1024, Random.new().read)
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],

            )
            print(private)
            print(private.exportKey())
            UserProfile.objects.create(user=user, privateKey=private.exportKey(), publicKey=private.publickey().exportKey())
            #print(private.exportKey())
            priv = private.exportKey('PEM')
            priv_KEY = binascii.b2a_qp(priv).decode('latin_1')
            #print(priv_KEY)
            file = open("privateKeyDowload.txt","w")
            file.write(str(priv))
            privateKeyDownload(request, priv)

            return render_to_response('success.html', {'private': priv_KEY})
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )


def register_success(request):
    return render_to_response(
        'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required#(redirect_field_name='login')
def home(request):
    isSuperUser = False
    if request.user.is_superuser: isSuperUser = True

    return render_to_response(
        'home.html',
        {'user': request.user, 'SM' : isSuperUser}
    )

@csrf_exempt
def createGroup(request):
    if request.method == 'POST':
        user = request.user
        form = GroupForm(request.POST)
        group = form.instance
        g = 0
        if form.is_valid():

            form.save(commit=True)
            group.user_set.add(user)
            count = Group.objects.count()

        return HttpResponseRedirect('/allusers/' + str(count))
    else:
        form = GroupForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'createGroup.html',
        variables,
    )

def changeUserRole(request):
    current_user = request.user.username
    users = User.objects.all()
    return render(request, 'registration/UserRoles.html', {'current_user' : current_user, 'users' : users})

@csrf_exempt
def updatePrivilege(request):
    username = request.POST.get('username')
    isSM = request.POST.get('isSM')
    user = User.objects.get(username=username)
    if isSM == 'true':isSM = True
    else:isSM = False

    if isSM:user.is_superuser = True
    else:user.is_superuser = False

    user.save()
    return HttpResponse(json.dumps(""), status=200, content_type="application/json")


@csrf_exempt
def privateKeyDownload(request, priv):
    print("scott")
    response = HttpResponse(priv)
    response['content_type'] = 'application/txt'
    response['Content-Disposition'] = 'attachment; filename=myfile.zip'
    return response