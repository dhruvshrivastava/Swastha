from easy_entrez import EntrezAPI
import requests 
import xml.etree.ElementTree as ET
import urllib.request
import re
import os 
import openai
import json
import re
from fastapi import FastAPI

app = FastAPI()

@app.post("/api")
def result(query: str):
    text = get_result(query)
    return text


openai.api_key = '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'


def get_uid(query):
    '''
    Takes in search query and returns a list of UIDs from PubMed
    '''
    entrez_api = EntrezAPI(
        'pubmed',
        'dhruvsri5@gmail.com',
        return_type = 'json'
    )
    result = entrez_api.search(query, max_results=7)
    return result.data['esearchresult']['idlist']


def full_text(uids):
    '''
    Takes in list of PubMed UIDs and returns combined full-text
    '''
    combined_text = ''
    for uid in uids: 
        url = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/BioConcept/{0}/PubTator/".format(uid)
        r = urllib.request.urlopen(url)
        text = str(r.read(), "UTF-8")
        combined_text += text
    print(combined_text)


def get_result(query):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=query,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    response = json.loads(str(response))
    response = response["choices"][0]["text"]
    return response

