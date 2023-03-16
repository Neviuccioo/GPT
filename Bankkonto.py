# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:46:26 2023

@author: nevio
"""
"""
Entwickeln Sie eine Klasse BankAccount in objektorientierter Weise mit folgender Spezifikation: 
Ein Bankkonto dient der Geldverwaltung und wird durch eine Kennung 
(Ziffern und/oder Buchstaben, z.B. IBAN) eindeutig bestimmt. 
Das Konto kann eröffnet oder aufgelöst werden. Geld kann eingezahlt oder abgehoben werden. 
Der aktuelle Kontostand kann jederzeit abgefragt werden. 
Der Betrag wird in einer kontospezifischen Währung ausgedrückt, standardmäßig in Schweizer Franken (Fr, rp). 
Der Kontostand kann weder unter Null noch über 100'000.- in der jeweiligen Währung liegen.
- Verwenden Sie Attribute für Daten: Überlege dir, welche Daten ein solches Bankkonto 
braucht und deklariere einige Klassenvariablen (Attribute) dafür.
- Verwenden Sie einen Konstruktor, um das Objekt zu initialisieren: Das Bankkonto 
beginnt mit 0.- Fr und dem obligatorischen Identifikator.
- Verwenden Sie Methoden für Aktionen: Überlegen Sie sich, wie sich das Bankkonto 
verhalten soll (welche Aktion ausgeführt werden kann). Methoden sind ähnlich wie Funktionen, 
nur dass sie in einem Klassenbereich deklariert werden.
Testen Sie Ihre Klasse mit einem nicht-interaktiven Testskript, das das 
Bankkonto-Objekt initialisiert, etwas Geld einzahlt, den Kontostand anzeigt, 
usw. Das Hauptskript sollte bewacht werden (wenn __name__ == "__main__"), 
um das Skript für die Verwendung im Modul vorzubereiten. Reichen Sie die Datei als bankaccount.py ein.
Hinweis: Diese Klasse wird später erweitert werden. Achten Sie darauf, "Spaghetti-Code" zu vermeiden.

Übersetzt mit www.DeepL.com/Translator (kostenlose Version)
"""
# Bankaccount erstellt


class BankAccount:

    def __init__(self, name, iban, guthaben):
        self.name = name
        self.iban = iban
        self.guthaben = 0

    def einzahlung(self, betrag):

        if self.guthaben + betrag > 100000:
            print("Sie können nur 100'000.- auf dem Konto haben")
        else:
            self.guthaben += betrag

    def auszahlen(self, betrag):

      if self.guthaben - betrag >= 0:
          self.guthaben -= betrag
      else:
          print("Sie haben zu wenig Geld auf dem Konto")

    def anzeigen(self):
        print(f"Kontoinhaber: {self.name}, IBAN: {self.iban}, Guthaben: {self.guthaben}")

if __name__ == "__main__":
    pass   