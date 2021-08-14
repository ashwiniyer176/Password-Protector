from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse


from .forms import PasswordModelForm
from manager.config import STANDARD_OFFSET
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
            instance.save()
            return HttpResponseRedirect(reverse('manager:home'))
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
            form.save()
            return HttpResponseRedirect(reverse('manager:home'))
    return render(request, "manager/editPassword.html", {"form": form, "itemID": itemID})
