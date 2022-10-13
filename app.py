from flask import Flask, session

import os
import swimclub

app = Flask(__name__)  # Creates a web server which can run your Flask code.and
app.secret_key = (
    "kjhfdskjhfsdghk;odgkjsdkjsdkgsdgjdsghdjgdghdfghdfgdfghfggdf;uaghdfgagf"
)


@app.get("/")  # The @ symbol is a Python decorator.
def homepage():
    ## 1 / 0
    return "Hello from your first webapp.  Alnost too exciting, eh?"


@app.get("/about")
def display_about_message():
    return "This is the about page for this site."


def get_data():
    keys = ["age", "distance", "stroke", "average", "average_str", "times", "converts"]
    session["swimmers"] = {}  # Empty dictionary.
    files = os.listdir(swimclub.FOLDER)
    files.remove(".DS_Store")
    for file in files:  # Process each file one at a time.
        name, *the_rest = swimclub.get_swim_data(file)  # Get the data.
        if name not in session["swimmers"]:
            session["swimmers"][name] = []
        session["swimmers"][name].append({k: v for k, v in zip(keys, the_rest)})
        session["swimmers"][name][-1]["file"] = file


@app.get("/swimmers")
def get_swimmers_names():
    if "swimmers" not in session:
        get_data()
    return str(sorted(session["swimmers"]))


@app.get("/files/<swimmer>")
def get_swimmers_files(swimmer):
    if "swimmers" not in session:
        get_data()
    events = []
    for event in session["swimmers"][swimmer]:
        events.append(event["file"])
    return events


if __name__ == "__main__":
    app.run(debug=True)  # Starts the web server, and keeps going...
