import numpy as np
from Functions import *

#Déclaration tableau initial
tab = np.array([[3, 4, 5, 6],[1, 2, 3, 4],[9, 8, 7, 10],[56, 21, 45, 32]])
#Déclaration tableau final
tabReduce = np.array([[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]])

#Appel à la fonction Mapper()
tabMap = mapper(tab)

#Inscrit la liste retournée par Mapper()
print(tabMap)

for i in tabMap:
    #Parcours de la liste retournée par le Mapper()
    #Appel à la fonction Reducer()
    #Retourne la valeur, ainsi que les coordonnées inversées
    (val,x,y) = reducer(i)
    #Cast les coordonnées en int pour pouvoir parcourir le tableau final
    x = int(x)
    y = int(y)
    #Inscrit la bonne valeur à la bonne place dans le tableau
    tabReduce[x][y] = val

#Résultat: tableau inversé
print(tabReduce)

