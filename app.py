from flask import Flask

app = Flask(__name__)   # Creates a web server which can run your Flask code.and

## print(f"****** The current value of dunder name is: { __name__ }.")

@app.get("/")   # The @ symbol is a Python decorator.
def homepage():
    ## 1 / 0
    return "Hello from your first webapp.  Alnost too exciting, eh?"


if __name__ == "__main__":
    app.run(debug=True)   # Starts the web server, and keeps going...
