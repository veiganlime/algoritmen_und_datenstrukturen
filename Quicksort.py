def quck_sort(unsortierte_liste, liste_links, liste_rechts):
    if liste_links < liste_rechts:
        pivotIndex = partitionierung (unsortierte_liste, liste_links, liste_rechts)
        qucksort(unsortierte_liste, liste_links, pivotIndex-1)
        qucksort(unsortierte_liste, pivotIndex+1, liste_rechts)

def partitionierung(unsortierte_liste, liste_links, liste_rechts):
    i = liste_links
    j = liste_rechts
    pivot = unsortierte_liste[liste_rechts]
    while i < j:
        while i < liste_rechts and unsortierte_liste[i] < pivot:
            i += 1
        while j > liste_links and unsortierte_liste[j] >= pivot:
            j -= 1
        if i < j:
            unsortierte_liste[i], unsortierte_liste[j] = unsortierte_liste[j], unsortierte_liste[i]
    if unsortierte_liste[i] > pivot:
        unsortierte_liste[i], unsortierte_liste[liste_rechts] = unsortierte_liste[liste_rechts], unsortierte_liste[i]

    return i


    return unsortierte_liste