from flask import Flask, url_for, render_template
from routes.port import port_route
app = Flask(__name__)

app.register_blueprint(port_route)


app.run(debug=True, port=8050, host='0.0.0.0')

