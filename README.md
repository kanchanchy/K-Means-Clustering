# K-Means Clustering
This repository implements K-Means clustering algorithm and applies the algorithm to cluster a dataset, which contains a set of 2-D points. It uses two different strategies for choosing the initial cluster centers:

Strategy 1: It randomly picks the initial centers from the given samples.

Strategy 2: It picks the first center randomly. For the i-th center (i>1), it chooses a sample (among all possible samples) such that the average distance of this chosen one to all previous (i-1) centers is maximal.

The implementation performs clustering with the number of clusters ranging from 2-10 and plots the objective function value vs. the number of clusters. Under each cluster center initialization strategy, it plots the objective function twice, each starting from a different initialization. The plots are shown below:

![Random_Initialization_1](https://github.com/kanchanchy/K-Means-Clustering/tree/master/Plots/random_1.png)

![Random_Initialization_2](https://github.com/kanchanchy/K-Means-Clustering/tree/master/Plots/random_2.png)

![Distance_Initialization_1](https://github.com/kanchanchy/K-Means-Clustering/tree/master/Plots/distance_1.png)

![Distance_Initialization_2](https://github.com/kanchanchy/K-Means-Clustering/tree/master/Plots/distance_2.png)
