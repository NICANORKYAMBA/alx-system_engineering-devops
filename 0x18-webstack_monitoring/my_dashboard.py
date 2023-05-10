#!/usr/bin/python3


import requests
import os

# Define your Datadog API credentials
api_key = os.environ['DD_API_KEY']
app_key = os.environ['DD_APP_KEY']

# Define the name of your dashboard
dashboard_name = 'MyDashboard'

# Define the Datadog API endpoint
url = f'https://api.datadoghq.com/api/v1/dashboard'

# Define the headers for the Datadog API request
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

# Define the Datadog API query parameters
params = {
    'filter': dashboard_name
}

# Send a GET request to the Datadog API to get the dashboards
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code != 200:
    print(f'Request failed with status code {response.status_code}.')
    exit(1)

# Extract the ID of the first dashboard with the specified name
data = response.json()
if 'dashboards' not in data or not data['dashboards']:
    print(f'No dashboard found with name "{dashboard_name}".')
    exit(1)
dashboard_id = data['dashboards'][0]['id']

# Print the ID of the dashboard
print(f'The ID of the "{dashboard_name}" dashboard is: {dashboard_id}')
