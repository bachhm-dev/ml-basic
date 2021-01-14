import matplotlib.pyplot
from sklearn.cluster import KMeans
import numpy

img = matplotlib.pyplot.imread("./k-means/a.jpg")

height = img.shape[0]
width = img.shape[1]
print(img)

img = img.reshape(width*height,3)

kmeans = KMeans(n_clusters=4).fit(img)

labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_

img2 = numpy.zeros_like(img)

for i in range(len(img2)):
    img2[i] = clusters[labels[i]]

img2 = img2.reshape(height,width,3)

matplotlib.pyplot.imshow(img2)
matplotlib.pyplot.show()