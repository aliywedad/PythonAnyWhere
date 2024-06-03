# backend
pip install mysqlclient 
pip install mysql-connector-python



<!-- way for listing moghataa by wilaya :
    json_dict = {}
    w=Wilaya.objects.all()
    for i in w:
        m=Maghataa.objects.filter(ID_wilaya=i.ID_wilaya).values()
        json_dict[i.Nom_wilaya] = {(m)}
    # users_data=list(user.values())
    # return JsonResponse(json_dict,safe=False)
    # return Response(json_dict) -->


from django.http import JsonResponse
        obj = table.objects.all()
    users_data=list(obj.values())
    return JsonResponse(users_data, safe=False)


ob=Formilair.objects.all()
Q=Question.objects.all()
R=Reponse.objects.all()
print("\n \n \n \n\n\n \n ")
for i in ob:
    print ("le formilair ",i.titre)
    Qs=Question.objects.filter(formilair_id=i.id)
    for Q in Qs:
        R=Reponse.objects.filter(question_id=Q.id)
        print(" le Question : ",Q.text)
        for rep in R:
            print("les reponse : ",rep.text_reponse)

    print("\n \n \n \n ")







