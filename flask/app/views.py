from app import app, render_template
import os

@app.route("/")
def index():
    

    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"
    return "Hello from Flask"

@app.route("/test")
def templateTest():
    return render_template("main.html")
