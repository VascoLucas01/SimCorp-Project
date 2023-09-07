#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: Scan a target for possible XSS vulnerabilities.
# Date:        21/08/2023
# Modified by: Sergio Charruadas, Vasco Lucas

# Import libraries

import os
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from dotenv import load_dotenv

# This function is identifying all form type fields on a specific url and returning it to where the function is being called.
def get_all_forms(url,session):
    soup = bs(session.get(url).content, "html.parser")
    return soup.find_all("form")

# This function is retrieving where the data is being sent to and what the method is and saving, finds all <input> tags within the form and parses each one and stores the method, action URL and inputs list in the details dictionary
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# Submits an HTML form given its details and base URL
def submit_form(form_details, url, session, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return session.post(target_url, data=data)
    else:
        return session.get(target_url, params=data)

# Scans a URL for forms with cross-site scripting (XSS) vulnerabilities
def scan_xss(url,session):
    forms = get_all_forms(url,session)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    
    with open("xss_payloads.txt") as f:
        payloads = f.readlines()
        
    successful_payloads = []     
    for js_script in payloads:
        js_script = js_script.strip()  
        for form in forms:
            form_details = get_form_details(form)
            content = submit_form(form_details, url, session, js_script).content.decode() 
            if js_script in content:
                print(f"[+] XSS Detected on {url}")
                print(f"[*] Form details:")
                pprint(form_details)
                is_vulnerable = True
                successful_payloads.append(js_script)
    print("\nSuccessful Payloads: \n")
    for line in successful_payloads:
        print(line)
    return is_vulnerable

# This is just the main function that shows when script is first run asking for the url the user wants to target.
if __name__ == "__main__":

    load_dotenv()

    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    
    URL = "http://10.0.0.175/simcorp/login.php"
    session = requests.session()
    r = session.post(URL, data = {"login": username, "password": password, "security_level": "0", "form": "submit"})
    
    url = input("Enter a URL to test for XSS:")
    scan_xss(url,session)
