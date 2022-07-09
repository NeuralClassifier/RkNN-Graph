
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import sklearn
from scipy.sparse.csgraph import minimum_spanning_tree
import time
import sklearn
from math import sqrt

def reverse_k_max_NNG(self,k):

    reverse_kmax_NNG = np.zeros(self.pairwise_distances.shape)

    for can in range(self.nearest_neighbors.shape[0]):
        #if k>1:
        k_neighbors = self.nearest_neighbors[can][:k]
        #print("k-neighbors: ",k_neighbors)
        natural_neighb_count = 0
        for neighb in k_neighbors:
            if can in self.nearest_neighbors[neighb][:k]:
                natural_neighb_count +=1
                if reverse_kmax_NNG[can,neighb] != 1:
                    reverse_kmax_NNG[can,neighb] = 1
                    reverse_kmax_NNG[neighb,can] = 1

        print("RkNN neighbors count: ",natural_neighb_count)

        self.reverse_k_NNG = reverse_kmax_NNG