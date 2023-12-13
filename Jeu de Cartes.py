#édition de classes

class Carte:
    def __init__(self,Name):
        self.__MP = -50
        self.__nom = Name
        self.__descrip = ("c'est une carte de sort")

    
    #def get
    def getMana(self):
        return self.__MP
    
    def getNom(self):
        return self.__nom
    
    def getdescription(self):
        return self.__descrip


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Mage:
    def __init__(self,Name,Main):
        self.__nom = Name
        self.__HP = 300
        self.__MP = 200
        self.__Action = Main
        self.__défausse
        self.__ZoneDeJeu


    #def get...

    def getNom(self):
        return self.__nom
    
    def getHealth(self):
        return self.__HP
    
    def getMana(self):
        return self.__MP
    
    def getAction(self):
        return self.__Action
    
    def getDéfausse(self):
        return self.__défausse
    def getZoneDeJeu(self):
        return self.__ZoneDeJeu
    


    #Actions

    def JoueUneCarte(self):
        print (Main = Carte)

    def RechargeMana(self,MP):
        print (MP + 10)

    def UtiliseUnCrystal(self):
        print (Main = Cristal)



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Cristal(Carte):
    def __init__(self,MP):
        self.__valeur = MP+10


    #def get

    def getValeur(self):
        return self.__valeur



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Créature(Carte):
    def __init__(self,HP):
        self.__HP = 500
        self.__HitScore = HP-50


    #def get

    def getHealth(self):
        self.__HP

    def getHitScore(self):
        self.__HitScore



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Blast(Carte):
    def __init__(self):
        self.__valeur = 150

    #def get

    def getValeur(self):
        return self.__valeur


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Jeu
Joueur = ""
choix = int(input("Carte(1), Cristal(2), Créature(3), Blast(4)"))
if(choix==1):
    Joueur = Carte("Lance Magie")

if(choix==2):
    Joueur = Cristal("Utilise Crystal")