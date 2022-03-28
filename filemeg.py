 #! python3
import json,requests
from pprint import pprint

## Access a word-finding query engine
## See API at http://www.datamuse.com/api/

#this library handles the query with the API so we do not need the following steps:
#Step1: Check the API documentation to see if the APIkey is needed. 
#No APIkey needed.


#Step2: Check API documentation to see what structure of URL is needed to access the data?
#For finding rhyming words for the keyword 'funny', the URL looks like this:
#'https://api.datamuse.com/words?rel_rhy=funny'
# make the above URL more generic, so that it is easy to replace the keyword
keyword=input('plz give me a keyword')
url= 'https://api.datamuse.com/words?rel_bga=' + keyword + '&max=10'
#Step3: Download the JSON data from the API.
response = requests.get(url)   
#Uncomment to see the raw JSON text:
#print(response.text)  


#Step4: Load JSON data into a Python variable and use it in your program.
dataFromDatamuse = json.loads(response.text) 
#Uncomment to see the raw JSON text loaded in a Python Variable:
#print(dataFromDatamuse) 
#Uncomment to see a better readable version:
#pprint(dataFromDatamuse) #dont forget to import the correct pprint library to make this work
pprint(dataFromDatamuse[0:4])#if you just want to see the first 9 results
