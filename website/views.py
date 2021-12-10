from flask import Blueprint, render_template, url_for
import json

with open("website/topics.json") as file:
    topics = json.load(file)

blueprint = Blueprint("templates", __name__, "templates")


@blueprint.route("/")
def main():
    return render_template("base.html")


@blueprint.route("/topics/<path:topic>")
def tps(topic="time-period"):
    if topic not in topics.values():
        topic = "time-period"
    title = (list(topics.keys())[list(topics.values()).index(topic)])
    print(title)
    return render_template("Topics/" + topic + ".html", title=title, topics=topics)
