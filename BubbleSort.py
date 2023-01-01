import random
import time


def bubble_sort(unsortierte_list):
    for i in range(len(unsortierte_list)):
        for j in range(0, len(unsortierte_list)-1-i):
            if unsortierte_list[j] >unsortierte_list[j+1]:
                unsortierte_list[j],unsortierte_list[j+1] = unsortierte_list[j+1], unsortierte_list[j]
    return unsortierte_list

