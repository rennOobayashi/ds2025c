from collections import deque

class Graph:
	def __init__ (self, size):
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

class Disjoint:
	def __init__(self, n):
		self.parent = [i for i in range(n)]

	def find(self, node):
		if self.parent[node] != node:
			self.parent[node] = self.find(self.parent[node])

		return self.parent[node]

	def marge(self, x, y):
		x_root = self.find(x)
		y_root = self.find(y)

		if x_root != y_root:
			self.parent[y_root] = x_root
			return True

		return False


def print_graph(g) :
	print(' ', end = ' ')
	for v in range(len(g.graph)) :
		print(citys[v], end =' ')
	print()
	for row in range(len(g.graph)) :
		print(citys[row], end =' ')
		for col in range(len(g.graph)) :
			print(f"{g.graph[row][col]:2d}", end=' ')
		print()
	print()

g1 = None
citys = ['인천', '서울', '강릉', '대전', '광주', '부산']
incheon, seoul, gangneung, daejeon, gwangju, busan = 0, 1, 2, 3, 4, 5


graph_size = 6
g1 = Graph(graph_size)
g1.graph[incheon][seoul] = 10; g1.graph[incheon][gangneung] = 15
g1.graph[seoul][incheon] = 10; g1.graph[seoul][gangneung] = 40; g1.graph[seoul][daejeon] = 11; g1.graph[seoul][gwangju] = 55
g1.graph[gangneung][incheon] = 15; g1.graph[gangneung][seoul] = 40; g1.graph[gangneung][daejeon] = 12
g1.graph[daejeon][seoul] = 11; g1.graph[daejeon][gangneung] = 12; g1.graph[daejeon][gwangju] = 20; g1.graph[daejeon][busan] = 30
g1.graph[gwangju][seoul] = 55; g1.graph[gwangju][daejeon] = 20; g1.graph[gwangju][busan] = 28
g1.graph[busan][daejeon] = 30; g1.graph[busan][gwangju] = 28

print('도시 간 도로 건설을 위한 전체 연결도')
print_graph(g1)

edges = []  # 결과적으로 2d list
for i in range(graph_size) :
	for k in range(graph_size) :
		if g1.graph[i][k] != 0 :
			edges.append([g1.graph[i][k], i, k])
print(edges)

print('최소 비용의 도로 연결도')
print_graph(g1)

edges.sort()
print(edges)

ds = Disjoint(graph_size)
mst_edges = []
mst_cost = 0

for cost, s, e in edges:
	if ds.marge(s, e):
		mst_edges.append((cost, s, e))
		mst_cost =  mst_cost + cost

mst_graph = Graph(graph_size)

for cost, s, e in mst_edges:
	mst_graph.graph[s][e] = cost
	mst_graph.graph[e][s] = cost

print_graph(mst_graph)

print(f"최소 비용의 도로 건설 비용 :  {mst_cost}")

print("최소 간선")

for cost, s, e in mst_edges:
	print(f"{citys[s]}--{cost}--{citys[e]}")