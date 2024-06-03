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
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


# conn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "pis4")

@api_view(['POST'])
def Getforms(request):
    forms_data = []
    id = request.data.get("id")
    formilair = Formilair.objects.get(id=id)
    # for formilair in formilairs:
    form_data = {'formilair': formilair.titre, 'description': formilair.description,  'questions':[]}
    
    questions = Question.objects.filter(formilair=formilair)
    for question in questions:

        # print("****************************************************************")
        question_data = {'id':question.id,'text': question.text,'type':question.type ,'choices':question.choices}
 
        form_data['questions'].append(question_data) 
 
    forms_data.append(form_data)
    
    return Response(forms_data)


@api_view(['GET'])
def forms(request):
    forms_data = []
    formilairs = Formilair.objects.all()
    question=Question.objects.all()

    for formilair in formilairs:
        counter=0
        for i in question:
            if i.formilair==formilair:
                counter+=1
        form_data = { 'id':formilair.id,'formilair': formilair.titre, 'description': formilair.description,'questions':counter}
        forms_data.append(form_data)
    return Response(forms_data)

@api_view(['GET'])
def predict(request):
    forms_data = []
    try:
        categories = Question_backup.objects.values('categorie').distinct()
        for category in categories:
            print(category['categorie'])
            a = { 'categorie':category['categorie'],'sous-categorie':[]}
            b=[]

            questions = Question_backup.objects.filter(categorie=category['categorie']).values('sub_categorie').distinct()
            for i in questions:
                b.append(i)
                print(i["sub_categorie"])
                a['sous-categorie'].append(i["sub_categorie"])
            forms_data.append(a)
        return Response(forms_data)
    except:
        return Response("400")

@api_view(['POST'])
def delet_forms(request):
    id=request.data.get('id')
    try:
        form=Formilair.objects.get(id=id).delete()
        return Response("form deleted")
    except:
        return Response('400')


@api_view(['POST'])
def delQuetion(request):
    id=request.data.get('id')
    try:
        Question.objects.get(id=id).delete()
    except:
        return Reponse('400')
    return Response("200")
 
 

@api_view(['POST'])
def create_formilair(request):
    titr = request.data.get("title")
    description = request.data.get("description")
    # questions_data = request.data.get("questions",[]) 
    # questionPreDefinie = request.data.get("questionPreDefinie",[]) 
    # ifrastricteur=request.data.get('ifrastricteur')
    formilair = Formilair.objects.create(titre=titr, description=description)
    questions_data = request.data.get("questions",[]) 
    # return Response(questions_data)
    for question_data in questions_data:
        text = question_data.get('text')
        choices = question_data.get('choices', '')  
        type_reponse = question_data.get('type')
        # parent = question_data.get('parent')
        # subQuestion = question_data.get('subQuestion')
        categorie = question_data.get('categorie')
        Question.objects.create(formilair=formilair ,categorie=categorie,  text=text, choices=choices, type=type_reponse)

    return Response(status=201)

@api_view(['GET'])
def list_users(request):
    user = users.objects.all()
    if not user  :
        return Response("no data")
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)
    # return Response(serializer.data)
@api_view(['GET'])
def list_Infrastructur(request):
    infra = Infrastructur.objects.all().order_by('type')
    serializer = InfrastructurSerializer(infra, many=True)
    return Response(serializer.data)
    # return Response(serializer.data)

@api_view(['GET'])
def list_TypeInfrastructur(request):
    infra = TypeInfrastructure.objects.all()
    serializer = TypeInfrastructureSerializer(infra, many=True)
    return Response(serializer.data)
    # return Response(serializer.data)


@api_view(['POST'])
def AddWilaye(request):
    data=request.data.get('formData',[])
    done=0
    cancel=0
    for i in data:
        print(i['name'],i['code'])
        try:
            if i['code'] :
                Wilaya.objects.create(Nom_wilaya=i['name'],ID_wilaya=i['code'])
            else :
                Wilaya.objects.create(Nom_wilaya=i['name'])
            done+=1
        except:
            cancel+=1

    return Response(f"200 done : {done} cancel : {cancel} data : {data}")


@api_view(['POST'])
def AddUser(request):
    data=request.data.get('data',[])
    if data['tel']=='':
        data['tel']=0
    # user=users.objects.create(nom=data['nom'],prenom=data['prenom'],tel=data['tel'],email=data['email'],role=data['role'],active=data['active'])

    try:
        user=users.objects.create(nom=data['nom'],prenom=data['prenom'],tel=data['tel'],email=data['email'],role=data['role'],active=data['active'])
        return Response(f"200 done  ")
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    



@api_view(['POST'])
def modifierWilaye(request):
    id = request.data.get('id')
    nom = request.data.get('nom')
    code = request.data.get('code')  # Access the 'wilaya' key from each item
    print("ajoutation du moghataa : ",nom, code)
    
    try:
        # 
        wilaya=Wilaya.objects.get(ID_wilaya=id)
        if wilaya :
            wilaya.Nom_wilaya=nom
            wilaya.ID_wilaya=code
            wilaya.save()
            return Response("Data received and modified successfully")
        return Response({"ther is no wilaya has this code"})
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(['POST'])
def modifierMoughataa(request):
    nom = request.data.get('nom')
    id = request.data.get('id')
    code = request.data.get('code')  # Access the 'wilaya' key from each item
    print("ajoutation du moghataa : ",nom, code)
    wilaye=Wilaya.objects.get(ID_wilaya=code)
    
    try:
        # 
        mog=Moughata.objects.get(ID_maghataa=id)
        if mog :
            mog.Nom_maghataa=nom
            mog.ID_wilaya=wilaye
            mog.save()
            return Response("Data received and modified successfully")
        return Response({"ther is no wilaya has this code"})
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(['POST'])
def modifierCommin(request):
    nom = request.data.get('nom')
    id = int(request.data.get('id'))
    code = int(request.data.get('code'))  # Access the 'wilaya' key from each item
    print("ajoutation du moghataa : ",nom, code)
    moghataa=Moughata.objects.get(ID_maghataa=code)
    commin=Commune.objects.get(ID_commune=id)

    try:
        if commin :
            commin.Nom_commune=nom
            commin.ID_maghataa_id=moghataa
            commin.save()
            return Response("Data received and modified successfully")
        return Response({"ther is no wilaya has this code"})
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(['POST'])
def modifierVillage(request):
    NomAdministratifVillage = request.data.get('NomAdministratifVillage')
    NomLocal = request.data.get('NomLocal')
    id = request.data.get('id')
    DistanceChefLieu = request.data.get('DistanceChefLieu')
    DistanceAxesPrincipaux = request.data.get('DistanceAxesPrincipaux')
    DateCreation = request.data.get('DateCreation')
    CompositionEthnique = request.data.get('CompositionEthnique')
    AutresInfosVillage = request.data.get('AutresInfosVillage')
    idcommin= request.data.get('commin')
    
    print("ajoutation du village : ",id,NomAdministratifVillage, idcommin,NomLocal,DistanceChefLieu,DistanceAxesPrincipaux,DateCreation,CompositionEthnique,AutresInfosVillage)
    villge=Village.objects.get(NumeroVillage=id)
    commin=Commune.objects.get(ID_commune=idcommin) 
    try:
        villge.NomAdministratifVillage=NomAdministratifVillage, 
        villge.idcommin=commin,
        villge.NomLocal=NomLocal
        villge.DistanceChefLieu=DistanceChefLieu
        villge.DistanceAxesPrincipaux=DistanceAxesPrincipaux
        villge.DateCreation=DateCreation
        villge.CompositionEthnique=CompositionEthnique
        villge.AutresInfosVillage=AutresInfosVillage
        villge.save()
        return Response("Data received and modified successfully")
    except Exception as e:
        return Response({"error": str(e)}, status=400)




@api_view(['POST'])
def AddMoughataa(request):
    done = 0
    cancel = 0
    nom = request.data.get('nom')
    idwilaya = request.data.get('wilaya')  # Access the 'wilaya' key from each item
    print("ajoutation du moghataa : ",nom, idwilaya)
    wilaya=Wilaya.objects.get(ID_wilaya=idwilaya)
    try:
        M=Moughata.objects.create(ID_wilaya=wilaya,Nom_maghataa=nom)
        return Response({"Data received successfully"})
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(['POST'])
def AddCommin(request):

    nom = request.data.get('nom')
    idmoghataa = request.data.get('moghataa')  # Access the 'wilaya' key from each item
    print("ajoutation du commin : ",nom, idmoghataa)
    moghataa=Moughata.objects.get(ID_maghataa=idmoghataa)
    try:
        C=Commune.objects.create(ID_maghataa_id=moghataa,Nom_commune=nom)
        return Response({"Data received successfully"})
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(['POST'])
def AddVillage(request):

    NomAdministratifVillage = request.data.get('NomAdministratifVillage')
    NomLocal = request.data.get('NomLocal')
    DistanceChefLieu = request.data.get('DistanceChefLieu')
    DistanceAxesPrincipaux = request.data.get('DistanceAxesPrincipaux')
    DateCreation = request.data.get('DateCreation')
    CompositionEthnique = request.data.get('CompositionEthnique')
    AutresInfosVillage = request.data.get('AutresInfosVillage')
    idcommin= request.data.get('commin')  # Access the 'wilaya' key from each item
    print("ajoutation du commin : ",NomAdministratifVillage, idcommin,NomLocal,DistanceChefLieu,DistanceAxesPrincipaux,DateCreation,CompositionEthnique,AutresInfosVillage)
    commin=Commune.objects.get(ID_commune=idcommin)
    try:
        V=Village.objects.create(idCommit=commin,NomAdministratifVillage=NomAdministratifVillage,NomLocal=NomLocal,DistanceChefLieu=DistanceChefLieu,DistanceAxesPrincipaux=DistanceAxesPrincipaux,DateCreation=DateCreation,CompositionEthnique=CompositionEthnique,AutresInfosVillage=AutresInfosVillage)
        return Response({"Data received successfully"})
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(['GET'])
def list_wilaya(request):
    obj = Wilaya.objects.all().order_by('ID_wilaya')
    if not obj  :
        return Response("no data")
    serializer = WilayaSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['Post'])
def suprimerWilaya(request):
    id=request.data.get('id')
    try:
        wilaye=Wilaya.objects.get(ID_wilaya=id).delete()
        return Response('200')

    except:
        return Response('400')
@api_view(['Post'])
def suprimerUtilisateur(request):
    id=request.data.get('id')
    try:
        user=users.objects.get(id=id).delete()
        return Response('200')

    except:
        return Response('400')
    
@api_view(['Post'])
def modifierEtat(request):
    id=request.data.get('id')
    try:
        user=users.objects.get(id=id)
        etat=user.active
        user.active=not etat
        user.save()
        return Response('200')
    except:
        return Response('400')
# gmt = pytz.timezone('GMT')
# gmt_time = datetime.now(gmt)
# formatted_time = gmt_time.strftime('%Y-%m-%d %H:%M:%S')

# print(formatted_time)
# print("******************************************************************",formatted_time)
@api_view(['Post'])
def Repondre(request):
    if request.method == 'POST':
        # gmt = pytz.timezone('GMT')
        # gmt_time = datetime.now(gmt)
        # formatted_time = gmt_time.strftime('%Y-%m-%d %H:%M:%S')
        gmt = pytz.timezone('GMT')
        gmt_time = datetime.now(gmt)
        formatted_time = gmt_time.strftime('%Y-%m-%d %H:%M:%S')

        data = request.data
        infrastructures = data.get('infrastructures', [])
        dataList = data.get('dataList', [])
        idvillage = data.get('village')
        idUser = data.get('idUser')
        village=Village.objects.get(NumeroVillage=idvillage)   

        print("user:", idUser)
        # print("DataList:", dataList)
        for i in infrastructures:
            if i['fonctionnelles']=="":
                i['fonctionnelles']=0
            if i['nonFonctionnelles']=="":
                i['nonFonctionnelles']=0
            if  i['total']!=0 and  i['typeInfra']!=0  and  i['typeInfra']!="" :

                print(f"ajouter une Infrastructures du Village type ={i['typeInfra']} fonctionnelles = {i['fonctionnelles']} et non fonctionnelles {i['nonFonctionnelles']} pour le village {village.NomAdministratifVillage}")

                infra=Infrastructur.objects.get(id=i['typeInfra'])
                obj=InfrastructuresVillage.objects.create(NumeroVillage=village,TypeInfrastructure=infra,NombreNonFonctionnelles=i['nonFonctionnelles'],NombreFonctionnelles=i['fonctionnelles'],NombreTotal=i['total'],date_info=formatted_time)

        for i in dataList:
            print(" this ****************************************************************")
            print(i,dataList[i])
            if i :
                print(f"ajouter une reponse id ={i} reponse = {dataList[i]} par {idUser} du date {formatted_time} pour le village {village.NomAdministratifVillage}")

                u=users.objects.get(id=idUser) 
                q=Question.objects.get(id=i)       
                obj=Reponse.objects.create(question_id=q,response_date=formatted_time,text_reponse=dataList[i],village=village,id_user=u)

        return Response('200 OK')  # Réponse OK
    else:
        return Response('405 Method Not Allowed', status=405) 


@api_view(['Post'])
def suprimercommin(request):
    id=request.data.get('id')
    try:
        obg=Commune.objects.get(ID_commune=id).delete()
        return Response('200')

    except:
        return Response('400')

@api_view(['Post'])
def suprimervillage(request):
    id=request.data.get('id')
    try:
        obg=Village.objects.get(NumeroVillage=id).delete()
        return Response('200')

    except:
        return Response('400')
    
@api_view(['Post'])
def suprimermoghataa(request):
    id=request.data.get('id')
    try:
        obg=Moughata.objects.get(ID_maghataa=id).delete()
        return Response('200')

    except:
        return Response('400')
    # idvillage = request.data.get('village')
    # idform = request.data.get('form')
    # if idvillage== "Choisissez le village" or idform=="Choisissez le formilaire" :
    #     return Response({"message":"choisissez le formilaire et le village "})
@api_view(['POST'])
def formInfo(request):
    idvillage = request.data.get('village')
    idform = request.data.get('form')
    if idvillage== "Choisissez le village" or idform=="Choisissez le formilaire" :
        return Response({"message":"choisissez le formilaire et le village "})
    data = []
    listdata = []

    formulaire = Formilair.objects.get(id=idform)
    # questios = Question.objects.get(formilair=formulaire)
    village = Village.objects.get(NumeroVillage=idvillage)
    reponsesDates = Reponse.objects.filter(village=village).order_by('-response_date').values('response_date').distinct()
    # print(reponsesDates)
 
    for date in reponsesDates:
        reponsesList=[]
        questionsList = []
        reponses = Reponse.objects.filter(village=village,response_date=date['response_date'])
        try:
            for reponse in reponses:
                if reponse.question_id.formilair==formulaire:
                    form_data={"question":reponse.question_id.text, "reponse":reponse.text_reponse,'date': reponse.response_date}
                    reponsesList.append(form_data)
        except:
            print("errur")
        if len(reponsesList):
            questions_data={ "Date":date['response_date'].strftime("%Y-%m-%d %H:%M:%S"),"user":reponse.id_user.fullname(),"data":reponsesList}
            listdata.append(questions_data)
    form_data={ "formilaire":formulaire.titre,'questions': listdata}
    data.append(form_data)
    return Response(data)


 


@api_view(['GET'])
def list_commune(request):
    data=[]
    obj = Commune.objects.all().order_by('Nom_commune')
    moughataa = Moughata.objects.all()
    if not obj  :
        return Response("no data")
    for commin in obj:
        for mogh in moughataa:
            if commin.ID_maghataa_id_id == mogh.ID_maghataa:
                form_data={ "ID_commin":commin.ID_commune,'nom':commin.Nom_commune,'ID_maghataa':mogh.ID_maghataa,'moughataa':mogh.Nom_maghataa}
                data.append(form_data)
    return Response(data)
from django.db.models import Count

@api_view(['GET'])
def list_Village(request):
    data=[]
    obj = Village.objects.all()
    commin = Commune.objects.all()
    if not obj  :
        return Response("no data")
    for village in obj:
        for comm in commin:
            if village.idCommit_id == comm.ID_commune:
                form_data={ "idvillage":village.NumeroVillage,"DistanceAxesPrincipaux":village.DistanceAxesPrincipaux,'idCommin':comm.ID_commune,'nomAdministratif':village.NomAdministratifVillage,'NomLocal':village.NomLocal,'DistanceChefLieu':village.DistanceChefLieu,'DateCreation':village.DateCreation,'commin':comm.Nom_commune}
                data.append(form_data)
    return Response(data)

@api_view(['GET'])
def list_Maghataa(request):
    data=[]
    obj = Moughata.objects.all().order_by('Nom_maghataa')
    wilayes = Wilaya.objects.all()
    if not obj  :
        return Response("no data")
    for mouhgataa in obj:
        for wilaya in wilayes:
            if mouhgataa.ID_wilaya_id == wilaya.ID_wilaya:
                form_data={ "ID_maghataa":mouhgataa.ID_maghataa,'nom':mouhgataa.Nom_maghataa,'wilaye':wilaya.Nom_wilaya,'codeWilaye':wilaya.ID_wilaya}
                data.append(form_data)
    return Response(data)
    

    for formilair in formilairs:
        form_data = { 'id':formilair.id,'formilair': formilair.titre, 'description': formilair.description}
        forms_data.append(form_data)

@api_view(['GET'])
def list_demo(request):
    obj = Demographie.objects.all()
    if not obj  :
        return Response("no data")
    serializer = DemographieSerializer(obj, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def list_questions(request):
    obj = Question.objects.all()
    if not obj  :
        return Response("no data")
    serializer = QuestionSerializer(obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_coordonnesgps(request):
    obj = CoordonneesGPS.objects.all()
    if not obj  :
        return Response("no data")
    serializer = CoordonneesGPSSerializer(obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_EstimationRessources(request):
    obj = EstimationRessources.objects.all()
    if not obj  :
        return Response("no data")
    serializer = EstimationRessourcesSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_InfrastructuresVillage(request):
    obj = InfrastructuresVillage.objects.all()
    if not obj  :
        return Response("no data")
    serializer = InfrastructuresVillageSerializer(obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_ActivitesEconomiques(request):
    obj = ActivitesEconomiques.objects.all()
    if not obj  :
        return Response("no data")
    serializer = ActivitesEconomiquesSerializer(obj, many=True)
    return Response(serializer.data)

@api_view(['POST'])

def auth(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Method Not Allowed"}, status=405)

    email = request.data.get('email')
    password = request.data.get('password')
    print(email,password)
    
    if email is None or password is None:
        return JsonResponse({"message": "Email or password is missing"}, status=400)

    try:
        user = users.objects.get(email=email)
    except user.DoesNotExist:
        return JsonResponse({"message": "User Not Found"}, status=404)

    if   user.password !=password:
        return JsonResponse({"message": "Incorrect Password"}, status=401)

    if not user.active or user.role != "admin":
        return JsonResponse({"message": "Unauthorized Access"}, status=403)

    # Serialize user data before returning
    user.password=""
    serializer = UserSerializer(user)
    return JsonResponse({"message": "Successful", "user": serializer.data})
@api_view(['POST'])
def list_Maghataa_parwilaya(request):
    id_w=request.data.get("id")
    # id_w=1
    
    Mogh = Moughata.objects.filter(ID_wilaya=id_w)
    willaye=Wilaya.objects.get(ID_wilaya=id_w)

    l={}
    l['willaye']=willaye.Nom_wilaya
    l['moughata']=list(Mogh.values())
    # l['moghataa']=list(Mogh.values())
    if not Mogh  :
        return Response("no data")
    return Response(l)


@api_view(['POST'])
def list_commun_parMough(request):
    id_w=request.data.get("id")
    Mogh = Moughata.objects.get(ID_maghataa=id_w)
    communs=Commune.objects.filter(ID_maghataa_id=id_w)

    l={}
    l['Moughata']=Mogh.Nom_maghataa
    l['communs']=list(communs.values())
    if not Mogh or not communs  :
        return Response("no data")
    return Response(l)

@api_view(['POST'])
def inserer_donnees(request):
    if request.method == 'POST':
        data = request.data
        village_id = data.get('village')
        questions = data.get('dataList', [])
        gmt = pytz.timezone('GMT')
        gmt_time = datetime.now(gmt)
        infrastructures = data.get('infrastructures', [])
        try:
            village = Village.objects.get(NumeroVillage=village_id)
            if infrastructures:
                for i in infrastructures:
                    try:
                        # Convertir les valeurs en entiers
                        typeInfra = int(i['typeInfra'])
                        fonctionnelles = int(i['fonctionnelles'])
                        nonFonctionnelles = int(i['nonFonctionnelles'])
                        total = int(i['total'])

                        print("Creating infrastructure with:")
                        print(f"Village: {village}")
                        print(f"TypeInfrastructure: {typeInfra}")
                        print(f"NombreFonctionnelles: {fonctionnelles}")
                        print(f"NombreNonFonctionnelles: {nonFonctionnelles}")
                        print(f"NombreTotal: {total}")
                        print(f"Date: {gmt_time}")

                        # Créer ou mettre à jour l'infrastructure
                        InfrastructuresVillage.objects.create(NumeroVillage=village,TypeInfrastructure=i['typeInfra'],NombreNonFonctionnelles=i['nonFonctionnelles'],NombreFonctionnelles=i['fonctionnelles'],NombreTotal=i['total'],date_info=gmt_time)

                    except ValueError as e:
                        return JsonResponse({'message': f'Erreur de conversion: {str(e)}'}, status=400)

            for question in questions:
                question_id = question.get('id')
                value = question.get('value')
                try:
                    q = Question.objects.get(id=question_id)
                    u = users.objects.first()  # Remplacez ceci par la récupération de l'utilisateur approprié
                    nouvelle_reponse = Reponse.objects.create(
                        question_id=q,
                        response_date=gmt_time,
                        text_reponse=value,
                        village=village,
                        id_user=u
                    )
                    nouvelle_reponse.save()
                except ObjectDoesNotExist as e:
                    return JsonResponse({'message': f"La question avec l'ID {question_id} n'existe pas"}, status=400)

            return JsonResponse({'message': 'Données insérées avec succès'}, status=200)
        except Village.DoesNotExist:
            return JsonResponse({'message': 'Le village spécifié n\'existe pas'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Méthode non autorisée'}, status=405)


# @api_view(['POST'])
# def create_user(request):
#     """
#     Create a new user.
#     """
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)
# # @api_view(['POST'])
