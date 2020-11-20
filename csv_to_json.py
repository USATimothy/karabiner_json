# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 21:40:30 2019

@author: odin
This script translate a .csv of key remapping instructions into a .json
readable by the Karabiner app.
"""
import csv
import copy
import json

#import csv with json building definition
#See Readme for instructions on builing the .csv file
instruction_file = open('/Users/odin/Documents/keylayout_json_instructions.csv',encoding='utf-8')
instruction_reader = csv.DictReader(instruction_file,delimiter='\t')

#build dictionary from rows of csv
rules = []
idict = {"title":"Tim1","rules":rules}
i=0
for row in instruction_reader:
    i+=1
    description = "from " + row["from"] + " to " + row["to"] +str(i)
    from_dict={"key_code":row["from"]}
    to_dict={"key_code":row["to"]}
    mlist=[]
    olist=[]
    tlist=[]
    for e in row:
        if 'm' in row[e] and not e in ['from','to']:
            mlist.append(e)
        if 'o' in row[e] and not e in ['from','to']:
            olist.append(e)
        if 't' in row[e] and not e in ['from','to']:
            tlist.append(e)
    fmod={}
    if len(mlist)>0:
        fmod["mandatory"]=mlist
    if len(olist)>0:
        fmod["optional"]=olist
    if len(fmod)>0:
        from_dict["modifiers"]=fmod
    if len(tlist)>0:
        to_dict["modifiers"]=tlist
    manipulators = [{"type":"basic","from":from_dict,"to":[to_dict]}]
    rule_dict={"description":description,"manipulators":copy.deepcopy(manipulators)}
    rules.append(copy.deepcopy(rule_dict))

#save to json
    
#Replace odin with your computer username.
with open('/Users/odin/.config/karabiner/assets/complex_modifications/Tim edit.json','w') as json_file:
    json.dump(idict, json_file, indent=2)