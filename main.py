#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas
import numpy as np
import codecs


IDphoto_tags = {}  # diccionari de ID a tags
tags_IDphoto = {}  # dciccionari de tags a ID

IDtagtoString = {}  # diccionari per a traduir ID de tags a el seu nom

ID = 1  # comptador intern de ID per cada fotos
IDtags = 1  # comptador intern de IDS per tags de fotos
IDtagslist = []  # llista temporal de IDs de tags


with codecs.open('a_example.txt', encoding='utf-8', mode='r') as fileref:

    NPhotos = int(fileref.readline())  # nombre de fotos a llegir

    for line in fileref.readlines():
        IDtagslist = []

        line = line.splitlines()[0]
        fields = line.split(' ')  # obte llista de paraules
        orientation = fields.pop(0)
        Ntags = fields.pop(0)

        tags = []  # llista de tags en versio string
        for i in fields:
            tags.append(i)

        # traduccio de tag string a ID
        for i in tags:
            if i not in IDtagtoString.values():  # si un dels tags no esta registrat creem ID i registrem
                IDtagtoString[IDtags] = i
                IDtagslist.append(IDtags)
                IDtags += 1

            else:  # si esta registrat busquem la seva ID corresponent i lafegim a la llista
                for j in IDtagtoString.keys():
                    if IDtagtoString[j].__eq__(i):
                        IDtagslist.append(j)

        IDphoto_tags[ID] = [orientation, IDtagslist]  # afegim orientacio i lllista de ID tags al diccionari

        for i in IDtagslist:
            if i not in tags_IDphoto.keys():
                tags_IDphoto[i] = [ID]
            else:
                tags_IDphoto[i].append(ID)

        ID += 1
    print(IDphoto_tags)
    print(tags_IDphoto)
