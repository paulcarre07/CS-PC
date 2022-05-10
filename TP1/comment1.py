import os,sys

"""
Entrée : none
Sortie : int i
But : Le programme principal va créer un fils qui print i tant que i=<N
"""
N=10
i =1
while os.fork()==0 and i<=N: #Création du fils
    i+=1
    print(i)
sys.exit(0)

