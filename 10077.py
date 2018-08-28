import sys
sys.setrecursionlimit(1000000)
from sys import stdin

def buscar(izq_a,izq_b,der_a,der_b,m,n):
    result =""
    if( izq_a + der_a == m and izq_b + der_b == n):
        return ""
    if((izq_a + der_a)*n > (izq_b + der_b)*m):
        
        return "L"+buscar(izq_a,izq_b,izq_a + der_a, izq_b + der_b,m,n);

    else:
        
        return "R"+buscar(izq_a + der_a, izq_b + der_b ,der_a,der_b,m,n)
    

def main():
   
    target = [int(x) for x in stdin.readline().strip().split()]
    while target[0]!=1 or target[1]!=1:
        print( buscar(0,1,1,0,target[0],target[1]))
        target = [int(x) for x in stdin.readline().strip().split()]

main()
