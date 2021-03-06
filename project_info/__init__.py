from django.conf import settings
import json
import os.path


def get_project_info(req):
    pip = {}
    if os.path.isfile(settings.PIP_CONFIG):
        json_data = open(settings.PIP_CONFIG)
        pip = json.load(json_data)
        json_data.close()
    return dict(('PROJECT_' + k.upper(), v) for k, v in pip.items())
