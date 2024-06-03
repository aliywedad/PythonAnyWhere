from django.urls import path
from . import views
from . import mobile



urlpatterns = [
    path('', views.list_users, name='list_users'),
    path('auth/', views.auth, name='auth'),  
    path('list_users/', views.list_users, name='list_users'),  
    path('list_wilaya/', views.list_wilaya, name='list_wilaya'),  
    path('list_Infrastructur/', views.list_Infrastructur, name='list_Infrastructur'),  
    path('list_TypeInfrastructur/', views.list_TypeInfrastructur, name='list_TypeInfrastructur'),  
    path('suprimerWilaya/', views.suprimerWilaya, name='suprimerWilaya'),  
    path('suprimerUtilisateur/', views.suprimerUtilisateur, name='suprimerUtilisateur'),  
    path('modifierEtat/', views.modifierEtat, name='modifierEtat'),  
    path('AddUser/', views.AddUser, name='AddUser'),  
    path('suprimercommin/', views.suprimercommin, name='suprimercommin'),  
    path('suprimermoghataa/', views.suprimermoghataa, name='suprimermoghataa'),  
    path('suprimervillage/', views.suprimervillage, name='suprimervillage'),  
    path('list_commune/', views.list_commune, name='list_commune'),  
    path('list_Village/', views.list_Village, name='list_Village'),  
    path('list_Maghataa/', views.list_Maghataa, name='list_Maghataa'),  
    path('list_demo/', views.list_demo, name='list_demo'),  
    path('list_coordonnesgps/', views.list_coordonnesgps, name='list_coordonnesgps'),  
    path('list_EstimationRessources/', views.list_EstimationRessources, name='list_EstimationRessources'),  
    path('list_InfrastructuresVillage/', views.list_InfrastructuresVillage, name='list_InfrastructuresVillage'), 
    path('list_ActivitesEconomiques/', views.list_ActivitesEconomiques, name='list_ActivitesEconomiques'),   
    path('list_Maghataa_parwilaya/', views.list_Maghataa_parwilaya, name='list_Maghataa_parwilaya'),   
    path('list_commun_parMough/', views.list_commun_parMough, name='list_commun_parMough'), 
    path('Repondre/', views.Repondre, name='Repondre'), 
    path('inserer_donnees/', views.inserer_donnees, name='inserer_donnees'), 
    path('list_questions/', views.list_questions, name='list_questions'), 
        

    path('forms/', views.forms, name='forms'),   
    path('delet_forms/', views.delet_forms, name='delet_forms'),   
    path('Getforms/', views.Getforms, name='Getforms'),   
    path('create_formilair/', views.create_formilair, name='create_formilair'),   
    path('delQuetion/', views.delQuetion, name='delQuetion'),   
    path('AddWilaye/', views.AddWilaye, name='AddWilaye'),   
    path('modifierWilaye/', views.modifierWilaye, name='modifierWilaye'),   
    path('modifierCommin/', views.modifierCommin, name='modifierCommin'),   
    path('modifierMoughataa/', views.modifierMoughataa, name='modifierMoughataa'),   
    path('modifierVillage/', views.modifierVillage, name='modifierVillage'),   
    path('formInfo/', views.formInfo, name='formInfo'),   
    path('AddMoughataa/', views.AddMoughataa, name='AddMoughataa'),   
    path('AddCommin/', views.AddCommin, name='AddCommin'),   
    path('AddVillage/', views.AddVillage, name='AddVillage'),   
    path('predict/', views.predict, name='predict'), 







    # *************************************************** ( mobile )***********************************************************
    path('Connexion/',mobile.Connexion, name='Connexion'), 
    path('village_info/',mobile.village_info, name='village_info'), 
    path('TypeInfra/',mobile.TypeInfra, name='TypeInfra'), 
    path('InfraVillage/',mobile.villageInfra_info, name='InfraVillage'), 
    path('Upload_Reponses/',mobile.Upload_Reponses, name='Upload_Reponses'), 

]





