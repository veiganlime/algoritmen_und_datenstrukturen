def insertion_sort(unsortierte_liste):
    for index in range(1, len(unsortierte_liste)):# Durchlaufe Array
        elememt = unsortierte_liste[index] # einzufügender Wert merken
        i = index - 1 #Suche nach insertion point rueckwaerts
        while i >= 0:
            if elememt < unsortierte_liste[i]:
                unsortierte_liste[i+1] = unsortierte_liste[i]# Verschiebung nach rechts
                unsortierte_liste[i] = elememt #Verschiebung nach links
                i = i-1
            else:
                break



    return unsortierte_liste
