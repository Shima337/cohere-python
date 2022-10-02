import json
from urllib.parse import urlparse

from linkedin_api import Linkedin  # https://github.com/tomquirk/linkedin-api.git
import os 


#email = os.getenv("LINKEDIN_EMAIL")
#password = os.getenv("LINKEDIN_PASSWORD")

email = "ashsimansk2@gmail.com"
password = "Vv335292168071"

def get_username_from_link(link):
    parse = urlparse(link)
    segments = parse.path.strip('/').split('/')
    in_index = segments.index('in')
    return segments[in_index + 1]


def scrap_profile(profile_link):
    print(email,  password)
    profile_name = get_username_from_link(profile_link)
    api = Linkedin(email, password)
    # GET a profile
    profile = api.get_profile(profile_name)
    skills = api.get_profile_skills(profile_name)

    last_education = profile['education'][0]
    last_experience = profile['experience'][0]
    certifications = profile['certifications']

    degree = []
    for certification in certifications:
        degree.append(
            {k: v for k, v in certification.items() if k in ['name', 'authority', 'timePeriod']}
        )

    scraped = dict(
        first_name=profile.get('firstName'),
        lastName=profile.get('lastName'),
        position=last_experience.get('title'),
        study={k: v for k, v in last_education.items() if
               k in ['schoolName', 'fieldOfStudy', 'degreeName', 'timePeriod']},
        degree=degree,
        company={k: v for k, v in last_experience.items() if
                 k in ['locationName', 'companyName', 'timePeriod']},
        responsibilities=[s['name'] for s in skills if s and len(s) > 0],
        achievements=last_experience.get('description')



    )

    return scraped
