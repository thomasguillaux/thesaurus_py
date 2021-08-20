import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(str):
    lower_str = str.lower()
    title_str= str.title()
    upper_str = str.upper()
    if lower_str or title_str or upper_str in data:
        return data[str]
    elif len(get_close_matches(str, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(str, data.keys())[0])
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(str, data.keys())[0]]
        elif yn == 'n':
            return "The word doesn't exist. Please double check"
        else:
            return "We didn't understand your query."
    else:
        return"The word doesn't exist. Please double check"

word = input("Enter a word: ")

output = search(word)
if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)
