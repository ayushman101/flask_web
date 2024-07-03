from flask import Flask

def create_app():
    app= Flask(__name__)
    app.config["SECRET_KEY"]="feoeiq3n nno aep;gourtp.apeae[ ]"

    return app