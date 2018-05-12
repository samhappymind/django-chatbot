# -*- coding: utf-8 -*-

from django.http import JsonResponse

from rest_framework.decorators import api_view
from chatbot import  cache,service
from django.template.context_processors import request
import json
from django.template.context_processors import request
import os
from django.conf import settings
from django.http import HttpResponse


@api_view(['get'])
def chatbot(request):
    query=request.GET['query']            
    model=cache.get_txt_classifier_model()
    result= service.getBotResponse(model, query)  
    #rel = ','.join(str(v) for v in result)
    print ("foo2",result)
    return JsonResponse({"result":result},safe=False)






