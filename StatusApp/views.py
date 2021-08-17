from django.shortcuts import render, redirect, reverse
from StatusApp.models import Placement
from .models import Placement
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.http import Http404, HttpResponse
from .forms import PlacementCreateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

import pickle
# Create your views here.

# signup
class SignUp(CreateView):
  form_class=UserCreationForm
  success_url=reverse_lazy("login")
  template_name="registration/signup.html"


  


# home view page

@login_required
def home(request):
  context = {
    "name": "Ibrahim",
     "name_two": request.user
  }
  return render(request, 'StatusApp/home.html', context)



#logout
def logout_view(request):
  logout(request)
  return redirect("home")


# Placement ListView
class PlacementList(LoginRequiredMixin,ListView):
    model=Placement
    template_name="StatusApp/placement_list.html"


# Create View

class PlacementCreate(CreateView):
    model=Placement
    template_name="StatusApp/student_create_form.html"
    form_class = PlacementCreateForm

# placement Create Request
def StudentCreate(request):
  if request.method == "POST":
    form = PlacementCreateForm(request.POST)
    # Add the form validation below:
    if form.is_valid():
      form=form.save()
  else:
    form = PlacementCreateForm()
  return render(request, "StatusApp/student_create_form.html", {"form":form})




# method for generating predictions

def getPredictions(sec_score,highSec_score,degree_score,etest_score,mba_score):
    x=[sec_score, highSec_score, degree_score, etest_score, mba_score]
    model=pickle.load(open("Job_Placement_ml_model.sav", "rb"))
    scaled = pickle.load(open("scaler.sav", "rb"))
    prediction = model.predict(scaled.transform([x]))
    if prediction == 0:
        return "NOT PLACED"
    elif prediction == 1:
        return "PLACED"
    else:
        return "error"


# result page view
def result(request):
    sec_score = int(request.POST.get('sec_score'))
    highSec_score = int(request.POST.get('highSec_score'))
    degree_score = int(request.POST.get('degree_score'))
    etest_score = int(request.POST.get('etest_score'))
    mba_score = int(request.POST.get('mba_score'))
    result = getPredictions(sec_score, highSec_score, degree_score, etest_score, mba_score)
    result.save()
    context={'result':result}
    return render(request, 'StatusApp/result.html', context)

    
  


