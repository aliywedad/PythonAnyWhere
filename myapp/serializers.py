from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields ='__all__'
class ReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields ='__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields ='__all__'
class WilayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields ='__all__'

class InfrastructurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infrastructur
        fields ='__all__'

class TypeInfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeInfrastructure
        fields ='__all__'

class MaghataaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Moughata
        fields ='__all__'


class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields ='__all__'

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields ='__all__'


class DemographieSerializer(serializers.ModelSerializer):
    class Meta:
        model =Demographie

        fields ='__all__'


class CoordonneesGPSSerializer(serializers.ModelSerializer):
    class Meta:
        model =CoordonneesGPS

        fields ='__all__'


class EstimationRessourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model =EstimationRessources

        fields ='__all__'




class InfrastructuresVillageSerializer(serializers.ModelSerializer):
    class Meta:
        model =InfrastructuresVillage

        fields ='__all__'

class ActivitesEconomiquesSerializer(serializers.ModelSerializer):
    class Meta:
        model =ActivitesEconomiques

        fields ='__all__'        