def merge_sort(unsortierte_liste):
    if len(unsortierte_liste) > 1:
        liste_links = unsortierte_liste[:len(unsortierte_liste)//2]
        liste_rechts = unsortierte_liste[len(unsortierte_liste) // 2:]

        #recursion
        merge_sort(liste_links)
        merge_sort(liste_rechts)

        #merge von Teil-Array
        i = 0 # Index von Liste_Links
        j = 0 # Index von Liste_Rechts
        k = 0 # index von merged Array
        while i < len(liste_links) and j < len(liste_rechts):
            if liste_links[i] < liste_rechts[j]:
                unsortierte_liste[k] = liste_links[i]
                i += 1
            else:
                unsortierte_liste[k] = liste_rechts[j]
                j += 1
            k += 1
        while i < len(liste_links):
            unsortierte_liste[k] = liste_links[i]
            i += 1
            k += 1
        while j < len(liste_rechts):
            unsortierte_liste[k] = liste_rechts[j]
            j += 1
            k += 1



    return unsortierte_liste