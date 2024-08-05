from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from .forms import GenderselectForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, View, TemplateView
from account.models import User
from .models import Genderselect

def intex(request):
    return render(request, 'shared/base.html')

class GenderselectView(FormView):
    template_name = 'Dating/selectgender.html'
    form_class = GenderselectForm
    success_url = 'Dating:index'

    def form_valid(self, form):
        intrested_in = form.cleaned_data['genderselect']
        return super().form_valid(form)

class Gridview(TemplateView):
    template_name = 'Dating/gridview.html'

class Educationview(TemplateView):
    template_name = 'Dating/education.html'

class Locationview(TemplateView):
    template_name = 'Dating/location.html'

class Desiginationview(TemplateView):
    template_name = 'Dating/pro.html'

class Matchesview(TemplateView):
    template_name = 'Dating/matchs.html'

class Discoverview(TemplateView):
    template_name = 'Dating/discover.html'
    
class Profileview(TemplateView):
    template_name = 'Dating/viewedprofile.html'

class Errorview(TemplateView):
    template_name = 'shared/error404.html'