from flask import Flask

import os
import swimclub

app = Flask(__name__)   # Creates a web server which can run your Flask code.and

## print(f"****** The current value of dunder name is: { __name__ }.")


@app.get("/")   # The @ symbol is a Python decorator.
def homepage():
    ## 1 / 0
    return "Hello from your first webapp.  Alnost too exciting, eh?"


@app.get("/about")
def display_about_message():
    return "This is the about page for this site."


@app.get("/swimmers")
def get_swimmers_names():
    keys =  ["age", "distance", "stroke", "average", "average_str", "times", "converts" ]

    swimmers = {}  # Empty dictionary.

    files = os.listdir(swimclub.FOLDER)
    files.remove(".DS_Store")

    # At this point, I have 61 filenames in "files".

    for file in files:   # Process each file one at a time.
        name, *the_rest = swimclub.get_swim_data(file)   # Get the data. 
        if name not in swimmers:
            swimmers[name] = []
        swimmers[name].append( { k: v for k, v in zip(keys, the_rest)} )  # Add the data to the dictionary.
        swimmers[name][-1]["file"] = file   # Remembering the filename which contains the data. 

    return str(sorted(swimmers.keys()))

if __name__ == "__main__":
    app.run(debug=True)   # Starts the web server, and keeps going...
