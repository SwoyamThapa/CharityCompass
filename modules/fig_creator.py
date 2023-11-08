import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


def fig_creator():
    figs = []

    file_path = 'modules/data/data.json'

    with open(file_path, 'r') as file:
        data = json.load(file)

    org_country_dict = {}

    for entry in data:
        org = entry.get('organization')
        org_name = org.get('name')
        countries = org.get('countries').get('country')

        for country in countries:
            if org_name in org_country_dict:
                org_country_dict[org_name].append(country.get('name'))
            else:
                org_country_dict[org_name] = [country.get('name')]

    df = pd.DataFrame.from_dict(org_country_dict, orient='index').T.melt(value_name='Country', var_name='Organization')
    df = df.dropna(subset=['Country'])

    _fig= go.Figure()

    unique_organizations = df['Organization'].unique()
    color_mapping = {}  

    for idx, organization in enumerate(unique_organizations):
        color = px.colors.qualitative.Plotly[idx % len(px.colors.qualitative.Plotly)]
        color_mapping[organization] = color
        subset_df = df[df['Organization'] == organization]
        text = subset_df['Organization'] + '<br>' + subset_df['Country']
        
        _fig.add_trace(go.Scattergeo(
            locationmode="country names",
            locations=subset_df['Country'],
            text=text,
            marker=dict(size=10, color=color),
            name=organization,  
        ))

    _fig.update_layout(
        title = "Organization's operatiopn country",
        geo=dict(showland=True, landcolor="lightgray"),
        legend_title_text='Organizations',  
    )

    figs.append(_fig)


    df = pd.DataFrame(data)

    _fig = px.bar(df, x='title', y=['goal', 'funding'], title='Project Funding vs. Goal',
                labels={'title': 'Organization', 'value': 'Amount'},
                barmode='group') 

    figs.append(_fig)

    projects = []

    for entry in data:
        org = entry.get('organization')

        projects_info = {
            'Organization' : org.get('name'),
            'totalProjects' : org.get('totalProjects'),
            'activeProjects' : org.get('activeProjects')
        }

        if not projects_info in projects:
            projects.append(projects_info)

    df = pd.DataFrame(projects)

    _fig = px.bar(df, x='Organization', y=['totalProjects', 'activeProjects'], title='TotalProjects and ActiveProjects',
                labels={'title': 'Organization', 'value': 'No. of Projects'},
                barmode='group')  
    
    figs.append(_fig)

    df = pd.DataFrame(data)

    _fig = px.bar(df, x='title', y=['numberOfDonations'], title='Number of Donations',
                labels={'title': 'Organization', 'value': 'No. of Projects'},
                barmode='group')

    figs.append(_fig)

    figure_json_list = [pio.to_json(fig) for fig in figs]


    return figure_json_list


    
