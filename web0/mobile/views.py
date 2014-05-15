from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from mobile.models import Soul
import json
from django.core import serializers

# Create your views here.



def index(request):
    latest_soul_list = Soul.objects.order_by("-date")[:10]
    context = {'latest_soul_list':latest_soul_list}
    return render(request,'mobile/index.html',context)


def detail(request, soul_id):
    soul = get_object_or_404(Soul, pk=soul_id)
    return render(request, 'mobile/detail.html', {'soul': soul})

@csrf_exempt
def submit(request):
    try:
        json_data = request.read()
        numRecords = numErrors = 0
        for obj in serializers.deserialize("json",json_data):
            try:
                obj.save()
                numRecords = numRecords+1
            except DeserializationError:
                numErrors = numErrors + 1
        return render(request,'mobile/submitSuccess.html',{'numRecords':numRecords,'numErrors':numErrors})
    except KeyError:
        return render(request,'mobile/missingData.html',{})


### Utilities below are for internal usage only.
def postJson(request):
    import urllib2
    # Whatever structure you need to send goes here:
    jdata = json.dumps({"username":"abc", "password":"def"})
    urllib2.urlopen("http://127.0.0.1:8000/mobile/submit", jdata)