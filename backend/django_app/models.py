from django.db import models
import pandas as pd

# Create your models here.
class BD:

    def __init__(self,file:str) -> None:
        self.df =  pd.read_csv(file)
        self.name = file[:-4]
    def calcul(self,choix:str,quantite:float)->float:
        for i in range(len(self.df)-1):
            if self.df.iloc[i].iloc[0].lower() == choix.lower():
                return self.df.iloc[i].iloc[1]*quantite
        raise ValueError("transport non valide")
    def list_value(self)->list[str]:
        return list(self.df.iloc[:,0])
    def recherche(self,choix:str) -> list[str]:
        return [i for i in self.list_value() if choix.lower() in i.lower()]