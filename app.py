import json
import random

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/member')
def hello_world():
    with open("templates/info.json", "rt", encoding="utf-8") as file:
        file_json = json.loads(file.read())
    quantity_members = len(file_json["members"])
    number_member = random.randint(0, quantity_members - 1)

    name = file_json["members"][number_member]["name"]
    picture = file_json["members"][number_member]["picture"]
    picture = url_for('static', filename=picture)
    content = file_json["members"][number_member]["content"]
    content_list = content.split(", ")
    content_list.sort()
    content = ", ".join([info for info in content_list])
    return render_template("index.html", name=name, picture=picture, content=content)


if __name__ == '__main__':
    app.run()
