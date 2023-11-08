from flask import Flask, render_template, redirect, url_for
from modules.fig_creator import fig_creator
from modules.organization_data import get_updated_data


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/organizations')
def organizations():
    data = get_updated_data()

    return render_template("organizations.html",organizations = data)

@app.route('/compiled_data')
def compiled_data():

    figure_json_list = fig_creator()
    return render_template('compiled_data.html', figure_json_list=figure_json_list)

if __name__ == '__main__':
    app.run()