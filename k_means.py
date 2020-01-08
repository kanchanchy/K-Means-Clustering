import scipy.io
import numpy as np
import random
from matplotlib import pyplot as plt

#Method for selecting initial centers randomly
def init_center_randomly(data, k):
	center_list = []
	index_list = []
	for i in range(k):
		while True:
			random_index = random.randrange(len(data) - 1)
			if random_index not in index_list:
				index_list.append(random_index)
				center_list.append(data[random_index])
				break
	return np.array(center_list)

#Method for selecting initial centers based on distance or strategy 2
def init_center_by_distance(data, k):
	center_list = []
	index_list = []
	random_index = random.randrange(len(data) - 1)
	index_list.append(random_index)
	center_list.append(data[random_index])

	for i in range(1, k):
		max_distance = 0
		selected_index = -1
		for j in range(len(data)):
			if j not in index_list:
				distance = 0
				for center in center_list:
					distance += ((data[j][0] - center[0])**2 + (data[j][1] - center[1])**2)**0.5
				distance = distance/len(center_list)
				if distance > max_distance:
					max_distance = distance
					selected_index = j
		index_list.append(selected_index)
		center_list.append(data[selected_index])
	return np.array(center_list)


# Method for finding the closest cluster for each data sample
def find_closest_cluster(instance, center_list):
	distances = []
	for center in center_list:
		distances.append(((instance[0] - center[0])**2 + (instance[1] - center[1])**2)**0.5)
	distances = np.array(distances)
	min_distance = np.amin(distances)
	return (np.where(distances == min_distance))[0][0]

#Method for finding value of given objective function
def find_squared_error(center_list, cluster_final):
	squared_error = 0
	for key in cluster_final:
		center = center_list[key]
		for instance in cluster_final[key]:
			squared_error += (instance[0] - center[0])**2 + (instance[1] - center[1])**2
	return squared_error

#Method for finding clusters untill centers converge
def find_clusters(data, center_list):
	cluster_final = {}
	while True:
		clusters = {}
		for instance in data:
			cluster_index = find_closest_cluster(instance, center_list)
			if cluster_index in clusters:
				clusters[cluster_index].append(instance)
			else:
				clusters[cluster_index] = [instance]
		new_center_list = []
		for i in range(no_cluster):
			if i in clusters:
				np_cluster = np.array(clusters[i])
				new_center_list.append(np.mean(np_cluster, axis = 0))
			else:
				new_center_list.append(center_list[i])
		if np.array_equal(np.array(center_list), np.array(new_center_list)):
			cluster_final = clusters
			break
		else:
			center_list = new_center_list
	return center_list, cluster_final



#loading dataset
Numpyfile= scipy.io.loadmat('AllSamples.mat')

data = Numpyfile['AllSamples']

#find clusters and objective function based on strategy 1
#Iterate for each attempt
for t in range(2):
	#Iterate for various number of clusters
	list_cluster_number = []
	list_squared_error = []
	for no_cluster in range(2, 11):
		#initialize center randomly
		center_list = init_center_randomly(data, no_cluster)

		center_list, cluster_final = find_clusters(data, center_list)

		#Calculate value of objective function:
		squared_error = find_squared_error(center_list, cluster_final)
		list_cluster_number.append(no_cluster)
		list_squared_error.append(squared_error)

	#plot objective function vs number of cluster
	plt.plot(list_cluster_number, list_squared_error)
	plt.xlabel("Number of Clusters")
	plt.ylabel("Value of Objective Function")
	plt.title("Randomly initiated centers: " + str(t + 1))
	plt.show()


#find clusters and objective function based on strategy 2
#Iterate for each attempt
for t in range(2):
	#Iterate for various number of clusters
	list_cluster_number = []
	list_squared_error = []
	for no_cluster in range(2, 11):
		#initialize center randomly
		center_list = init_center_by_distance(data, no_cluster)

		center_list, cluster_final = find_clusters(data, center_list)

		#Calculate value of objective function:
		squared_error = find_squared_error(center_list, cluster_final)
		list_cluster_number.append(no_cluster)
		list_squared_error.append(squared_error)

	#plot objective function vs number of cluster
	plt.plot(list_cluster_number, list_squared_error)
	plt.xlabel("Number of Clusters")
	plt.ylabel("Value of Objective Function")
	plt.title("Distance based initiated centers: " + str(t + 1))
	plt.show()



