import sys
sys.setrecursionlimit(1000000)

from sys import stdin

MAX   = 50010
l   = [ None for i in range(MAX) ]


def solve(low, hi):

    if( hi -low <= 1 ):
        return 0

    mid = low + ((hi-low)>>1)
    cont = solve(low, mid)
    cont += solve(mid, hi)

    temp = []

    i= low
    j =  mid

    while( i < mid and j<hi ):
        if( l[i] <= l[j]):
            temp.append(l[i])
            i+=1
        else:
            temp.append(l[j])
            j+=1
            cont += mid - i

    while i<mid:
        temp.append(l[i])
        i+=1

    while(j < hi ):
        temp.append(l[j])
        j+=1

    l[low:hi] = temp

    #print(cont)
    return cont



def main():
  global num
  inp = stdin
  n = int(stdin.readline().strip())
  while n>0:
    for i in range(n):
      l[i] = int(stdin.readline())
    print(solve(0, n))
    n = int(stdin.readline().strip())

main()
