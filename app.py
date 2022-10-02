from flask import Flask, redirect, render_template, request, url_for
from flask_cors import CORS
from cohere_api import cohere_generate
from gpt_api import gpt_generate
from linkedin_scraper import scrap_profile

app = Flask(__name__)
CORS(app, resources=r'/dev/*')

@app.route('/dev/parse', methods=["POST"])
def parse_linkedin():
    link =  request.json['link']
    print()
    print(link)
    profile = scrap_profile(link)
    print('profile_comback')
    print( profile)
    return profile

@app.route('/dev/gpt', methods=["POST"])
def send_gpt():
    body = request.json['person_info']
    data = trenings_prompt(body)
    return {'response': gpt_generate(data)}

@app.route('/dev/cohere', methods=["POST"])
def send_cohere():
    body = request.json['person_info']
    data = trenings_prompt(body)
    return {'response': cohere_generate(data)}


def trenings_prompt(data):
    return f""" Compose a personal biography in narrative text:

   Person biography: {data}

    Narrative text min 150 words:
    """

@app.route('/dev/test')
def hello_world():
    return  'hello world'


