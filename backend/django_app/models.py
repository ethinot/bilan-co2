from django.db import models
import pandas as pd
import unicodedata
# Create your models here.
def pre_traitement(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return str(only_ascii).lower().replace(" ","")


class BD:

    def __init__(self,file:str) -> None:
        self.df =  pd.read_csv(file)
        self.name = file[:-4]
    def calcul(self,choix:str,quantite:float)->float:
        for i in range(len(self.df)-1):
            if  pre_traitement(self.df.iloc[i].iloc[0])== pre_traitement(choix):
                return self.df.iloc[i].iloc[1]*quantite
        raise ValueError("{self.name} non valide")
    def list_value(self)->list[str]:
        return list(self.df.iloc[:,0])
    def recherche(self,choix:str) -> list[str]:
        return [i for i in self.list_value() if choix.lower() in i.lower()]
    
class Alimentation(BD):
    filtre = []
    def list_value(self)->list[str]:
        return list(self.df.iloc[:,2])
    def list_categorie(self) -> list[str]:
        return list(set(self.df.iloc[:,0]))
    def select_categorie(self,categorie : str) -> list[str]:
        l = [self.df.iloc[i,:] for i in range(len(self.df)) if pre_traitement(self.df.iloc[i,0])==pre_traitement(categorie)]
        if l == []:
            raise ValueError("categorie non valide")
        else:
            self.filtre = pd.DataFrame(l)
        return list(set(self.filtre.iloc[:,1]))
    def select_sous_categorie(self,categorie: str)->list[str]:
        l = [self.filtre.iloc[i,:] for i in range(len(self.filtre)) if pre_traitement(self.filtre.iloc[i,1])==pre_traitement(categorie)]
        if l == []:
            raise ValueError("sous categorie non valide")
        else:
            self.filtre = pd.DataFrame(l)
        return list(self.filtre.iloc[:,2])
    def calcul(self,choix:str,quantite:float)->float:
        for i in range(len(self.filtre)-1):
            if pre_traitement(self.filtre.iloc[i].iloc[2]) == pre_traitement(choix):

                return self.filtre.iloc[i].iloc[3]*quantite