#!/usr/bin/env python3

import os
import glob
import sys
import json
 
from string import Template

class Builder():

    def __init__(self):
        self.script_dir = sys.path[0]
        self.content_root = f"{self.script_dir}/../site/json-examples"
        self.content_dirs = [ 
            dir for dir in glob.glob(f"{self.content_root}/*")
            if os.path.isdir(dir)
        ]
        self.template_path = f"{self.script_dir}/src/home_page.html"
        self.output_path = f"{self.script_dir}/../site/index.html"
        self.data = { "JSON_LINKS": "here"}

    def build_file(self):
        with open(self.template_path) as _template:
            with open(self.output_path, 'w') as _out:
                frame = Template(_template.read())
                _out.write(frame.substitute(self.data))

    def get_json_links(self):
        links = []
        for content_dir in self.content_dirs:
            data_path = f"{content_dir}/data.json"
            if os.path.isfile(data_path):
                with open(data_path) as _data:
                    data = json.load(_data)
                    path = data_path.split("site/")[1]
                    print(data_path)
                    print(data['description'])
                    links.append(f'''<li><a href="{path}">{data['description']}</a></li>''')


        links.sort()
        self.data["JSON_LINKS"] = "".join(links)




if __name__ == "__main__":
    b = Builder()
    b.get_json_links()
    b.build_file()
