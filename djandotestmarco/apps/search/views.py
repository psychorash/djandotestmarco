from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic import ListView
from djandotestmarco.apps.main.models import Setting

class SearchView(ListView):
    model = Setting
    select_related = ['settings_name']
    template_name = 'search/search.html'
    context_object_name = 'user_list'
    paginate_by = 10  #and that's it !!


    def get_queryset(self):
         query = self.request.REQUEST.get("q")
         return self.model.objects.filter(settings_name__icontains=query)