class WeightedGraph(object):

	def __init__(self, vertices, weights, edges):

		self.weights, self.edges = self.sort_edges(weights,edges)
		self.vertices = vertices

	def get_mst_kruskal(self):

		''' The idea is the following, we start iterating over the sorted edges and
			and if the edge is not in the temp list, then this means that we can add it,
			if it is, it means that it is a cycle and so we skip it.
		'''

		temp_edges = [self.edges.pop(0)]
		temp_vertices = [vertex for vertex in temp_edges[0]] #we add the first edge in order to have some base
		#iterate over the rest
		for edge in self.edges:
			#instead of making find-set function we can just do it here
			#if the two are different, then it means, that one of the vertices is not
			#in the list and so we just add it
			#if they are both present, then we just skip to avoid cycles
			first = edge[0] in temp_vertices
			second = edge[1] in temp_vertices
			if not ( first and second):
				temp_edges.append(edge)
				if not first:
					temp_vertices.append(edge[0])
				else:
					temp_vertices.append(edge[1])
		return temp_edges


	def sort_edges(self,weights,edges):

		#the lists for the weights division
		less_than = []
		greater_than = []
		pivot_list = []
		#the lists for the edges
		less_than_edges = []
		greater_than_edges = []
		pivot_edges = []

		#NOTE : is it possible to make it in place ?
		# is the place taken too much ?

		if len(weights) < 1:
			return weights,edges
		else:
			pivot_element = weights[0]

			for index in xrange(len(weights)):

				if weights[index] < pivot_element:

					less_than.append(weights[index])
					less_than_edges.append(edges[index])
				
				elif weights[index] > pivot_element:
				
					greater_than.append(weights[index])
					greater_than_edges.append(edges[index])

				else:

					pivot_list.append(weights[index])
					pivot_edges.append(edges[index])

			less_than, less_than_edges = self.sort_edges(less_than, less_than_edges)
			greater_than, greater_than_edges = self.sort_edges(greater_than,greater_than_edges)
		return (less_than + pivot_list + greater_than, less_than_edges + pivot_edges + greater_than_edges)

if __name__ == '__main__':

	weights = [1,2,3,4,5,6,1]
	edges = [(1,2),(1,3),(3,6),(2,4),(2,6),(4,5),(2,3)]
	vertices = [1,2,3,4,5,6]

	p = WeightedGraph(vertices,weights,edges)
	print p.get_mst_kruskal()