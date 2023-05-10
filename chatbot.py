import os
import google.generativeai as palm
from halo import Halo

palm.configure(api_key=os.environ['PALM_API_KEY'])

while True:
    print("CLAI> ", end='')
    input_msg = input()
    if not input_msg:
        continue
    spinner = Halo(text='Processing...', spinner='dots')
    spinner.start()
    response = palm.chat(messages=input_msg)
    spinner.stop()
    if not response.last:
        print("CLAI> Sorry, I couldn't fetch a response for that.")
        continue
    print(response.last + "\n")