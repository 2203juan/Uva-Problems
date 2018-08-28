from sys import stdin

visited= [[None for _ in range(100)] for _ in range(100)];
pares = None
impares = None

def solve(R,C,M,N):
	global visited,pares, impares
	node = (0,0)
	stack = [node]

	visited[0][0]= 2
	aux = []
	cont =0


	while len(stack)!=0:
		cont=0
		i,j = stack.pop()


		aux.append((i+M,j+N))#1
		aux.append((i-M,j+N))#2
		aux.append((i+M,j-N))#3
		aux.append((i-M,j-N))#4
		if(M!=N):
			aux.append((i+N,j+M))#5
			aux.append((i+N,j-M))#6
			aux.append((i-N,j+M))#7
			aux.append((i-N,j-M))#8
		if(M==0 or N==0):
			aux.clear()
			aux.append((i+M,j+N))
			aux.append((i-M,j-N))
			aux.append((i+N,j+M))
			aux.append((i-N,j-M))



		
		for (x,y) in aux:
			if x<R and y<C and x>=0 and y>=0 :
				if visited[x][y]==0:
					stack.append((x,y))
					visited[x][y]=2
				if(visited[x][y]!=1):
					cont+=1
		aux.clear()
		if(cont%2 == 0):
			pares+=1
		else:
			impares+=1


	  

def main():
	global visited,pares, impares
	tcnt = int(stdin.readline())
	case=0
	c,d = 0,0
	while tcnt >0:
		R,C,M,N = map(int, stdin.readline().split())
		pares = 0; impares = 0
		charcos = int(stdin.readline())
		for i in range(R):
				for j in range(C):
					visited[i][j] = 0

		while(charcos >0):
			c,d = map(int,stdin.readline().split())
			charcos-=1
			visited[c][d]=1 
		solve(R,C,M,N)
		tcnt -= 1
		case+=1
		print('Case {0}: {1} {2}'.format(case,pares,impares))

main()