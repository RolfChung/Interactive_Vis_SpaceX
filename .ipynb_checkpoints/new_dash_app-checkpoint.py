# Import required libraries
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Create sample data if you don't have the CSV
data = {
    'Launch Site': ['Site A', 'Site A', 'Site B', 'Site B', 'Site C'],
    'class': [1, 0, 1, 1, 0],  # 1=success, 0=failure
    'Payload Mass (kg)': [2500, 5000, 3000, 4500, 6000],
    'Booster Version Category': ['v1', 'v2', 'v1', 'v2', 'v1']
}
spacex_df = pd.DataFrame(data)
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('SpaceX Launch Dashboard'),
    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': 'All Sites', 'value': 'ALL'}] + 
               [{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()],
        value='ALL'
    ),
    dcc.Graph(id='success-pie-chart'),
    html.P("Payload range (Kg):"),
    dcc.RangeSlider(
        id='payload-slider',
        min=0, max=10000, step=1000,
        marks={i: str(i) for i in range(0, 10001, 2500)},
        value=[min_payload, max_payload]
    ),
    dcc.Graph(id='success-payload-scatter-chart')
])

@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value'))
def update_pie(selected_site):
    if selected_site == 'ALL':
        fig = px.pie(spacex_df, names='Launch Site', title='All Sites')
    else:
        filtered = spacex_df[spacex_df['Launch Site'] == selected_site]
        fig = px.pie(filtered, names='class', title=f'Site {selected_site}')
    return fig

@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')])
def update_scatter(selected_site, payload_range):
    low, high = payload_range
    filtered = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & 
                       (spacex_df['Payload Mass (kg)'] <= high)]
    if selected_site != 'ALL':
        filtered = filtered[filtered['Launch Site'] == selected_site]
    fig = px.scatter(filtered, x='Payload Mass (kg)', y='class', 
                     color='Booster Version Category')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)