#!/usr/bin/env python3

from string import Template

def data_builder():
    data = {}
    text = 'Alpha, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu'
    words = text.split(',')
    for i in range(0, len(words)):
        words[i] = f"'{words[i].strip()}'"
        print(words[i])
    data['CODE'] = "[\n    " + ",\n    ".join(words) + "\n]"
    return data

def make_page(template_path, output_path, data):
    with open(template_path) as _template:
        template = Template(_template.read())
        with open(output_path, 'w') as _output:
            _output.write(
                template.substitute(data)
            )

if __name__ == "__main__":
    make_page(
        'src/PAGE.html',
        '../index.html',
        data_builder()
    )

