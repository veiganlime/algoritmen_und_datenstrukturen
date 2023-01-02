import random
import time
from CountingSort import counting_sort

def main():
    l =[]
    for i in range (999):
        l.append(random.randint(0,99))
    print(l)
    start = time.time()
    l = counting_sort(l)
    print(l)
    end = time.time()



    for i in range (len(l)-1):# mit "len(l)-1" berücksichtigung, dass die for-Schleife nicht außerchalb des Arrays luafen wird
        assert l[i] <=l[i+1] ,'Array ist unsortiert'
    print(end-start)

if __name__ == "__main__":
    main()