from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from .forms import PasswordModelForm
from .models import PasswordModel
# Create your views here.


@login_required(login_url="/accounts/login/")
def showData(request):
    """
    View that shows user's created passwords
    """
    data = PasswordModel.objects.filter(user=request.user)
    return render(request, 'home.html', {'data': data})


@login_required(login_url="/accounts/login/")
def addNewPassword(request):
    if(request.method == "POST"):
        form = PasswordModelForm(request.POST)
        if(form.is_valid()):
            instance = form.save(commit=False)
            instance.user = request.user
            # similarInstances = PasswordModel.objects.filter(
            #     websiteName=instance.websiteName, passwordSaved=instance.passwordSaved, user=instance.user)
            # if(len(similarInstances) == 0):
            instance.save()
            return HttpResponseRedirect(reverse('manager:home'))
            # else:
            #     return HttpResponse("Cannot add 2 same objects")
    else:
        form = PasswordModelForm()
        return render(request, "manager/newPassword.html", {"form": form})


@login_required(login_url="/accounts/login/")
def editPassword(request, itemID):
    passwordObject = PasswordModel.objects.get(id=itemID)
    form = PasswordModelForm(instance=passwordObject)
    if(request.method == "POST"):
        form = PasswordModelForm(request.POST, instance=passwordObject)
        if(form.is_valid()):
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('manager:home'))
    return render(request, "manager/newPassword.html", {"form": form, "itemID": itemID})


@login_required(login_url="/accounts/login")
def deletePassword(request, itemID):
    instance = PasswordModel.objects.get(id=itemID)
    instance.delete()
    return HttpResponseRedirect(reverse("manager:home"))
