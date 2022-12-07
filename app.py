from flask import Flask, session, render_template, request

import os
import data_utils

app = Flask(__name__)  # Creates a web server which can run your Flask code.and
app.secret_key = (
    "kjhfdskjhfsdghk;odgkjsdkjsdkgsdgjdsghdjgdghdfghdfgdfghfggdf;uaghdfgagf"
)
app.config["SESSION_TYPE"] = "filessystem"


@app.get("/")  # The @ symbol is a Python decorator.
def homepage():
    return render_template(
        "index.html",
        title="Welcome to Swimclub",
    )


def get_data():
    session.clear()  # Just being safe.
    keys = ["age", "distance", "stroke", "average", "average_str", "times", "converts"]
    session["swimmers"] = {}  # Empty dictionary.
    files = os.listdir(swimclub.FOLDER)
    files.remove(".DS_Store")
    for file in files:  # Process each file one at a time.
        name, *the_rest, _times, _converts = swimclub.get_swim_data(
            file
        )  # Get the data.
        if name not in session["swimmers"]:
            session["swimmers"][name] = []
        session["swimmers"][name].append({k: v for k, v in zip(keys, the_rest)})
        session["swimmers"][name][-1]["file"] = file


@app.get("/swimmers")
def get_swimmers_names():
    names = data_utils.get_swimmers_list()
    return render_template(
        "select.html",
        data=sorted(names),
        title="Please select a swimmer from the dropdown list",
        select_id="swimmer",
        url="/showevents",
    )


@app.post("/showevents")
def show_swimmer_files():
    name = request.form["swimmer"]
    events = data_utils.get_swimmer_events(name)
    return render_template(
        "select.html",
        data=events,
        title="Please select an event from the dropdown list",
        select_id="event",
        url="/showchart",
    )


@app.post("/showchart")
def show_event_chart():
    event = request.form["event"]
    swimclub.produce_bar_chart(event, "templates/")
    return render_template(event.removesuffix("txt") + "html")


if __name__ == "__main__":
    app.run(debug=True)  # Starts the web server, and keeps going...
