## 함수
class Graph() :
    def __init__(self, size):
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


## 변수


## 메인
G1 = Graph(4)
A, B, C, D = 0, 1, 2, 3

G1.graph[A][B] = 1 ; G1.graph[A][C] = 1 ; G1.graph[A][D] = 1
G1.graph[B][A] = 1 ; G1.graph[B][C] = 1
G1.graph[C][A] = 1 ; G1.graph[C][B] = 1 ; G1.graph[C][D] = 1
G1.graph[D][A] = 1 ; G1.graph[D][A] = 1


## 응용하기 : 도시 간의 최단 거리 찾기, 도로공사에서 최저가 비용 구하기