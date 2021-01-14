import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy

img = plt.imread("./k-means/a.jpg")

height = img.shape[0]
width = img.shape[1]


img = img.reshape(width*height,3)

kmeans = KMeans(n_clusters=3).fit(img)

labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_

img2 = numpy.zeros((height,width,3), dtype=numpy.uint8)

index = 0
for i in range(height):
    for j in range(width):
       label_of_pixel = labels[index]
       img2[i][j] = clusters[label_of_pixel]
       index+=1



plt.imshow(img2)
plt.show()