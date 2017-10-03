def mapper(tab):
    print(tab)
    #liste Mapper()
    liste = []

    a = 0
    b = 0

    for i in tab:
        #Parcours ligne par ligne
        for j in i:
            #Parcours colonne par colonne

            #Inscrit valeur et coordonnées dans la liste Mapper()
            j = '{0},{1},{2}'.format(j, a, b)
            liste.append(j)
            b = b + 1

        a = a + 1
        b = 0

    #On renvoie la liste Mapper()
    return (liste)


def reducer(obj):
    #Split l'objet recu, composé d'une valeur et de ses coordonnées
    split = obj.split(',')
    a = split[0]
    x = split[1]
    y = split[2]

    #Retourne valeur, nouveau x, et nouveau y
    return (a, y, x)
