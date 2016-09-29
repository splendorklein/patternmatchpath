#!/bin/python
import os
import sys
from collections import deque

class Field:

    def __init__(self,currentField):
        self.currentField = currentField
        self.nextFields = {}
        self.isLastField = (False,[])


class Patterns:

    def __init__(self):
        self.start = Field('')

    def buildPattern(self, pattern):
        currentField = self.start
        for field in pattern:
            if field not in currentField.nextFields:
                currentField.nextFields[field] = Field(field)
            currentField = currentField.nextFields[field]
        currentField.isLastField = (True,pattern)

    def matchPattern(self, path):
        currentField = self.start
        stack = deque()
        stack.append([currentField,0])
        match = "NO MATCH"
        while stack:
            pos = stack.pop()
            if pos[1] == len(path) - 1:
                if path[pos[1]] in pos[0].nextFields and pos[0].nextFields[path[pos[1]]].isLastField[0]:
                    match = pos[0].nextFields[path[pos[1]]].isLastField[1]
                    stack = []
                elif "*" in pos[0].nextFields and pos[0].nextFields["*"].isLastField[0]:
                    match = pos[0].nextFields["*"].isLastField[1]
                    stack = []
            else:
                if "*" in pos[0].nextFields:
                    stack.appendleft((pos[0].nextFields["*"],pos[1]+1))
                if path[pos[1]] in pos[0].nextFields:
                    stack.append((pos[0].nextFields[path[pos[1]]],pos[1]+1))
        return match

def patternMatchPaths(_patterns,_paths):

    patterns = Patterns()
    for pattern in _patterns:
        patterns.buildPattern(pattern)
    ans = []
    for path in _paths:
        ans.append(patterns.matchPattern(path))
    
    return ans


input_filename = sys.argv[1]
output_filename = sys.argv[2]

with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    
    _patterns_cnt = 0
    _patterns_cnt = int(input_file.readline())
    _patterns_i=0
    _patterns = []
    while _patterns_i < _patterns_cnt:
        _patterns_item = input_file.readline().split(",")
        _patterns.append(_patterns_item)
        _patterns_i+=1

    _paths_cnt = 0
    _paths_cnt = int(input_file.readline())
    _paths_i=0
    _paths = []
    while _paths_i < _paths_cnt:
        temp = input_file.readline()
        if temp[0] == "/":
            temp = temp[1:]
        if temp[-1] == "/":
            temp = [:len(temp)-1]
        _paths_item = temp.split("/")
        _paths.append(_paths_item)
        _paths_i+=1
        

    res = patternMatchPaths(_patterns,_paths);
    for res_cur in res:
        output_file.write( str(res_cur) + "\n" )





















a = [['*','b','*'],
['a','*','*'], 
['*','*','c'], 
['foo','bar','baz'],
['w','x','*','*'], 
['*','x','y','z'] 
]
b = [['w','x','y','z'] ,
['a','b','c'] ,
['foo'] ,
['foo','bar'] ,
['foo','bar','baz'] ]

print patternMatchPaths(a,b)
