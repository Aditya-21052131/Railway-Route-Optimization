from flask import Flask, render_template, request
from models.graph import Graph
from models.routes import Routes

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']
        graph = Graph()
        routes = Routes(graph)
        optimized_route = routes.find_optimized_route(origin, destination)
        return render_template('map.html', optimized_route=optimized_route)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
