import re


with open('C:\\Users\\david\\Downloads\\pg42671.txt','r'
        ,encoding='utf-8') as f:
    raw_text=f.read()
    filtered_text = re.sub(r'([,.:;?_&$!"()\-\*\']|--|)', '', raw_text)
    tmp=filtered_text.lower()
    