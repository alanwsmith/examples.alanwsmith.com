#!/usr/bin/env python3

import json
import re 

output_dir = "../../site/json-examples"

source_words = []

skip_words = [
    'abortion', 'male', 'female', 'bombing', 
    'cancer', 'cigarette', 'clan', 'depression', 
    'disability', 'discrimination', 'father', 'mother',
    'girl', 'boy', 'boyfriend', 'girlfriend', 'grandmother',
    'grandfather', 'herself', 'himself', 'his', 'her', 'kill',
    'killing', 'lawsuit', 'marry', 'married', 'minor', 'minority',
    'murder', 'ourselves',  'pregnant', 'pregnancy', 'sex', 'sexual',
    'he', 'she', 'alcohol', 'anger', 'angry', 'anxiety', 'virus',
    'birth', 'prison', 'toilet', 'flesh', 'illegal', 'ethics',
    'rifle', 'funeral', 'lawyer', 'breast',
    ]

with open('source.txt') as _in:
    text_block = _in.read()
    initial_words = text_block.split("\n")
    # filter out words with capitals and dashes
    # and explicit skips
    for word in initial_words:
        if re.search(r'[A-Z]', word):
            continue
        if re.search(r'-', word):
            continue
        if word == "":
            continue
        if word in skip_words:
            continue
        source_words.append(word)

data = {
    "source": "https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/",
    "_note": "Please don't use this as an API. I'm posting these so you can pull them down and work with them that way"
}


with open(f"{output_dir}/english-words--full-set--2hlcotri63ds/data.", "w") as _out:
    data['description'] = "English Words: all lengths"
    data['data'] = source_words
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/english-words--4-letters--2hlcmyrqbg8v/data.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) == 4:
            words.append(word.lower())
    data['description'] = "English Words: 4 letters"
    data['data'] = words
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/english-words--4-or-more-letters--2hlct3fqpkdw/data.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) >= 4:
            words.append(word.lower())
    data['description'] = "English Words: 4 or more letters"
    data['data'] = words
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/english-words--4-5-or-6-letters--2hldesbvshhx/data.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) >= 4 and len(word) <= 6:
            words.append(word.lower())
    data['description'] = "English Words: 4, 5, or 6 letters"
    data['data'] = words
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/english-words--5-letters--2hlcpalckmnz/data.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) == 5:
            words.append(word.lower())
    data['description'] = "English Words: 5 letters"
    data['data'] = words
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/english-words--5-or-more-letters--2hlcv30h2hjp/data.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) >= 5:
            words.append(word.lower())
    data['description'] = "English Words: 5 or more letters"
    data['data'] = words
    json.dump(data, _out, sort_keys=True, indent=2)



with open(f"{output_dir}/english-words--5-6-or-7-letters--2hddgazwinfz/data.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) >= 5 and len(word) <= 7:
            words.append(word.lower())
    data['description'] = "English Words: 5, 6, or 7 letters"
    data['data'] = words
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/english-words--6-letters--2hdhlkihvslr/data.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) >= 6 and len(word) <= 6:
            words.append(word.lower())
    data['description'] = "English Words: 6 letters"
    data['data'] = words
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/english-words--6-or-7-letters--2hdhopsjy4gz/data.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) >= 6 and len(word) <= 7:
            words.append(word.lower())
    data['description'] = "English Words: 6 or 7 letters"
    data['data'] = words
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/english-words--6-7-or-8-letters--2hdib8vr7syk/data.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) >= 6 and len(word) <= 8:
            words.append(word.lower())
    data['description'] = "English Words: 6, 7, or 8 letters"
    data['data'] = words
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/english-words--6-or-more-letters--2hegrr8eflot/data.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) >= 6 and len(word) <= 8:
            words.append(word.lower())
    data['description'] = "English Words: 6 or more letters"
    data['data'] = words
    json.dump(data, _out, sort_keys=True, indent=2)

