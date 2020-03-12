import json

from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from app2.models import NoteData
from .forms import NoteForm
import datetime

now = datetime.datetime.now().date()


# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class Create(View):
    def get(self, request):
        data = NoteData.objects.all()
        if data:
            data = serialize('json', data)
            return HttpResponse(data, content_type="application/json")
        else:
            msg = {"msg": "Data Not Available."}
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")
    def post(self, request):
        data = request.body
        d1 = json.loads(data)
        print(d1)
        nf = NoteForm(d1)
        if nf.is_valid():
            nf.save()
            msg = {"msg": "NoteBook added successfully."}
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")
        else:
            msg = {"msg": "Invalid Details."}
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")


@method_decorator(csrf_exempt, name='dispatch')
class Update(View):
    def get(self, request, pk):
        data = NoteData.objects.get(id=pk)
        if data:
            data = serialize('json', [data])
            return HttpResponse(data, content_type="application/json")
        else:
            msg = {"msg": "Data Not Available."}
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")
    def put(self, request, pk):
        data = request.body
        new_data = json.loads(data)
        old_data = NoteData.objects.get(id=pk)
        old_data_dict = {"id":old_data.id, "username":old_data.username, "note":old_data.note, "data":old_data.data, "updatedate":now}
        old_data_dict.update(new_data)

        nf = NoteForm(old_data_dict, instance=old_data)

        if nf.is_valid():
            nf.save()
            msg = {"msg": "NoteBook Updated successfully."}
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")
        else:
            msg = {"msg": "Invalid Details."}
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")


@method_decorator(csrf_exempt, name='dispatch')
class Filter(View):
    def get(self, request, pk):
        data = NoteData.objects.get(id=pk)
        if data:
            data = serialize('json', [data])
            return HttpResponse(data, content_type="application/json")
        else:
            msg = {"msg": "Data Not Available."}
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")


@method_decorator(csrf_exempt, name='dispatch')
class FilterDate(View):
    def get(self, request,pk):
        data = NoteData.objects.filter(data=pk)
        if data:
            data = serialize('json', data)
            return HttpResponse(data, content_type="application/json")
        else:
            msg = {"msg": "Data Not Available."}
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")
