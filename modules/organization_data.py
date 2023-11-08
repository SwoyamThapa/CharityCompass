import json

def get_updated_data():
    file_path = 'modules/data/data.json'

    with open(file_path, 'r') as file:
        data = json.load(file)


    new_data = []

    for items in data:

        org = items.get('organization')
        
        org_info = {
            'name' : org.get('name'),
            'address1' : org.get('addressLine2'),
            'address2' : org.get('addressLine2'),
            'city' : org.get('city'),
            'state' : org.get('state'),
            'postal' : org.get('postal'),
            'country' : org.get('iso3166CountryCode'),
            'url' : org.get('url'),
            'mission' : org.get('mission'),
            'themes' : [theme.get('name') for theme in org.get('themes').get('theme')],
            'countries' : [country.get('name') for country in org.get('countries').get('country')],
            'totalProjects' : org.get('totalProjects'),
            'activeProjects' : org.get('activeProjects'),
            'goal' : items.get('goal'),
            'funding' : items.get('funding')
        }

        new_data.append(org_info)

    return new_data

    