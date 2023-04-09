import os
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
  def __init__(self):
    self.subscribers = []
    self.filename = None
    self.G = nx.MultiGraph()

  def subscribe(self, callback):
    self.subscribers.append(callback)

  def unsubscribe(self, callback):
    self.subscribers.remove(callback)

  def notify(self):
    for sub in self.subscribers:
      sub()

  def has_file(self):
    return bool(self.filename)

  def set_file(self, filename):
    if self.filename:
      self.save()

    if not filename:
      self.filename = None
      self.notify()
      return

    if not os.path.isfile(filename):
      nx.write_edgelist(self.G, filename, data=True)

    self.G = nx.read_edgelist(filename, create_using=nx.DiGraph)

    self.filename = filename
    self.notify()

  def get_filename(self):
    if self.filename:
      return os.path.basename(self.filename)
    else:
      return 'no file'

  def save(self):
    nx.write_edgelist(self.G, self.filename, data=True)

  def add_node(self, node_name):
    self.G.add_node(node_name)
    self.save()

  def remove_node(self, node_name):
    if self.G.has_node(node_name):
      self.G.remove_node(node_name)
      self.save()

  def edit_node(self, node_name, new_node_name):
    self.G.add_node(new_node_name)
    neighbor_list = list(self.G[node_name])
    for neighbor in neighbor_list:
      neighbor_name = str(neighbor)
      edge = self.G.edges[node_name, neighbor_name]['connection']
      self.G.add_edge(new_node_name, neighbor_name, connection=edge)
    self.remove_node(node_name)
    self.save()

  def add_connection(self, connection_name, node1, node2):
    self.G.add_edge(node1, node2, connection=connection_name)
    self.save()

  def remove_connection(self, node1, node2):
    self.G.remove_edge(node1, node2)
    self.save()

  def edit_connection(self, new_connection_name, node1, node2):
    self.G.remove_edge(node1, node2)
    self.G.add_edge(node1, node2, connection=new_connection_name)
    self.save()

  def find(self, node1, node2):
    if self.G.has_node(node1) and self.G.has_node(node2):
      res = []

      paths = nx.all_simple_paths(self.G, node1, node2)
      res.append(('Поиск с учётом возможного направления связи', list(paths)))
      paths = nx.all_simple_paths(self.G.to_undirected(), node1, node2)
      res.append(('Поиск без учёта возможного направления связи', list(paths)))

      return res
    else:
      return []

  def show(self):
    if self.G.edges:
      pos = nx.spring_layout(self.G, seed=3)
      nx.draw(self.G, pos, with_labels=True)
      edge_weight = nx.get_edge_attributes(self.G, 'connection')
      nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_weight, label_pos=0.5)
      plt.show()
    else:
      nx.draw(self.G, with_labels=True)
      plt.show()

  def get_nodes(self):
    return list(self.G.nodes)

  def get_edges(self):
    return list(self.G.edges)