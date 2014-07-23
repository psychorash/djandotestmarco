from django.shortcuts import render, render_to_response, RequestContext
from djandotestmarco.apps.social.models import SocialNetWork
from djandotestmarco.apps.main.models import Setting


def index_view(request):
    user=request.user
    redes = SocialNetWork.objects.filter(status=True)
    sett = Setting.objects.filter(status=True)[0]
    ctx = {'networks': redes, 'settings':sett, 'user': user}
    return render_to_response('main/index.html', ctx, context_instance = RequestContext(request))


