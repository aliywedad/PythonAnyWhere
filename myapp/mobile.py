from django.contrib.auth import authenticate
from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import *
from .serializers import *
import mysql
import json
import smtplib
import random
from django.http import JsonResponse
from datetime import datetime
import pytz

# conn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "pis4")

@api_view(['GET'])
def Connexion(request):
    return Response("connected",status=200)

@api_view(['POST'])
def village_info(request):
    idvillage=request.data.get('id')
    # idform=request.data.get('id')
    villaje=Village.objects.get(NumeroVillage=idvillage)
    # form=Formilair.objects.get(id=idform)
    obj = Reponse.objects.filter(village=villaje)
    if not obj  :
        return Response({"message":"ther is no data for this wilaya"}, status=202)
    serializer = ReponseSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def TypeInfra(request):
    obj = TypeInfrastructure.objects.all()
    serializer = TypeInfrastructureSerializer(obj, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def villageInfra_info(request):
    idvillage=request.data.get('id')
    villaje=Village.objects.get(NumeroVillage=idvillage)
    obj = InfrastructuresVillage.objects.filter(NumeroVillage=villaje)
    if not obj  :
        return Response( status=202)
    serializer = InfrastructuresVillageSerializer(obj, many=True)
    return Response(serializer.data,status=200)


@api_view(['POST'])
def Upload_Reponses(request):
    data = request.data.get('data', [])
    infra = request.data.get('infralist', [])
    
    count=0
    # print(data[0]['id_user'])
    # print(infra)
 
    try:
        user=users.objects.get(id=data[0]['id_user'])
        village=Village.objects.get(NumeroVillage=data[0]['village'])
    except:
        return JsonResponse({"message":"404"})
    try:
        for i in data:
            try:
                Q=Question.objects.get(id=i['question_id'])
                Reponse.objects.create(text_reponse=i['text_reponse'],question_id=Q,response_date=i['response_date'],village=village ,id_user=user )
                count+=1
            except ValueError as e :
                print("erreur ",e)
        for i in infra:
            try:
                infrastructure=Infrastructur.objects.get(id=i['TypeInfrastructure'])
                InfrastructuresVillage.objects.create(NumeroVillage=village,user=user,TypeInfrastructure=infrastructure,NombreNonFonctionnelles=i['NombreNonFonctionnelles'],NombreFonctionnelles=i['NombreFonctionnelles'],NombreTotal=i['NombreTotal'],date_info=i['date_info']  )
                count+=1
            except ValueError as e :
                print("erreur ",e)
        return JsonResponse({ "message": "ok" }, status=200)
    except:
        return JsonResponse({ "message": "ereur" }, status=400)

 










