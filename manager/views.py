from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import PasswordModelForm

from .models import PasswordModel
# Create your views here.


@login_required(login_url="/accounts/login/")
def showData(request):
    data = PasswordModel.objects.filter(user=request.user)
    return render(request, 'home.html', {'data': data})


@login_required(login_url="/accounts/login/")
def addNewPassword(request):
    if(request.method == "POST"):
        form = PasswordModelForm(request.POST)
        if(form.is_valid()):
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('manager:home'))
    else:
        form = PasswordModelForm()
        return render(request, "manager/newPassword.html", {"form": form})
