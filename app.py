from flask import Flask, make_response
from markupsafe import escape
from flask import request
from GraphAPI import MSDrive
from time import time

app = Flask(__name__)
global drive

drive = MSDrive()

drive.meta_remote = True
drive.getMeta()
drive.last_meta_update = time()

@app.route("/hello-world")
def hello_world():
    return """<html>
<body>

<h2 id="demo"></h2>

</body>

<script type="text/javascript" src="https://form.jotform.com/jsform/233024658564055"></script>

<script>
document.getElementById("demo").innerHTML = "Testing";
</script>

</html> 
"""


@app.route("/")
def java():
    with open("Resources/meta.html") as file:
        html = file.read()
    return html

@app.route("/meta.css")
def meta_css():
    with open("Resources/meta.css") as file:
        html = file.read()
    return html


@app.route("/meta")
def meta():
    ret = ""
    for nb, info in drive.meta.items():
        job_nums = ', '.join(info['RPAT'] + info['ADM'])
        ret += f"{nb} : {job_nums}<br>"
    return ret


@app.route("/test", methods=['POST'])
def test():
    if time() - drive.last_meta_update > 60:
        print(f"Getting new meta...")
        drive.getMeta()
        drive.last_meta_update = time()
    drive.getMeta()
    query = request.json['query']
    jobs = get_matching_jobs(query)
    ret = []
    for i in jobs:
        ret.append(f"{i['folder name']}")

    return '<br>'.join([str(i) for i in ret])


def get_matching_jobs(query):
    query = query.lower()
    ret = []
    for nb, info in drive.meta.items():
        to_check = [info['folder name'], nb, info['job type']] + info['RPAT'] + info['ADM']
        for name in to_check:
            if name.lower().find(query) != -1:
                ret.append(info)
                break
    return ret


if __name__ == '__main__':
    app.run(host='192.168.2.10', port=80, debug=False)
