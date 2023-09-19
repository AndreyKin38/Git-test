import math
from collections import deque


class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, vertex):
        if vertex not in self._vertex:
            self._vertex.append(vertex)

    def add_link(self, link):
        t = tuple(filter(lambda x: (id(x.v1) == id(link.v1) and id(x.v2) == id(link.v2)) or \
                                   (id(x.v2) == id(link.v1) and id(x.v1) == id(link.v2)), self._links))
        if len(t) == 0:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)

    def get_link(self, v1, v2):
        for link in self._links:
            if (v1 == link.v1 and v2 == link.v2) or (v2 == link.v1 and v1 == link.v2):
                return link

    @staticmethod
    def arg_min(T, S):
        min_arg = -1
        max_arg = math.inf

        for i, j in T.items():
            if j < max_arg and i not in S:
                max_arg = j
                min_arg = i

        return min_arg

    def find_path(self, start_v, stop_v):
        T = dict(zip(self._vertex, (math.inf for _ in range(len(self._vertex)))))
        v = start_v
        S = {v}
        T[v] = 0
        M = dict(zip(self._vertex, (0 for _ in range(len(self._vertex)))))

        while v != -1:
            for i in v.links:
                v2 = i.v2
                if v == v2:
                    v2 = i.v1
                if v2 not in S:
                    w = T[v] + i.dist
                    if w < T[v2]:
                        T[v2] = w
                        M[v2] = v

            v = self.arg_min(T, S)
            if v != -1:
                S.add(v)

        start = start_v
        end = stop_v
        d = deque()
        d += [end]
        link_lst = []

        while end != start:
                end = M[d[0]]
                d.appendleft(end)
                link_lst.append(self.get_link(d[0], d[1]))

        return list(d), link_lst


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

# print(v1.links)
# print(map_metro._links)
# print(map_metro._vertex)
# tree = map_metro._tree(v1)
# print(tree)
# print(map_metro.find_path(v1, v2))

# print(map_metro._routes(tree, 2, 5))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
# print(path)

print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7

