#Assignment

## Table of contents
* [General info](#general-info)
* [Requirements](#requirements)
* [Setup](#setup)

## General info
This project is a simple REST API service. The web app has a button that makes a request to the service and returns a greeting message as response.
	
## Requirements
To build this project without any errors/issues, the following requirements needs to be satisfied
All requirements are in the requirements.txt and listed bellow:
* blinker==1.6.2
* click==8.1.3
* colorama==0.4.6
* Flask==2.3.2
* gunicorn==20.1.0
* importlib-metadata==6.6.0
* itsdangerous==2.1.2
* Jinja2==3.1.2
* MarkupSafe==2.1.2
* Werkzeug==2.3.3
* zipp==3.15.0


	
## Setup
### Run Local
First open your Anaconda Prompt and create your virtual environment using
```
conda create --name env_name python=3.9.13
```
You can replace env_name with the name of your choice and the python version you have.
Then activate your new environment using
```
conda activate env_name
```
Install the dependencies from the requirements text file from the repository.You can use the followng command.
```
pip install -r requirements.txt
```
Once all requirements are met you can navigate to the root folder providing the correct path
```
cd C:\Users\...\assignment
```
Then use the `flask run` command
You should be able to see an output like `* Running on http://localhost:5000`

You can now open your browser and hit the server IP http://localhost:5000 provided to run the demo on your local system.

### Run on Heroku Cloud Application Platform
