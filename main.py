#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs


def read_files(filename):
    IDphoto_tags = {}  # diccionari de ID a tags
    tags_IDphoto = {}  # dciccionari de tags a ID

    IDtagtoString = {}  # diccionari per a traduir ID de tags a el seu nom

    ID = 1  # comptador intern de ID per cada fotos
    IDtags = 1  # comptador intern de IDS per tags de fotos
    IDtagslist = []  # llista temporal de IDs de tags

    with codecs.open(filename, encoding='utf-8', mode='r') as fileref:

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

        Horizontal_list = []
        Vertical_list = []
        for i in IDphoto_tags.keys():
            if IDphoto_tags[i][0].__eq__('H'):
                Horizontal_list.append([i, IDphoto_tags[i][1]])
            else:
                Vertical_list.append([i, IDphoto_tags[i][1]])

        return Vertical_list, Horizontal_list, tags_IDphoto, IDtagtoString

        # print(IDphoto_tags)
        # print(tags_IDphoto)
        # print(IDtagtoString)


def merge_vertical_in_slide(verticals):
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
        if (len(verticals) < 2):
            break


def compare_tags(photo1, photo2):
    common = len(set(photo1[1], photo2[1]))
    return len(photo1[1]) + len(photo2[1]) - common


print("Hello World")
read_files('a_example.txt')
