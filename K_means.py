import networkx as nx


# Function to assign data points to centroids using network flow algorithm
def assignment_model(left_points, right_points):
    # Create a directed graph for assignment network
    assignment_network = nx.DiGraph()

    # Add a terminal node "T" with demand equal to the number of left points
    assignment_network.add_node("T", demand=len(left_points))

    # Add right points as nodes and edges with zero weight to terminal node "T"
    for right_node_index in range(len(right_points)):
        assignment_network.add_node(f"R{right_node_index}")
        assignment_network.add_edge(f"R{right_node_index}", "T", weight=0)

    # Add left points as nodes and edges with distances to right points
    for left_node_index, left_point in enumerate(left_points):
        assignment_network.add_node(f"L{left_node_index}", demand=-1)
        for right_node_index, right_point in enumerate(right_points):
            distance = (
                (left_point[0] - right_point[0]) ** 2
                + (left_point[1] - right_point[1]) ** 2
            ) ** 0.5
            assignment_network.add_edge(
                f"L{left_node_index}", f"R{right_node_index}", weight=distance
            )

    # Solve the network flow problem and get the flow cost and flow dictionary
    flow_cost, flow_dict = nx.capacity_scaling(assignment_network)

    # Extract the assigned left points instead of indices
    assigned_points = [[] for _ in range(len(right_points))]
    for node_name in flow_dict:
        if node_name.startswith("L"):
            for right_node_name in flow_dict[node_name]:
                if flow_dict[node_name][right_node_name] > 0:
                    assigned_points[int(right_node_name[1:])].append(
                        left_points[int(node_name[1:])]
                    )
    return assigned_points, flow_cost


# Function to perform k-means clustering
def kmeans_clustering(data_points, k):
    # Initialize the centroids list with (0,0) coordinates for each centroid
    centroids = [(0, 0) for _ in range(k)]

    # Iterate until the centroids don't change anymore
    while True:
        # Assign each data point to its closest centroid
        new_assignment, sum_derivations = assignment_model(data_points, centroids)

        # Update the centroids to be the average of the assigned data points
        new_centroids = []
        for assigned_points in new_assignment:
            if len(assigned_points) == 0:
                new_centroids.append((0, 0))
            else:
                centroid_x = sum(point[0] for point in assigned_points) / len(
                    assigned_points
                )
                centroid_y = sum(point[1] for point in assigned_points) / len(
                    assigned_points
                )
                new_centroids.append((centroid_x, centroid_y))

        # Check if the centroids have changed
        if new_centroids == centroids:
            break
        centroids = new_centroids

    return centroids, new_assignment, sum_derivations


# Function to determine the best K for the given data points using the elbow method
def determine_best_K(data_points):
    for K in range(1, len(data_points)):
        current_sum_derivations = kmeans_clustering(data_points, K)[2]
        next_sum_derivations = kmeans_clustering(data_points, K + 1)[2]
        if current_sum_derivations - next_sum_derivations < 1:
            return K
    return len(data_points)
