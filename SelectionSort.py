def selection_sort(unsortierte_liste):
    for index in range(len(unsortierte_liste)):# Durchlaufe Array
        minimum_index = index
        for i in range(minimum_index+1, len(unsortierte_liste)): #Durchlaufe unsortierten
            if unsortierte_liste[minimum_index] > unsortierte_liste[i]:# Fallls kleinstes gefunden, Merken
                minimum_index = i

        cache = unsortierte_liste[index] # Tausche von zwei Elementen aus
        unsortierte_liste[index] = unsortierte_liste[minimum_index]
        unsortierte_liste[minimum_index] = cache

    return unsortierte_liste