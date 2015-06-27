# Standard Library
from datetime import datetime

# Django
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# My Apps
from .models import Webinar, FacebookGroup

# Create your views here.
def home(request):
    last_webinar = Webinar.objects.all().filter(date_time__lt=datetime.now())[0]
    next_webinars = Webinar.objects.all().filter(date_time__gt=datetime.now())
    facebook_groups = FacebookGroup.objects.all()

    return render_to_response('home.html', {
        'last_webinar': last_webinar,
        'next_webinars': next_webinars,
        'groups': facebook_groups

    }, context_instance=RequestContext(request))


def webinar_view(request, id):
    webinar = get_object_or_404(Webinar, pk=id)
    return render_to_response('webinar_view.html', {'webinar': webinar}, context_instance=RequestContext(request))
