from flask import Flask

import os
import swimclub

app = Flask(__name__)  # Creates a web server which can run your Flask code.and


@app.get("/")  # The @ symbol is a Python decorator.
def homepage():
    ## 1 / 0
    return "Hello from your first webapp.  Alnost too exciting, eh?"


@app.get("/about")
def display_about_message():
    return "This is the about page for this site."


def get_data():
    keys = ["age", "distance", "stroke", "average", "average_str", "times", "converts"]
    swimmers = {}  # Empty dictionary.
    files = os.listdir(swimclub.FOLDER)
    files.remove(".DS_Store")
    for file in files:  # Process each file one at a time.
        name, *the_rest = swimclub.get_swim_data(file)  # Get the data.
        if name not in swimmers:
            swimmers[name] = []
        swimmers[name].append({k: v for k, v in zip(keys, the_rest)})
        swimmers[name][-1]["file"] = file
    return swimmers 


@app.get("/swimmers")
def get_swimmers_names():
    swimmers = get_data()
    return str(sorted(swimmers))


@app.get("/files/<swimmer>")
def get_swimmers_files(swimmer):
    swimmers = get_data()
    events = []
    for event in swimmers[swimmer]:  # a list of dictionaries, with "file" as a key
        events.append(event["file"])
    return events


if __name__ == "__main__":
    app.run(debug=True)  # Starts the web server, and keeps going...
