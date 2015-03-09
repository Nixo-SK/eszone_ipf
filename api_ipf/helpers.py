from os import remove
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from eszone_ipf.settings import CONF_DIR

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def get_content(title):
    try:
        with open(''.join([CONF_DIR, title]), 'rb') as f:
            return f.read()
    except Exception as e:
        return e

def file_delete(title):
    try:
        remove(''.join([CONF_DIR, title]))
    except Exception as e:
        print(e)