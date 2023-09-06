import requests
import json

class GetRequester:

    def __init__(self, url):
        url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        load_json = []
        programs = json.loads(self.get_response_body())
        for program in programs:
            load_json.append(program) 
        return load_json