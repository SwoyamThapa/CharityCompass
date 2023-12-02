from flask import Flask, render_template, request, redirect,url_for
from modules.fig_creator import fig_creator
from modules.organization_data import get_updated_data
import json

app = Flask(__name__)

organization = []

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

@app.route('/add_organizations')
def add_organizations():
    return render_template('add_organization.html')

@app.route('/submit', methods=['POST'])
def submit():

    org_info = {
        'name': request.form['orgName'],
        'address1': request.form['orgAddress1'],
        'address2': request.form['orgAddress2'],
        'city': request.form['orgCity'],
        'state': request.form['orgState'],
        'postal': request.form['orgPostal'],
        'country': request.form['orgCountry'],
        'url': request.form['orgURL'],
        'mission': request.form['orgMission'],
        'themes': request.form['orgThemes'].split(','),
        'countries': request.form['orgCountries'].split(','),
        'totalProjects': request.form['orgTotalProjects'],
        'activeProjects': request.form['orgActiveProjects'],
        'goal': request.form['orgGoal']
    }

    organization.append(org_info)

    with open('modules/data/organizations.json', 'w') as json_file:
        json.dump(organization, json_file, indent=2)

    return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.run()