#!/usr/bin/env python3

import json

output_dir = "../../site/english-word-lists"

with open('source.txt') as _in:
    text_block = _in.read()
    source_words = text_block.split("\n")

with open(f"{output_dir}/3000-with-capitals.json", "w") as _out:
    data = {
        "description": "3000 of the most common English words in Capital Case where appropriate",
        "source": "https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/",
        "words": source_words,
    }
    json.dump(data, _out, sort_keys=True, indent=2)


with open(f"{output_dir}/3000-lower-case.json", "w") as _out:
    words = []
    for word in source_words:
        words.append(word.lower())
    data = {
        "description": "3000 of the most common English words lower cased",
        "source": "https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/",
        "words": words,
    }
    json.dump(data, _out, sort_keys=True, indent=2)




