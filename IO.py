import matplotlib.pyplot as plt
import csv


# Function to read data points from a CSV file
def read_data_from_csv(file_name):
    data_points = []
    with open(file_name, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            x = float(row["x"])
            y = float(row["y"])
            data_points.append([x, y])
    return data_points


# Function to draw the scatter plot
def draw_plot(data_points, centroids, assignments):
    # Prepare the data for plotting
    x = [point[0] for point in data_points]
    y = [point[1] for point in data_points]

    # Plot the data points
    plt.scatter(x, y, color="blue", label="Data Points")

    # Plot the centroids with a plus symbol
    centroids_x = [centroid[0] for centroid in centroids]
    centroids_y = [centroid[1] for centroid in centroids]
    plt.scatter(centroids_x, centroids_y, marker="+", color="red", label="Centroids")

    # Color the data points based on their assigned centroid
    colors = [
        "blue",
        "green",
        "red",
        "cyan",
        "magenta",
        "yellow",
        "black",
        "orange",
        "purple",
        "gray",
    ]
    for i, assigned_points in enumerate(assignments):
        for point in assigned_points:
            plt.scatter(point[0], point[1], color=colors[i])

    # Add labels and title to the plot
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("K-Means Clustering")

    # Add legend to the plot
    plt.legend()

    # Show the plot
    plt.show()
