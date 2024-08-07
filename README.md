# Railway-Route-Optimization
This project demonstrates a route optimization algorithm using Python, Graph Theory, and Dijkstra's algorithm to find the shortest and most efficient route for trains between two stations.


The project consists of the following components:

* A Flask web application that allows users to input origin and destination stations and displays the optimized route on a map.
* A Graph class that represents the railway network and implements Dijkstra's algorithm to find the shortest path between two stations.
* A Routes class that uses the Graph class to find the optimized route between two stations.
* A map.html template that displays the optimized route on a map using Google Maps API.

To run the project, follow these steps:

1. Install the required packages by running `pip install -r requirements.txt`.
2. Run the Flask application by running `python app.py`.
3. Open a web browser and navigate to `http://localhost:5000`.
4. Input the origin and destination stations and click the "Find Optimized Route" button.
5. The optimized route will be displayed on a map.

