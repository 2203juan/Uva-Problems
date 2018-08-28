from collections import deque
from sys import stdin
visited = None

def bfs(conf_inicial, target):
	global visited
	deltaM = [1,10,100,1000]
	deltam = [9,90,900,9000]
	result = -1
	queue = deque()
	nodo = conf_inicial
	queue.append((nodo,0))
	visited[conf_inicial] = 1	
	while queue:
		nodo,value = queue.popleft()
		if(nodo == target):
			result = value
			break

		for i in range(4):
			if(nodo//deltaM[i]%10!=9):
				tmp = nodo+deltaM[i]
				if(visited[tmp]==0):
					queue.append((tmp,value+1)); visited[tmp]=1
			else:
				tmp = nodo-deltam[i]
				if(visited[tmp]==0):
					queue.append((tmp,value+1)); visited[tmp]=1
			if(nodo//deltaM[i]%10!=0):
				tmp= nodo-deltaM[i]
				if(visited[tmp]==0):
					queue.append((tmp,value+1)); visited[tmp]=1
			else:
				tmp = nodo+deltam[i]
				if(visited[tmp]==0):
					queue.append((tmp,value+1)); visited[tmp]=1

	return result

def main():
	global visited
	tc = int(input())
	stdin.readline()
	while tc!=0:
		conf_inicial =  int(stdin.readline().replace(" ", ""))
		target = int(stdin.readline().replace(" ", ""))
		visited = [ 0 for i in range(10000)]
		n_prohibidos = int(input())
		for i in range(n_prohibidos):
			fb = int(stdin.readline().replace(" ", ""))
			visited[fb]=1
		stdin.readline()
		tc-=1
		print(bfs(conf_inicial,target))

	return

main()



