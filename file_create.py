#!/usr/bin/env python

import json
import yaml

my_list = []

for i in range(10):
    my_list.append(i)

my_list.append('a string')
my_list.append({})

my_list[-1]['ip_addr'] = '10.10.1.100'
my_list[-1]['ip_sub'] = '255.255.255.0'
my_list[-1]['ip_gw'] = '10.10.1.1'

print 'In YAML:'
print yaml.dump(my_list, default_flow_style=False)

print 'In JSON:'
print json.dumps(my_list)

with open("my_list.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

with open("my_list.json", "w") as f:
    json.dump(my_list, f)
