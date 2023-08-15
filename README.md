<div align="center">
  <h1><strong>K-means Clustering Assignment Model</strong></h1>
  
![Screenshot (216)](https://github.com/Roodaki/Kmeans-Clustering-Assignment-Model/assets/89901590/b923a8b7-f707-41e2-a602-816651ba3711)
</div>

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage Guide](#usage-guide)

## Introduction
This project implements the K-means clustering algorithm using an Assignment Model (within the context of Operations Research) with the NetworkX library. The assignment model efficiently assigns each data point to the nearest cluster based on their distance, and the centroids' values are updated iteratively using the mean of each cluster's assigned data points. To determine the optimal number of clusters, the project utilizes the Elbow Method, automating the process without requiring user input for K. The Elbow Method helps to identify the number of clusters that best captures the underlying patterns in the data. The program reads a CSV file containing the data points and plots the resulting clusters using matplotlib.

![Screenshot (215)](https://github.com/Roodaki/Kmeans-Clustering-Assignment-Model/assets/89901590/409a214f-ac7c-4e5c-abbe-9fcacff7fedf)

## Project Structure
The project follows a specific structure to organize its files and directories:
```
Kmeans-Clustering-Assignment-Model/
├── K_means.py
├── IO.py
├── main.py
├── samples.csv
├── .gitignore
└── README.md
```
- `K_means.py:`: This file contains the implementation of the K-means clustering algorithm using network design techniques and the NetworkX library. It includes functions for assignment modeling, k-means clustering, and determining the best K using the elbow method.
- `IO.py`: This file contains the input/output operations for reading data points from a CSV file and drawing the scatter plot.
- `main.py`: This is the entry point of the application. It imports the necessary functions from `K_means` and `IO` modules, reads data points from a CSV file, performs K-means clustering, and draws the scatter plot to visualize the results.
- `samples.csv`: This file contains the input data points for the K-means clustering algorithm. It is a CSV file with x and y coordinates for each data point.
- `.gitignore`: This file specifies which files and directories should be ignored by version control, such as Git.
- `README.md`: This file provides documentation and information about the project, its structure, and how to use it.

## Getting Started
### Requirements
* Python (version 3.0 or higher)
* NetworkX library
* Matplotlib library
* Git command line tool (or Git GUI client) to clone the repository.
### Installation
1. Install the required dependencies: `pip install networkx matplotlib`
2. Open a terminal or command prompt and clone this repository: `git clone https://github.com/Roodaki/Kmeans-Clustering-Assignment-Model.git`
### Usage Guide
1. Prepare your dataset as a CSV file with the x and y coordinates for each data point and Update the path to your dataset file in the code.
2. Execute the main script: `python main.py`
3. The program will run the K-means clustering algorithm, visualize the clusters, and display the optimal number of clusters based on the Elbow Method.
