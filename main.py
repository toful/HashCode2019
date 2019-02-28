#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd
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
    print(IDtagtoString)

def merge_vertical_in_slide( verticals ):
    double_slides = []
    for elem1 in verticals:
        bestScore = 0
        bestPhoto = None
        verticals.remove(elem1)
        for elem2 in verticals:
            score = compare_tags(elem1, elem2)
            if (score > bestScore):
                bestScore = score
                bestPhoto = elem2
        double_slides += [(str(elem1[0]) + " " + str(bestPhoto[0]), elem1[1] + list(set(bestPhoto[1]) - set(elem1[1])))]
        verticals.remove(bestPhoto)
        if len(verticals) < 2:
            break


def compare_tags(photo1, photo2):
    common = len(set(photo1[1]) & set(photo2[1]))
    return len(photo1[1]) + len(photo2[1]) - common


def slides(sl):
    ordered = list()
    ordered.append(sl[0])
    sl.remove(ordered[0])
    while len(sl) != 0:
        slide = get_best_slide(sl, ordered[len(ordered) - 1])
        ordered.append(slide)
        sl.remove(slide)
    return ordered


def get_best_slide(sl, to_max):
    punct = -1
    for slide in sl:
        new_punct = compare_tags(to_max, slide)
        if new_punct > punct:
            max_slide = slide
            punct = new_punct
    return max_slide


sli = [(0, [1, 2, 3]), (1, [2, 3, 4]), (2, [1, 3, 5])]
print(slides(sli))
