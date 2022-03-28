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
keyword=st.text_input('plz give me a keyword')
url= 'https://api.datamuse.com/words?rel_bga=' + keyword + '&max=10'
choice = st.selectbox("What you want to know? ", ("Synonyms", "Antonyms", "Sounds like", "Means like"))
if choice == "Synonyms":
st.write("You selected synonyms of " + keyword)
if choice == "Antonyms" :
st.write("You selected antonyms of " + keyword)
if choice == "Sounds like":
st.write ("You selected sounds like of " + keyword)
if choice == "Means like":
st.write("You selected means like " + keyword)
