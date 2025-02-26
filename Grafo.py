import matplotlib.pyplot as plt
import networkx as nx
from InquirerPy import prompt

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def adj_matrix(self):
        """
        Função para criação de uma matriz de adjacência a partir
        da lista de arestas e sets de nós.
        """

        adj = [[0 for _ in self.nodes] for _ in self.nodes]

        for edge in self.edges:
            node1, node2 = edge[0], edge[1]
            adj[node1][node2] += 1

            if node1 != node2:
                adj[node2][node1] += 1

        return adj
    
    def load_file(self):
        """
        Função load_file lê o arquivo .txt e armazena as colunas relevantes em Edges.
        """

        with open('facebook_combined.txt', 'r') as f:
            for line in f:
                source, target = map(int, line.strip().split())

                self.edges.append((source, target))
                self.nodes.add(source)
                self.nodes.add(target)

    def minDistance(self, dist, sptSet):
        """
        Função auxiliar do dijkstra que calcula qual o nó com 
        menor caminho que ainda não foi processado e retorna seu id.
        """

        min_dist = float('inf')
        min_index = -1
        
        for v in range(len(self.nodes)):
            if not sptSet[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_index = v
        
        return min_index

    def dijkstra(self, src, adj):
        """
        Algoritmo dijkstra retorna o menor caminho entre dois 
        nós e o caminho até lá.
        Função auxiliar de closeness e find_shortest_paths.
        """

        n = len(self.nodes)
        path = [-1] * n

        dist = [float('inf')] * n
        dist[src] = 0
        sptSet = [False] * n
        
        for _ in range(n):
            u = self.minDistance(dist, sptSet)
            if u == -1:
                break
                
            sptSet[u] = True
            
            for v in range(n):
                if adj[u][v] != 0 and not sptSet[v]:
                    nova_dist = dist[u] + 1 
                    if dist[v] > nova_dist:
                        dist[v] = nova_dist

                        path[v] = u

        return dist, path
    
    def BFS(self, adj, node):
        """
        Implementação da Busca por Largura para uma matriz de adjacência
        """

        root = 107
        queue = []
        visited = []

        queue.append(root)
        visited.append(root)

        while queue:
            s = queue.pop()

            if node == s:
                print("Elemento encontrado:", node)
                return True

            for n in range(len(adj)):
                if adj[s][n] == 1 and n not in visited:
                    visited.append(n)
                    queue.append(n)
        
        print("Elemento não encontrado")
        return False
            

    def find_shortest_paths(self, start, end, adj):
        """
        Implementação de uma BFS modificada para encontrar todos os
        nós com a distância mínima calculada pelo dijkstra.
        Função auxiliar de betweenness.
        """

        distances, _ = self.dijkstra(start, adj)

        shortest_dist = distances[end]
        
        if shortest_dist == float('inf'):
            return []
        
        paths = []
        queue = [[start]]
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node == end and len(path) == shortest_dist + 1:
                paths.append(path)
                continue

            if len(path) < shortest_dist + 1:
                for next_node in range(len(adj)):
                    if adj[node][next_node] == 1 and next_node not in path:
                        new_path = path + [next_node]
                        queue.append(new_path)
        
        return paths
    
    def degree(self, adj, node=None):
        """
        Função para calcular o grau de um determinado nó através da
        soma de 1's na linha correspondente.
        """
        
        count = sum(1 for item in adj[node] if item != 0)

        return count
    
    def closeness(self, dist):
        """
        Função que calcula a métrica de closeness a partir da 
        distância(dist) recebida.
        """

        n = sum(1 for d in dist if d != float('inf') and d != 0)
        
        d = sum(d for d in dist if d != float('inf') and d != 0)

        return (n-1)/d

    def betweenness(self, s, t, v):
        """
        Função que calcula a betweenness de um determinado v para o 
        par (s,t).
        """
        if v == s or v == t:
            return 0

        shortest_paths = G.find_shortest_paths(s, t, self.adj_matrix())

        if not shortest_paths:
            return 0

        count = 0
        for paths in shortest_paths:
            if v in paths[1:-1]:
                count += 1

        return count/len(shortest_paths)

    
    def plot_simple(self):
        """
        Função para gerar a versão simples do gráfico do grafo
        """

        G_nx = nx.Graph()
        
        G_nx.add_nodes_from(self.nodes)
        G_nx.add_edges_from(self.edges)

        plt.figure(figsize=(12, 8))

        pos = nx.spring_layout(G_nx)

        nx.draw_networkx_edges(G_nx, pos,
                            width=0.1,
                            alpha=0.2,
                            edge_color='gray')

        nx.draw_networkx_nodes(G_nx, pos,
                            node_size=10,
                            node_color='black',
                            alpha=0.5)

        plt.axis('off')
        plt.tight_layout()
        plt.show()

    def plot(self, metric='degree'):
        """
        Função para gerar a versão composta do gráfico do grafo
        """

        G_nx = nx.Graph()
        
        G_nx.add_nodes_from(self.nodes)
        G_nx.add_edges_from(self.edges)

        pos = nx.spring_layout(G_nx)
        fig, ax = plt.subplots(figsize=(12, 8))

        metrics = {
            'degree': {
                'values': dict(G_nx.degree()),
                'scale_factor': 5,
                'threshold': 330,
                'size_mult': 5,
                'label': 'Grau do nó'
            },
            'closeness': {
                'values': dict(nx.closeness_centrality(G_nx)),
                'scale_factor': 150,
                'threshold': 0.39,
                'size_mult': 2000,
                'label': 'Closeness'
            },
            'betweenness': {
                'values': dict(nx.betweenness_centrality(G_nx)),
                'scale_factor': 7000,
                'threshold': 0.149,
                'size_mult': 8000,
                'label': 'Betweenness'
            }
        }

        metric_data = metrics[metric]
        values = metric_data['values']
        
        sorted_nodes = sorted(G_nx.nodes(), key=lambda x: values[x])
        
        nx.draw_networkx_edges(G_nx, pos,
                            width=0.5,
                            alpha=0.3,
                            ax=ax)

        vmin = min(values.values())
        vmax = max(values.values())
        norm = plt.Normalize(vmin=vmin, vmax=vmax)
        
        for node in sorted_nodes:
            color = plt.cm.viridis(norm(values[node]))
            size = values[node] * (metric_data['scale_factor'] 
                                if values[node] <= metric_data['threshold'] 
                                else metric_data['size_mult'])
            nx.draw_networkx_nodes(G_nx, pos,
                                nodelist=[node],
                                node_size=size,
                                node_color=[color],
                                ax=ax)

        high_value_nodes = [node for node in G_nx.nodes() if values[node] > metric_data['threshold']]
        labels = {node: str(node) for node in high_value_nodes}
        
        nx.draw_networkx_labels(G_nx, pos, 
                            labels,
                            font_size=8,
                            font_weight='bold',
                            ax=ax)

        sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=norm)
        plt.colorbar(sm, ax=ax, label=metric_data['label'])

        plt.title(f"Rede Social: Tamanho e cor baseados - {metric_data['label']}")
        ax.axis('off')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    G = Graph()
    G.load_file()

    adj = G.adj_matrix()

    nodes_dict = {node: 0 for node in G.nodes}

    while(True):
        options = [
            {
                "type" : "list",
                "name" : "operação",
                "message" : "Escolha uma operação do Grafo:",
                "choices": ["Degree", "Closeness", "Betweenness", "Pesquisar", "Gráfico", "Sair"]
            },
        ]

        resultado = prompt(options)

        if resultado["operação"] == "Degree":
            for node in G.nodes:
                d = G.degree(adj, node)
                nodes_dict[node] += d

            print(dict(sorted(nodes_dict.items(), key=lambda x: x[1], reverse=False)))

        elif resultado["operação"] == "Closeness":
            for node in G.nodes:
                dist, _ = G.dijkstra(node, adj)
                r = round(G.closeness(dist), 3)
                nodes_dict[node] += r

            print(dict(sorted(nodes_dict.items(), key=lambda x: x[1], reverse=False)))

        elif resultado["operação"] == "Betweenness":
            for s in G.nodes:
                for t in G.nodes:
                    if s != t:
                        for v in G.nodes:
                            if v != s and v != t:
                                b = round(G.betweenness(s, t, v), 5)
                                nodes_dict[v] += b

            print(dict(sorted(nodes_dict.items(), key=lambda x: x[1], reverse=False)))


        elif resultado["operação"] == "Pesquisar":
            node_to_find = int(input("Digite o nó a ser encontrado: "))

            G.BFS(adj, node_to_find)

        elif resultado["operação"] == "Gráfico":
            metric_in = str(input("Digite a métrica(degree/closeness/betweenness/simples) a ser avaliada: "))

            if metric_in == "simples":
                G.plot_simple()
            else:
                G.plot(metric = metric_in)

        else:
            print("Saindo...")
            break