from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """<html>
<body>

<h2>JavaScript in Body</h2>

<h2 id="demo"></h2>


</body>

<script type="text/javascript" src="https://form.jotform.com/jsform/233024658564055"></script>

<script>
document.getElementById("demo").innerHTML = "My First JavaScript";
</script>

</html> 
"""


@app.route("/test")
def wowow():
    with open('Resources/website.html') as file:
        text = file.read()
    return text


@app.route("/root")
def root():
    with open('Resources/root.html') as file:
        text = file.read()
    return text


if __name__ == '__main__':
    app.run(host='192.168.2.10', port=2000, debug=False)
