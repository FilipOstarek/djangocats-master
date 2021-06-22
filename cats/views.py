from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from cats.models import Description_of_the_cat, Species, Photo
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from cats.forms import KockaModelForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache

def indexu(request):
    number = Description_of_the_cat.objects.all().count()
    print(request)
    context = {
        'number': number,
    }
    return render(request, 'index.html', context=context)

class KockaListView(ListView):
    print(ListView)
    model = Description_of_the_cat
    context_object_name = 'cats_photo'
    template_name = 'page/list.html'
    paginate_by = 12

    def get_queryset(self):
        return Description_of_the_cat.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number'] = len(self.get_queryset())
        context['nazev'] = 'Karty koček'
        context['nazev_poctu'] = 'Počet záznamů :'
        return context

class KockaDetailView(DetailView):
    model = Description_of_the_cat

    context_object_name = 'kocka_detail'   # your own name for the list as a template variable
    template_name = 'page/detail.html'  # Specify your own template name/location


class KockaCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Description_of_the_cat
    template_name = 'forms/bootstrap_form.html'
    form_class = KockaModelForm
    #fields = ['jmeno', 'vek', 'vaha', 'popisek', 'druh', 'foto']
    login_url = '/accounts/login/'
    permission_required = 'cats.add_description_of_the_cat'

class KockaUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Description_of_the_cat
    template_name = 'forms/bootstrap_form.html'
    form_class = KockaModelForm
    #fields = '__all__' # Not recommended (potential security issue if more fields added)
    login_url = '/accounts/login/'
    permission_required = 'cats.change_description_of_the_cat'


class KockaDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Description_of_the_cat
    template_name = 'forms/confirm_delete.html'
    success_url = reverse_lazy('index')
    login_url = '/accounts/login/'
    permission_required = 'cats.delete_description_of_the_cat'

