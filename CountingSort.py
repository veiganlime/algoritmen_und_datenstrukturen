def counting_sort(unsortierte_liste):
    maxElemente = max(unsortierte_liste)
    count = maxElemente +1
    countArray = [0] * count

    for elemente in unsortierte_liste: # Elementen zählen, die in Liste vorkommen
        countArray[elemente] += 1

    for i in range(1, count):
        countArray[i] += countArray[i-1] # Teilsumme

    sortierte_liste = [0] * len(unsortierte_liste)
    i = len(unsortierte_liste) - 1
    while i >= 0:
        currentEl = unsortierte_liste[i]
        countArray[currentEl] -= 1
        neuePosotion = countArray[currentEl]
        sortierte_liste[neuePosotion] = currentEl
        i -= 1

    return sortierte_liste