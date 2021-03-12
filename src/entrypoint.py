from flask import escape

def entry(request):
    body = main("event", None)

    return escape(body)