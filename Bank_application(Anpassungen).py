# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:15:06 2023

@author: nevio
"""

import Bankkonto
import SubAccounts
import random
import sys
import time
import itertools


class Menu():
    def __init__(self):
        self.kunden = {}
        self.testkonten_anlegen()
        self.bank_menu()

            
    def bank_menu(self):
        print("1 = Konto anlegen")
        print("2 = Guthaben anzeigen")
        print("3 = Guthaben einzahlen")
        print("4 = Guthaben auszahlen")
        print("5 = sleep")
        print("6 = Steuerausweis")
        print("7 = Beenden")
    
    def choose_kunde(self):
        user_login = input("Geben Sie Ihren Namen ein: ")
        if user_login not in self.kunden:
            print("***************************")
            print("Kunde nicht vorhanden!!!!!!")
            print("***************************")
            return False
        return self.kunden[user_login]

    def choose_konto(self):
        z = int(input("Welches Konto möchten Sie anlegen? 1 - SavingAccount, 2 - YouthAccount, 3 - BankAccount: "))
        if z == 1:
            return SubAccounts.SavingAccount
        elif z == 2:
            jahre = int(input("Wie alt sind Sie? "))
            if SubAccounts.YouthAccount(None, None, None).bestimmung(jahre):
                return SubAccounts.YouthAccount
        elif z == 3:
            return Bankkonto.BankAccount
        else: 
            print()
            print("Ungültige Eingabe!")
            print()
            return None
    
    def anlegen(self):
        konto_art = self.choose_konto()
        if konto_art is True:
            return
        kunde_name = input("Geben Sie Ihren Namen ein: ")
        kunde_iban = random.randint(10000, 99999)
        kunde = konto_art(kunde_name, kunde_iban, 0)
        self.kunden[kunde_name] = kunde
        
        

    
    def testkonten_anlegen(self):
        while True:
            self.bank_menu()
            try:
                user_input = int(input("Was möchten Sie tun? "))
            except:
                user_input = 7
                print("Fehler")
        
            if user_input == 1:
                self.anlegen()
                while True:
                    f = int(input("Möchten Sie ein weiteres Konto eröffnen? 1 = ja 2 = nein"))
                    if f == 1:
                        self.anlegen()
                    if f == 2:
                        break
                
                
            elif user_input == 2:
                kunde = self.choose_kunde()
                if kunde is not False:
                    kunde.anzeigen()
            elif user_input == 3:
                kunde = self.choose_kunde()
                if kunde is not False:
                    kunde.einzahlung(int(input("Geben Sie den gewünschten Betrag ein: ")))
            elif user_input == 4:
                kunde = self.choose_kunde()
                if kunde is not False:
                    kunde.auszahlen(int(input("Geben Sie den gewünschten Betrag ein: ")))
            elif user_input == 5:
                kunde = self.choose_kunde()
                t = int(input("Wie viele Monate?: "))
                print("Wartezeit wird in Sekunden simuliert")
                print("Wartezeit", t*10, "Sekunden")
                print("-----------------------------")
                time.sleep(t*10)
                print("Willkommen", t, "Monate später")
                if kunde is not False:
                    kunde.guthaben += (kunde.guthaben / 100 * kunde.zinssatz * t)
                    print(kunde.name, "Ihr Guthaben beträgt nun", kunde.guthaben)
            elif user_input == 6:
                kunde = self.choose_kunde()
                if kunde is not False:
                    kunde.generate()
            elif user_input == 7:
                sys.exit()
            else:
                self.bank_menu()

                
if __name__ == "__main__":
    m = Menu()
