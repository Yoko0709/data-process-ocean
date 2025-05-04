🌊 Maritime Accident Risk Prediction using Clustering and Hazard Maps
Overview
This project analyzes historical wave and wind conditions alongside maritime accident records to predict accident-prone sea states. Using machine learning techniques such as clustering and dimensionality reduction, we identify abnormal sea states and visualize accident risk on hazard maps. The analysis focuses on the East China Sea, a high-risk area near Japan.

Motivation
Each year, numerous maritime accidents are caused by weather-related sea conditions. However:

Quantitative prediction of maritime risks remains limited.

Real-time application of weather data for risk prediction is underdeveloped.

This project aims to address these challenges using historical environmental data and unsupervised learning methods.

Methodology
Data Sources

Wave and wind data: ERA5 reanalysis dataset (Copernicus C3S)

Maritime accident data: IMO GISIS Marine Casualties and Incidents

Key Steps

Clustering:

MiniBatch K-Means for efficient exploration of k

Final clustering using K-Means with optimal k determined by Davies-Bouldin Index

Dimensionality Reduction:

PCA used for visualization (capturing 68% variance in 2D)

Hazard Mapping:

Mapping accident probabilities to each sea state cluster

Identifying abnormal clusters with high variance or outliers (e.g., Cluster 7)

Results
Optimal clustering number: k = 12

Abnormal sea conditions identified (e.g., high-variance cluster)

Hazard map created to visualize risk likelihood based on past conditions

2024 accident case successfully analyzed by matching to historical clusters
