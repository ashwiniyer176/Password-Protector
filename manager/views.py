from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse


from .forms import PasswordModelForm
from manager.config import STANDARD_OFFSET
from .models import PasswordModel
# Create your views here.


def encrypt(plainText):
    """
    Standard Caesar Cipher Implementation
    """
    cipherText = ""
    for char in plainText:
        cipherText += chr(ord(char)+STANDARD_OFFSET)
    return cipherText


def decrypt(cipherText):
    """
    Decrypt Caesar Cipher
    """
    plainText = ""
    for char in cipherText:
        plainText += chr(ord(char)-STANDARD_OFFSET)
    return plainText


@login_required(login_url="/accounts/login/")
def showData(request):
    """
    View that shows user's created passwords
    """
    data = PasswordModel.objects.filter(user=request.user)
    for dataObject in data:
        dataObject.passwordSaved = decrypt(dataObject.passwordSaved)
    return render(request, 'home.html', {'data': data})


@login_required(login_url="/accounts/login/")
def addNewPassword(request):
    if(request.method == "POST"):
        form = PasswordModelForm(request.POST)
        if(form.is_valid()):
            instance = form.save(commit=False)
            instance.user = request.user
            instance.passwordSaved = encrypt(instance.passwordSaved)
            instance.save()
            return HttpResponseRedirect(reverse('manager:home'))
    else:
        form = PasswordModelForm()
        return render(request, "manager/newPassword.html", {"form": form})
