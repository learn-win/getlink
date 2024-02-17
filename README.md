# getlink v1.0    
We can easily find the download link for any topic using Google's custom search engine, which may help reduce time. We can get the file in any format, such as pdf, PowerPoint, or Excel.  

## Requirements
Python 3, requests    
'''
Install the Python3 from the (python.org)
pip install requests
'''

## How to install Python

Download Python Installer:
Visit the official Python website at python.org and click on the "Downloads" tab. Choose the latest version for your operating system (e.g., Windows) and select the installer that matches your system architecture (32-bit or 64-bit).

Run Installer:
Run the downloaded installer. Make sure to check the box that says "Add Python to PATH" during installation. This will make it easier to run Python from the command line.

Install Python:
Follow the on-screen instructions to complete the installation.

Verify Installation:
Open a command prompt and type python --version or python -V to verify that Python is installed. You should see the installed version.

## Installation of requests

    pip install -r requirements.txt
    pip install requests

## How to get the Google Custom Search Engine

You need to replace the GOOGLE SEREACH API -> "Replace-Your-Google-Search-Api"

                                    STEPS TO CREATE THE GOOGLE SEARCH API 

Create a Custom Search Engine (CSE):
Go to the Google Custom Search website.
Click on the "Create a custom search engine" button.
Follow the steps to set up your custom search engine.

Get API Key:
Once you have set up your custom search engine, go to the Google Cloud Console.
Create a new project if you don't have one.
Enable the "Custom Search JSON API" for your project.
Create an API key in the "APIs & Services" > "Credentials" section.

Use the API:
You can then use the API key to make requests to the Custom Search API endpoint. The base URL is usually https://www.googleapis.com/customsearch/v1.
Include your API key in the request.

### Windows/linux/termux

    python3 getlink.py

## Sample Execution 

------------------------
python3 getlink.py
Search value: nodejs
File format: pdf
------------------------
python3 getlink.py
Search value: networking
File format: ppt
------------------------

## Refernal links for get the search api
## https://www.youtube.com/watch?v=b9G3DkCJCEg
### About

<p>Coded by: Ardhanarieswarar A</p>
<p>Follow Github : https://github.com/learn-win/</p>




