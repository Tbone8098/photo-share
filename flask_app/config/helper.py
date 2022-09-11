from functools import wraps
from flask import redirect, session, json
import random
import requests
import base64
import os

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'uuid' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

def generate_code(length):
    options = [
        ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
        ["1","2","3","4","5","6","7","8","9","0"],
        ["!","@","#","$","%","^","&"],
    ]
    code = ""
    for indx in range(length):
        option = options[random.randint(0, len(options) - 1)]
        char = option[random.randint(0, len(option) - 1)]
        code += char
    return code

def upload_photo(file):
    base64_file = base64.b64encode(file.read())
    url = "https://api.imgbb.com/1/upload"
    payload = {
        'key': os.environ.get("IMGBB_KEY"),
        'image': base64_file
    }
    resp = requests.post(url, payload)
    resp = resp.json()
    return resp['data']['url']
