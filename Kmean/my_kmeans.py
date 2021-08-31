import numpy as np
from itertools import permutations
from sklearn import datasets
from matplotlib import pyplot
from scipy.spatial.distance import cdist

def centroids_random_select(X, n_clusters):
    return X[np.random.choice(X.shape[0], size=n_clusters, replace=False), :]


def centroids_smart_select(X, n_clusters):
    """
    Input:
    X: numpy array, dimension (n, d) - dataset
    n_clusters: int - so cum (clusters)
    Output:
    centroids: numpy array, dimension (n_cluster, d)
            - cac centroid duoc chon de bat dau thuat toan
    """
    n = X.shape[0]
    first_centroid = X[np.random.randint(n)]
    centroids = [first_centroid] # init centroids with one random point as init centroid
    
    # select n - 1 remaining point
    for k in range(n_clusters - 1):
        # distance of each point with all selected centroids
        all_dists = cdist(X, centroids)
        # minimum distance of each point with all selected centroids
        all_min_dists = np.amin(all_dists, axis = 1)
        # choose point with maximum minimum distance with all selected centroids
        id_new_centroid = np.argmax(all_min_dists) 
        new_centroid = X[id_new_centroid]
        centroids.append(new_centroid)
    # casting list into numpy array then return
    return np.array(centroids)

def find_nearest_centroid(x, centroids):
    """
    Input:
    x: numpy array, dimension (d, ) - diem data
    centroids: numpy array, dimension (n_clusters, d) - cac centroid hien tai
    Output:
    label_x: int - so thu tu centroid gan x nhat (trong khoang 0...n_clusters)
    distance_x: float64 - khoang cach tu x den centroid gan x nhat
    """
    # Khoang cach Euclidean tu diem x den tat cac diem centroid
    D = cdist([x], centroids) 
    label_x = np.argmin(D)
    distance_x = np.amin(D)
    return label_x, distance_x 

def find_new_centroid(X, labels, j):
    """
    Input:
    X: numpy.ndarray, dimension (n, d) - dataset
    labels: numpy.ndarray, dimension (n, ) - array chua cluster hien tai cua tung diem data
            (Voi diem data X[i], labels[i] = so thu tu cua cluster dang chua X[i])
    j: int (trong khoang 0...n_clusters) - so thu tu cua cluster dang can update centroid
    Output:
    new_centroid_j: numpy.ndarray, dimension (d, ) - centroid moi cua cluster thu j
    """
    X_cluster = []
    for i in range(X.shape[0]):
        if labels[i] == j:
            X_cluster.append(X[i])
    #X_cluster = X[labels == j, :]
    return np.mean(X_cluster, axis = 0) 

def my_kmeans(X, n_clusters, max_iter=100, smart=False):
    # Khoi tao cac centroid ban dau bang cach chon ngau nhien
    centroids = (
        centroids_smart_select(X, n_clusters) if smart
        else centroids_random_select(X, n_clusters)
    )
    labels = - np.ones(X.shape[0])  # khoi tao bang vector [-1, -1, ..., -1]
    for iteration in range(max_iter):
        # voi moi diem data X[i], tim centroid gan nhat cho X[i]
        for i in range(X.shape[0]):
            labels[i], _ = find_nearest_centroid(X[i], centroids)
        # voi moi cluster j, cap nhat lai centroid cho cluster j
        new_centroids = np.empty((n_clusters, X.shape[1])) # khoi tao mang diem trung tam moi
        for j in range(n_clusters):
            new_centroids[j] = find_new_centroid(X, labels, j) #
        # neu cac centroid da cap nhat van bang cac centroid cu thi dung lai
        if np.sum((centroids - new_centroids) ** 2) < 1e-200:
            break
        else:
            centroids = new_centroids
    return centroids, labels
X = [1,2,3,4]
print(X[1:2])