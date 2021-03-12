from flask import escape
from main import main

def entry(request):
    body = main("event", None)

    return escape(body)