
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
    
    Wow
    
    """


if __name__ == '__main__':
    app.run(host='192.168.2.10', port=8080, debug=False)
