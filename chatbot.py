# rewrite the bleow 
import os
import google.generativeai as palm
from halo import Halo

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.4,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
}

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
        response = palm.generate_text(prompt=input_msg, **defaults)
        print(response.result)
        if not response.result:
            print("CLAI> Sorry, I couldn't fetch a response for that.")
            continue
    else:
        print(response.last)
        continue