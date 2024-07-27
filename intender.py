import urllib
import requests
import json
from dataclasses import dataclass

ENDPOINT= "https://intend.do/api/v0/"
AUTH_TOKEN= "744ae19bedf1829d4b23"

@dataclass
class Intention:
    body: str
    goals: list[int] = [] 

    def raw(self) -> str:
        prefix = ','.join(map(str, self.goals)) if self.goals else '@'
        return '{}) {}'.format(prefix, self.body)


def mk_url(path):
    params = {'auth_token': AUTH_TOKEN}
    url =ENDPOINT + path + "?" + urllib.parse.urlencode(params) 
    print(url)
    return url

def full():
    return json.loads(requests.get(mk_url('u/me/today/full.json')).content)

def intention_dict(full):
    return {g['zid']: g['text'] for g in full['core']['list']}

def add_intention(intention):

    intentions = intention_dict(full())
    message = {'raw': intention.raw(), 'response': 'today'}
    response = requests.post(mk_url('u/me/intentions'), json=message)
    new_full = json.loads(response.content)

    new_intentions = intention_dict(new_full)
    new_zid = new_intentions.keys() - intentions.keys()
    return new_zid
