from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic import ListView
from djandotestmarco.apps.main.models import Setting
from django import http
from django.http import HttpResponse
from django.utils import simplejson as json
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.core import serializers

class SearchView(ListView):
    model = Setting
    select_related = ['settings_name']
    template_name = 'search/search.html'
    context_object_name = 'user_list'
    paginate_by = 10  #and that's it !!


    def get_queryset(self):
         query = self.request.REQUEST.get("q")
         return self.model.objects.filter(settings_name__icontains=query)


class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)




class UserProfileAJAXView(TemplateView):
    model = Setting
    context_object_name = 'user_list'
    select_related = ['settings_name']
    def get(self, request, *args, **kwargs):
        id = request.GET['id']
        settings = self.model.objects.filter(settings_name__icontains=id)
        data = serializers.serialize('json', settings, fields=('settings_name', 'my_name'))
        return HttpResponse(data, mimetype='application/json')