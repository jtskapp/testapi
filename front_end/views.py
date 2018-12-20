from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q, CharField, Value, F, ExpressionWrapper
from django.db.models.functions import Length, Substr
from front_end.models import UserInfo

# Create your views here.
def index(request):
    return render(request, template_name='front_end/index.html', context={'status' : 'ok'})

def navbar(request):
    return render(request, template_name='front_end/navbar-demo.html', context={'status' : 'ok'})

def dashboard(request):
    return render(request, template_name='front_end/dashboard.html', context={'status' : 'ok'})

def element(request):
    return render(request, template_name='front_end/element.html', context={'status' : 'ok'})

def tables(request):
    return render(request, template_name='front_end/tables.html', context={'status' : 'ok'})

class Bs4(ListView):
    queryset = UserInfo.objects.all()
    template_name = 'front_end/bs4.html'
    context_object_name = 'user_info_list'

    def get_queryset(self, *args, **kwargs):
        queryset = super(Bs4, self).get_queryset(**kwargs)
        queryset = UserInfo.objects.values('samaccountname','enabled','name','adspath','canonicalname').annotate(
            ou=ExpressionWrapper(
                Substr(F('canonicalname'), 1 , (Length(F('canonicalname')) - Length(F('name'))) - 1),
                output_field=CharField()))
        return queryset[:50]

    def get_context_data(self, *args, **kwargs):
        qs = self.get_queryset(**kwargs)
        context = super(Bs4, self).get_context_data(**kwargs)
        context['total_count'] = qs.count()
        context['summary'] = {
            'info' : [
                {'countryfinal' : 'Singapore', 'hwtype' : 'UserPC', 'totalcount' : 1000},
                {'countryfinal' : 'Singapore', 'hwtype' : 'Laptop', 'totalcount' : 12},
                {'countryfinal' : 'Singapore', 'hwtype' : 'Shared', 'totalcount' : 10}
            ]}
        return context
