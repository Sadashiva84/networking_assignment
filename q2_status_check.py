"""
    1. Import necessary modules: The script uses requests to send HTTP requests, 
    time for delays, and tabulate for tabular formatting.

    2. Define the subdomains list: Add the subdomains you want 
    to check in this list.

    3. Define the check_status function: It checks the status of a 
    subdomain by sending an HTTP request. Returns 'Up' if successful, 
    'Down' if there's a connection error.

    4. Define the update_table function: It creates a table of 
    subdomains and their statuses using the check_status function.

    5. Main part of the script: Runs an infinite loop to update the 
    table every 60 secs and displays it using tabulate.
"""

import requests
import time
from tabulate import tabulate #it is an already installed library of anaconda

subdomains = ['xyz.zxy', 'google.com', 'yahoo.com']

def check_status(subdomain):
    try:
        response = requests.get(f"http://{subdomain}", timeout=10)
        return 'Up' if response.status_code == 200 else 'Down'
    except requests.ConnectionError:
        return 'Down'

def update_table():
    status_table = []
    for subdomain in subdomains:
        status = check_status(subdomain)
        status_table.append([subdomain, status])
    return status_table

if __name__ == "__main__":
    while True:
        status_table = update_table()
        print(tabulate(status_table, headers=["Subdomain", "Status"], tablefmt="grid"))
        time.sleep(60)