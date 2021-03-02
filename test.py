import requests

url = "https://viettelgroup.ai/voice/api/asr/v1/rest/decode_file"
headers = {
    'token': 'anonymous',
    #'sample_rate': 16000,
    #'format':'S16LE',
    #'num_of_channels':1,
    #'asr_model': 'model code'
}
s = requests.Session()
files = {'file': open($AUDIO_PATH,'rb')}
response = requests.post(url,files=files, headers=headers, verify=$CERT_PATH)

print(response.text)