#!/usr/bin/env python

import yaml
import json
from pprint import pprint as pp

with open ("my_list.json") as f:
    new_jlist = json.load(f)

with open ("my_list.yml") as f:
    new_ylist = yaml.load(f)

print '*' * 25
print 'Pretty print list in JSON:'
print '*' * 25
pp(new_jlist)
print '*' * 25
print 'Pretty print list in YAML:'
print '*' * 25
pp(new_ylist)
