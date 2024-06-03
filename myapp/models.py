from django.db import models
# Create your models here.
class users(models.Model): 
    tel = models.IntegerField()  
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100) 
    nom = models.CharField(max_length=100) 
    prenom = models.CharField(max_length=100) 
    role = models.CharField(max_length=100) 
    active=models.BooleanField()
    def fullname(self):
        return self.nom +" "+self.prenom

    class Meta:
        db_table = 'users'


class Wilaya(models.Model):
    ID_wilaya = models.IntegerField(primary_key=True)
    Nom_wilaya = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.Nom_wilaya
    class Meta:
        db_table = 'Wilaya'

class Moughata(models.Model):
    ID_maghataa = models.IntegerField(primary_key=True)
    Nom_maghataa = models.CharField(max_length=100)
    ID_wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, db_column='ID_wilaya')

    def __str__(self):
        return self.Nom_maghataa
    class Meta:
        db_table = 'moughata'



class Commune(models.Model):
    ID_commune = models.IntegerField(primary_key=True)
    Nom_commune = models.CharField(max_length=100)
    ID_maghataa_id = models.ForeignKey(Moughata, on_delete=models.CASCADE,db_column='ID_maghataa_id')

    def __str__(self):
        return self.Nom_commune

    class Meta:
        db_table = 'commune'





class Village(models.Model):
    NumeroVillage = models.IntegerField(primary_key=True)
    idCommit = models.ForeignKey(Commune, on_delete=models.CASCADE, db_column='idCommit', max_length=100)
    NomAdministratifVillage = models.CharField(max_length=150)
    NomLocal = models.CharField(max_length=150)
    DistanceChefLieu = models.FloatField()
    DistanceAxesPrincipaux = models.FloatField()
    DateCreation = models.DateField()
    CompositionEthnique = models.TextField()
    AutresInfosVillage = models.TextField()

    class Meta:
        db_table = 'village'


    def __str__(self):
        return self.NomAdministratifVillage

class Demographie(models.Model):
    ID_Demographie = models.IntegerField(primary_key=True)
    NumeroVillage = models.ForeignKey(Village, on_delete=models.CASCADE, db_column='NumeroVillage')
    PopulationFixe = models.IntegerField()
    NombreMenages = models.IntegerField()
    AutresInfosDemographie = models.TextField()

    class Meta:
        db_table = 'demographie'

    def __str__(self):
        return str(self.ID_Demographie)

class ActivitesEconomiques(models.Model):
    ID_ActiviteEco = models.IntegerField(primary_key=True)
    NumeroVillage = models.ForeignKey(Village, on_delete=models.CASCADE, db_column='NumeroVillage')
    TypeActivite = models.CharField(max_length=150)
    AutresDetailsActivite = models.TextField()

    class Meta:
        db_table = 'activiteseconomiques'

    def __str__(self):
        return self.TypeActivite

class CoordonneesGPS(models.Model):
    ID_CoordonneesGPS = models.IntegerField(primary_key=True)
    NumeroVillage = models.ForeignKey(Village, on_delete=models.CASCADE, db_column='NumeroVillage')
    Longitude = models.FloatField()
    Latitude = models.FloatField()
    TypeLocalite = models.CharField(max_length=150)
    StructureHabitat = models.CharField(max_length=150)
    ObservationsAccesLocalite = models.TextField()

    class Meta:
        db_table = 'coordonneesgps'

    def __str__(self):
        return f"Coordonnées GPS pour le village {self.NumeroVillage}"

class EstimationRessources(models.Model):
    ID_EstimationRessources = models.IntegerField(primary_key=True)
    NumeroVillage = models.ForeignKey(Village, on_delete=models.CASCADE, db_column='NumeroVillage')
    NombreFamillesEstime = models.IntegerField()
    PopulationEstimee = models.IntegerField()
    EstimationBetail = models.IntegerField()
    AnneeEstimation = models.IntegerField()

    class Meta:
        db_table = 'estimationressources'

    def __str__(self):
        return f"Estimation des ressources pour le village {self.NumeroVillage}"


        
class Formilair(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = 'Formilair'

class Question(models.Model):
    TEXT_RESPONSE = 'text'
    CHOICE_RESPONSE = 'choice'
    COMPOSITE_RESPONSE = 'composite'
    CHECKBOX_RESPONSE = 'checkbox'
    RADIO_RESPONSE = 'radio'
    RESPONSE_TYPES = [
        (TEXT_RESPONSE, 'Text'),
        (CHOICE_RESPONSE, 'Choice'),
        (COMPOSITE_RESPONSE, 'Composite'),
        (CHECKBOX_RESPONSE, 'Checkbox'),
        (RADIO_RESPONSE, 'Radio'),
    ]
    
    text = models.TextField()
    choices = models.TextField()  # Store choices as JSON or CSV
    categorie = models.TextField()  # Store choices as JSON or CSV
    type = models.CharField(max_length=10, choices=RESPONSE_TYPES)
    formilair = models.ForeignKey(Formilair, on_delete=models.CASCADE, related_name='formilair')
    # parent_question = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_questions', null=True, blank=True)

    class Meta:
        db_table = 'Question'


class TypeInfrastructure(models.Model) :
    nom = models.TextField()
    class Meta:
        db_table = 'Typeinfrastructur'
class Infrastructur(models.Model) :
    id = models.IntegerField(primary_key=True)
    nom = models.TextField()
    description = models.TextField()
    type = models.ForeignKey(TypeInfrastructure, on_delete=models.CASCADE, related_name='infrastructures', db_column='type')

    class Meta:
        db_table = 'Infrastructur'


class Question_backup(models.Model):
    TEXT_RESPONSE = 'text'
    CHOICE_RESPONSE = 'choice'
    COMPOSITE_RESPONSE = 'composite'
    CHECKBOX_RESPONSE = 'checkbox'
    RADIO_RESPONSE = 'radio'
    RESPONSE_TYPES = [
        (TEXT_RESPONSE, 'Text'),
        (CHOICE_RESPONSE, 'Choice'),
        (COMPOSITE_RESPONSE, 'Composite'),
        (CHECKBOX_RESPONSE, 'Checkbox'),
        (RADIO_RESPONSE, 'Radio'),
    ]
    
    text = models.TextField()
    choices = models.TextField()  # Store choices as JSON or CSV
    sub_categorie = models.TextField()  # Store choices as JSON or CSV
    categorie = models.TextField()  # Store choices as JSON or CSV
    parent = models.TextField()  # Store choices as JSON or CSV
    type = models.CharField(max_length=10, choices=RESPONSE_TYPES)
    # parent_question = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_questions', null=True, blank=True)
    class Meta:
        db_table = 'question-backup'

class Reponse(models.Model):
    text_reponse = models.TextField()
    response_date = models.DateTimeField()
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_id',db_column='question_id')
    village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='village',db_column='village')
    id_user = models.ForeignKey(users, on_delete=models.CASCADE, related_name='id_user',db_column='id_user')
    class Meta:
        db_table = 'Reponse'


class InfrastructuresVillage(models.Model):
    ID_Infrastructures = models.IntegerField(primary_key=True)
    NumeroVillage = models.ForeignKey(Village, on_delete=models.CASCADE, db_column='NumeroVillage')
    # TypeInfrastructure = models.CharField(max_length=150)
    TypeInfrastructure = models.ForeignKey(Infrastructur, on_delete=models.CASCADE, related_name='Infrastructur',db_column='TypeInfrastructure')
    user = models.ForeignKey(users, on_delete=models.CASCADE, related_name='user',db_column='user')
    NombreTotal = models.IntegerField()
    NombreFonctionnelles = models.IntegerField()
    NombreNonFonctionnelles = models.IntegerField()
    date_info = models.DateTimeField()

    class Meta:
        db_table = 'infrastructuresvillage'

    def __str__(self):
        return self.infrastructuresvillage





