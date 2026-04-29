import requests

def ask_ollama(prompt, system='You are a helpful AI', temp=0.7):
    r = requests.post('http://localhost:11434/api/generate', json={
        'model':'mistral',
        'prompt':prompt,
        'system':system,
        'temperature':temp,
        'stream':False
    })
    return r.json()['response']