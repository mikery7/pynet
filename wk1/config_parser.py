#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

#with open("cisco_config.txt") as f:
#    config = f.read()

config = CiscoConfParse("cisco_config.txt")

print config

intf = config.find_objects(r"^crypto map CRYPTO")
intfg2 = config.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"group2")
intfna = config.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")

print "*" * 50
print "All Crypto Map Entries:"
print "*" * 50
for i in intf:
    print i.text
    for child in i.all_children:
        print child.text

print "*" * 50
print "Crypto Map Entries Using PFS Group 2 ONLY"
print "*" * 50
for i in intfg2:
    print i.text
    for child in i.all_children:
        print child.text

print "*" * 50
print "Crypto Map Entries NOT Using AES"
print "*" * 50
for i in intfna:
    print i.text
    for child in i.all_children:
        print child.text
