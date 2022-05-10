import os,sys
"""
Entrée : None
Sortie : string "OK !" et "Bonjour !"
But : Boucle qui se répete 4 fois, à la première boucle on créait un fils, on a donc un père et un fils donc un "ok" et deux "bonjour" 
puis à la deuxiéme boucle le père créait un fils et le fils un deuxième fils 
donc on a un un père deux fils et un père/fils et ainsi de suite... 
NB: le fils dit juste Bonjour et le père Ok et Bonjour.
"""


for i in range(4):
    pid =os.fork() #création fils
    if pid != 0: #si c'est un père
        print("OK !") 
    print("Bonjour !")
sys.exit(0)