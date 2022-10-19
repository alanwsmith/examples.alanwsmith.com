#!/usr/bin/env python3

import json
import re 

output_dir = "../../site/json-english-word-lists"

source_words = []

with open('source.txt') as _in:
    text_block = _in.read()
    initial_words = text_block.split("\n")
    # filter out words with capitals and dashes
    for word in initial_words:
        if re.search(r'[A-Z]', word):
            continue
        if re.search(r'-', word):
            continue
        if word == "":
            continue
        source_words.append(word)


with open(f"{output_dir}/2944-english-words.json", "w") as _out:
    data = {
        "description": "2944 words, all lowercase, from the 3000 most common English with words with capital and dashes removed",
        "source": "https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/",
        "words": source_words,
    }
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/2746-english-words--4-plus-characters.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) > 3:
            words.append(word.lower())
    data = {
        "description": "2746 words, all lower case, from the 3000 most common English words filtered to words with four or more characters",
        "source": "https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/",
        "words": words,
    }
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/500-english-words--4-characters-exactly.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) == 4:
            words.append(word.lower())
    data = {
        "description": "500 words, all lowercase, from the 3000 most common English words filtered to words with exactly four characters",
        "source": "https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/",
        "words": words,
    }
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/2246-english-words--5-plus-characters.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) > 4:
            words.append(word.lower())
    data = {
        "description": "2246 words, all lower case, from the 3000 most common English words filtered to words with five or more characters",
        "source": "https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/",
        "words": words,
    }
    json.dump(data, _out, sort_keys=True, indent=2)



with open(f"{output_dir}/478-english-words--5-characters-exactly.json", "w") as _out:
    words = []
    for word in source_words:
        if len(word) == 5:
            words.append(word.lower())
    data = {
        "description": "478 words, all lowercase, from the 3000 most common English words filtered to words with exactly five characters",
        "source": "https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/",
        "words": words,
    }
    json.dump(data, _out, sort_keys=True, indent=2)

