#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas
import numpy as np
import codecs


ID_tags = {}
tags_ID = {}
IDtagtoString = {}
ID = 1

with codecs.open('a_example.txt', encoding='utf-8', mode='r') as fileref:

    NPhotos = int(fileref.readline())
    for line in fileref.readlines():
        line = line.splitlines()[0]
        fields = line.split(' ')
        orientation = fields.pop(0)
        Ntags = fields.pop(0)
        print(Ntags)""

        tags = []
        for i in fields:
            tags.append(i)

        ID_tags[ID] = [orientation, tags]

        for i in tags:
            if i not in tags_ID.keys():
                tags_ID[i] = [ID]
            else:
                tags_ID[i].append(ID)

        ID += 1
    print(ID_tags)
    print(tags_ID)
