from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import *

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    
    #override get context data method
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)# first, call super get context data
        context['about'] = About.objects.all()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        return context