from sys import stdin
from collections import OrderedDict
import random
def busqueda_binaria(lista,elemento):
	low,hi = 0,len(lista)
	while low+1!=hi:
		mid = low + ((hi-low)>>1)
		if(lista[mid]>elemento):
			hi = mid
		else:
			low = mid

	return low

def main():

	N = int(input())
	heights = list(OrderedDict.fromkeys(map(int, stdin.readline().split())))
	#OrderedDict consultado en stackoverflow para eliminar repetidos
	N_lucho = int(input())
	lucho_measure = list(map(int, stdin.readline().split()))
	
	for i in range(N_lucho):
		res = ''
		m = busqueda_binaria(heights,lucho_measure[i])
		if(lucho_measure[i]==heights[m]):
			if(m-1>=0 and heights[m-1]<lucho_measure[i]):
				res +=str(heights[m-1])
			else:
				res+='X'

			res+=' '

			if(m+1<len(heights) and heights[m+1]>lucho_measure[i]):
				res += str(heights[m+1])
			else:
				res+='X'


		else:
			if(heights[m]<lucho_measure[i]):
				res +=str(heights[m])
			else:
				res+='X'
			res+=' '
			if(heights[m]>lucho_measure[i]):
				res += str(heights[m])
 
			elif(m+1<len(heights) and heights[m+1]>lucho_measure[i]):
				res+=str(heights[m+1])
			else:
				res+='X'
		print(res)
		res= ''

main()
