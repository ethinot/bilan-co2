from django.db import models
import pandas as pd

# Create your models here.
class Transport:
    df = pd.read_csv('transport.csv')

    #calcul le cout en g de C02 pour une distance donné en km
    def calcul(self,transport:str,km:float)->float:
        for i in range(len(self.df)-1):
            if self.df.iloc[i].iloc[0].lower() == transport.lower():
                return self.df.iloc[i].iloc[1]*km
        raise ValueError("transport non valide")
    def transport_list(self)->list[str]:
        return list(self.df.iloc[:,0])