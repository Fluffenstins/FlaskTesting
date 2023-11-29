from flask import Flask, make_response
from markupsafe import escape
from flask import request
from GraphAPI import MSDrive

app = Flask(__name__)
global drive

drive = MSDrive()

drive.meta_remote = True
drive.getMeta()

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

@app.route("/search/<search_inp>")
def search(search_inp):
    cookie = request.cookies.get('username')
    print(cookie)
    search_inp = escape(search_inp)
    return f"Hello, {search_inp}"

@app.route("/login")
def login():
    html = "hello"
    ret = make_response(html)
    ret.set_cookie("username", 'Grady')
    return ret

@app.route("/meta")
def meta():
    return '<br>'.join([i for i in drive.meta])


if __name__ == '__main__':
    app.run(host='192.168.2.10', port=80, debug=False)
