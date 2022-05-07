from pypresence import Presence
import time
import requests as request
client_id = 'CLIENT_ID'  # Fake ID, put your real one here
RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop


while True:
    r = request.get('https://api.kognise.dev/')
    r = r.json()['activity']
    print(RPC.update(state="Kognise is " + r['label'], details=r['emoji']))
    time.sleep(15)
