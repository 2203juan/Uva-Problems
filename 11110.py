from collections import deque
m = []
def bfs(i,j,n):
	global m,vis
	s = []
	queue = deque()
	queue.append((i,j))
	s.append((i,j))
	vis[i][j]=1	
	b = mat[i][j]
	while len(queue)!=0:
		tmp,tmp2 = queue.popleft()
		c1,c2 = tmp-1,tmp2+0
		if(c1>=0 and c1<n and c2>=0 and c2<n and vis[c1][c2]==0 and mat[c1][c2]==b):
			vis[c1][c2]=1
			queue.append((c1,c2))
			s.append((i,j))
		c1,c2 = tmp+0,tmp2-1
		if(c1>=0 and c1<n and c2>=0 and c2<n and vis[c1][c2]==0 and mat[c1][c2]==b):
			vis[c1][c2]=1
			queue.append((c1,c2))
			s.append((i,j))
		c1,c2 = tmp+1,tmp2+0
		if(c1>=0 and c1<n and c2>=0 and c2<n and vis[c1][c2]==0 and mat[c1][c2]==b):
			vis[c1][c2]=1
			queue.append((c1,c2))
			s.append((i,j))
		c1,c2 = tmp+0,tmp2+1
		if(c1>=0 and c1<n and c2>=0 and c2<n and vis[c1][c2]==0 and mat[c1][c2]==b):
			vis[c1][c2]=1
			queue.append((c1,c2))
			s.append((i,j))
	return len(s)

def solve(mat):
	global vis,m
	n = len(mat)
	result= 'good'
	band = True
	i = 0
	while i<len(mat) and band:
		for j in range(len(vis)):
			if(vis[i][j]==0):
				ans = bfs(i,j,n)
				if(ans<n):
					result = 'wrong'
					band =  False
					break
		i+=1
	return result


def main():
	global m,vis,mat
	while 1:
		n = int(input())
		if n==0:
			break
		l = [ [ int(x) for x in input().split() ] for i in range(n-1)]
		m = []
		band = True
		mat = [ [n-1 for i in range(n)] for j in range(n) ]
		vis =[ [ 0 for i in range(n)] for j in range(n) ] 
		for i in range(n-1):
			band = True
			x = l[i][::2]
			y = l[i][1::2]
			for r,c in zip(x,y):
				band = False
				mat[r-1][c-1] = i



		#for i in range(len(mat)):
		#	print(mat[i])
		#print(m)
		print(solve(mat))
		#m.clear()
		#print(vis)

main()
