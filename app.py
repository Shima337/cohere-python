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
    return f""" Person name: Maksim
    Place of education: Belarussian Technical University
    Education degree: Bachelor's degree in Economics
    Place of work: Fetti
    Position: Product director
    Responsibilities: Creating product requirements documents, guiding other product leaders, and leading all product initiatives.
    Achievements: Attracted 1,000 users to the new mobile app, expanding the geographical area of interaction.
    Personal biography paragraph: I'm Maksim a Belarussian-born entrepreneur and technology executive who has co-founded and led several successful startups. I have a Bachelor's degree in Economics from Belarusian Technical University and extensive experience in building teams, organizing processes, and project management, including cross-team collaboration. I am passionate about using technology to solve problems and improve people's lives. My latest venture is Fetti, a mobile app for tourists and nomads. I consider myself a gifted leader and problem-solver who has a proven track record of success.
    --
    {data}
    Personal biography paragraph:
    """

@app.route('/dev/test')
def hello_world():
    return  'hello world'


