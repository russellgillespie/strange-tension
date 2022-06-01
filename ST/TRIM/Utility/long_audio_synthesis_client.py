import json
import ntpath
import requests

def get_voices():
    region = '<region>'
    key = '<your_key>'
    url = 'https://{}.customvoice.api.speech.microsoft.com/api/texttospeech/v3.0/longaudiosynthesis/voices'.format(region)
    header = {
        'Ocp-Apim-Subscription-Key': key
    }

    response = requests.get(url, headers=header)
    print(response.text)

get_voices()

# sample output:
# {
#   "values": [
#     {
#       "locale": "en-US",
#       "voiceName": "en-US-AriaNeural",
#       "description": "",
#       "gender": "Female",
#       "createdDateTime": "2020-05-21T05:57:39.123Z",
#       "properties": {
#         "publicAvailable": true
#       }
#     },
#     {
#       "id": "8fafd8cd-5f95-4a27-a0ce-59260f873141"
#       "locale": "en-US",
#       "voiceName": "my custom neural voice",
#       "description": "",
#       "gender": "Male",
#       "createdDateTime": "2020-05-21T05:25:40.243Z",
#       "properties": {
#         "publicAvailable": false
#       }
#     }
#   ]
#

def submit_synthesis():
    region = '<region>'
    key = '<your_key>'
    input_file_path = '<input_file_path>'
    locale = '<locale>'
    url = 'https://{}.customvoice.api.speech.microsoft.com/api/texttospeech/v3.0/longaudiosynthesis'.format(region)
    header = {
        'Ocp-Apim-Subscription-Key': key
    }

    voice_identities = [
        {
            'voicename': '<voice_name>'
        }
    ]

    payload = {
        'displayname': 'long audio synthesis sample',
        'description': 'sample description',
        'locale': locale,
        'voices': json.dumps(voice_identities),
        'outputformat': 'riff-16khz-16bit-mono-pcm',
        'concatenateresult': True,
    }

    filename = ntpath.basename(input_file_path)
    files = {
        'script': (filename, open(input_file_path, 'rb'), 'text/plain')
    }

    response = requests.post(url, payload, headers=header, files=files)
    print('response.status_code: %d' % response.status_code)
    print(response.headers['Location'])

submit_synthesis()

voice_identities = [
    {
        'id': '<voice_id>'
    }
]
