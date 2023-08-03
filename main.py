from K_means import *
from IO import *


# Get the input data points from a CSV file
data_points = read_data_from_csv("samples.csv")

# Determine the best K for the given data points using the elbow method
num_centroids = determine_best_K(data_points)

# Call the k-means_clustering function to get the final centroids' coordinates and the assignment of data points to them
centroids, assignments, sum_derivations = kmeans_clustering(data_points, num_centroids)

# Print the assignment of data points to the final centroids
print(f"Final {num_centroids} Clusters with {sum_derivations} derivations:")
for centroid_index, centroid in enumerate(centroids):
    print(
        f"Data-Points Assigned to the {centroid_index+1}th Centroid at {centroid}:\n {assignments[centroid_index]}"
    )

# Draw the plot
draw_plot(data_points, centroids, assignments)
