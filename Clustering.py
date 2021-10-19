
# %matplotlib qt5
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate some data
#from sklearn.datasets.samples_generator import make_blobs
#X, y_true = make_blobs(n_samples=400, centers=4,
#                       cluster_std=0.60, random_state=0)
#X = X[:, ::-1] # flip axes for better plotting

#Import Data from excel
X = pd.read_excel('TransformerLoadComposition.xlsx',sheet_name="tr_comp3", usecols="A:B")
from sklearn.preprocessing import MinMaxScaler
sc_X = MinMaxScaler()
X = sc_X.fit_transform(X)


# Plot the data with K Means Labels
from sklearn.cluster import KMeans
kmeans = KMeans(4, random_state=0)
labels = kmeans.fit(X).predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
plt.grid(color='black', linestyle=':', linewidth=0.3)

# Plot the data with MeanShift
from sklearn.cluster import MeanShift
Mshift = MeanShift()
labels = Mshift.fit(X).predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
plt.grid(color='black', linestyle=':', linewidth=0.3)

# Plot the data with GMM
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
X_train=X
gmm = GaussianMixture(n_components=6,covariance_type='tied').fit(X_train)
labels = gmm.predict(X_train)

#list the proabilities of the first 5 points in X
probs = gmm.predict_proba(X_train)
print(probs[:200].round(2))
print(silhouette_score(X_train, labels))

#Plot the points in different sizes by the probability 
#size = 50 * probs.max(1) ** 2  # square emphasizes differences; the maximum probability is the one with the assigned cluster
size = 50 * 1 ** 2  # square emphasizes differences; the maximum probability is the one with the assigned cluster
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=size)
plt.grid(color='black', linestyle=':', linewidth=0.3)

#from mpl_toolkits.mplot3d import Axes3D
#import matplotlib.pyplot as plt
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#wireframe = ax.plot_wireframe(X[:, 0], X[:, 1], probs)
#plt.show()


#X, Y = np.meshgrid(np.linspace(0, 1), np.linspace(0,1))
#XX = np.array([X.ravel(), Y.ravel()]).T
#Z = gmm.score_samples(XX)
#Z = Z.reshape((50,50))
#plt.contour(X, Y, Z)
#plt.scatter(X_train[:, 0], X_train[:, 1])

#Given a new datapoint, use GMM to predict the probabilites
from numpy import array
x=array([[6,-1]])
print(gmm.predict_proba(x).round(3))

# Plot the data with DBSCAN
from sklearn.cluster import DBSCAN
labels = DBSCAN(eps=0.5, min_samples=4).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')


