import requests
import json
def ocr_space_file(filename, overlay=False, api_key='eea27ccc0688957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

result = ocr_space_file(filename='Logo.png')
result = json.loads(result)
textDetected = result.get('ParsedResults')[0].get('ParsedText')
print(textDetected)