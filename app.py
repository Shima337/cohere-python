import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from linkedin_scraper import scrap_profile



app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/parse', methods=["POST"])
def parse_linkedin():
    link =  request.json['link']
    print()
    print(link)
    profile = scrap_profile(link)
    print('profile_comback')
    print( profile)
    return profile


@app.route('/gpt', methods=["POST"])
def send_gpt():
    body =  request.json['person_info']
    response= request_gpt(body)
    print(response)
    return {'response': response}


def request_gpt(data):
    response = openai.Completion.create(
            model="text-davinci-002",
            max_tokens = 250,
            top_p = 0.00,
            frequency_penalty = 0,
            presence_penalty = 0,
            prompt=trenings_prompt(data),
            temperature=0.5,
        )
    return response.choices[0].text


def trenings_prompt(data):
    return f""" Compose a personal biography in narrative text:

   Person info: {data}

    Bio:
    """

@app.route('/test')
def hello_world():
    return 