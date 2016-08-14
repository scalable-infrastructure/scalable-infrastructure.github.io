from pyspark.mllib.clustering import KMeans
from numpy import array
from math import sqrt

# Load and parse the data
# Upload Sample data: hadoop fs -put /data/kmeans_data.txt .
data = sc.textFile("kmeans_data.txt")
parsedData = data.map(lambda line: array([float(x) for x in line.split(' ')]))

# Build the model (cluster the data)
clusters = KMeans.train(parsedData, 2, maxIterations=10,
                        runs=10, initializationMode="random")


print str(clusters.clusterCenters)

parsedData.map(lambda point: (str(point), clusters.predict(point))).collect()






##################################################################################################
# Evaluate clustering by computing Within Set Sum of Squared Errors
def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
print("Within Set Sum of Squared Error = " + str(WSSSE))