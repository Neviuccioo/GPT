# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:19:17 2023

@author: nevio
"""

import sys
import time
import Bankkonto

class SavingAccount(Bankkonto.BankAccount):
    
    def __init__(self, name, iban, guthaben):
        super().__init__(name, iban, guthaben)
        self.zinssatz = 0.1
        self.gebühr = 0.02
        
    def auszahlen(self, betrag):
        gebühr = 0.02
        if self.guthaben - betrag <= 0:
            self.guthaben -= betrag + (betrag*gebühr)
            print("***************************************************")
            print("Sie zahlen 2% Gebühren da Ihr Konto ins Minus geht.")
            print("***************************************************")
        else:
            self.guthaben -= betrag
 

class YouthAccount(Bankkonto.BankAccount):
    
    def __init__(self, name, iban, guthaben):
        self.max_age = 25
        self.alter = None
        super().__init__(name, iban, guthaben)
        self.zinssatz = 2
        self.limit = 2000
        
    def auszahlen(self, betrag):
        if betrag > self.limit:
            print("*****************************************************")
            print("Sie können nicht mehr als 2000.- im Monat auszahlen.")
            print("*****************************************************")
        else:
            return super().auszahlen(betrag)
            
    def bestimmung(self, alter):
        if alter < self.max_age:
            self.alter = alter
            return True
        else:
            print("*****************************")
            print("Sie sind zu Alt für ein Konto")
            print("*****************************")
            sys.exit()  # Programm beenden

            return False
        
if __name__ == "__main__":
    pass
 
