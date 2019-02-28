#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs
import random

def read_file(filename):
    IDphoto_tags = {}  # diccionari de ID a tags
    tags_IDphoto = {}  # dciccionari de tags a ID

    IDtagtoString = {}  # diccionari per a traduir ID de tags a el seu nom

    ID = 0  # comptador intern de ID per cada fotos
    IDtags = 0  # comptador intern de IDS per tags de fotos
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


def merge_vertical_in_slide( verticals ):
    double_slides = []
    if len(verticals) >= 2:
        for elem1 in verticals:
            bestScore = 0
            bestPhoto = None
            verticals.remove(elem1)
            for elem2 in verticals:
                score = compare_tags(elem1, elem2)
                if score > bestScore:
                    bestScore = score
                    bestPhoto = elem2
            double_slides += [(str(elem1[0]) + " " + str(bestPhoto[0]), elem1[1] + list(set(bestPhoto[1]) - set(elem1[1])))]
            verticals.remove(bestPhoto)
            if len(verticals) < 2:
                break
    if len(verticals) == 1:
        double_slides += [ ( str( verticals[0][0] ), verticals[0][1] )]
    return double_slides


def compare_tags(photo1, photo2):
    common = len(set(photo1[1]) & set(photo2[1]))
    return len(photo1[1]) + len(photo2[1]) - common


def slides(sl):
    ordered = list()
    rand_int = random.randint(0, len(sl) - 1)
    ordered.append(sl[rand_int])
    sl.remove(ordered[0])
    while len(sl) != 0:
        slide = get_best_slide(sl, ordered[len(ordered) - 1])
        ordered.append(slide)
        sl.remove(slide)
    return ordered


def get_best_slide(sl, to_max):
    punct = -1
    max_slide = to_max
    for slide in sl:
        new_punct = compare_tags(to_max, slide)
        if new_punct > punct:
            max_slide = slide
            punct = new_punct
    return max_slide

def write_results( result, result_file ):
    file = open(result_file, "w")
    file.write( str(len(result)) )
    for elem in result:
        file.write( "\n"+str(elem[0]) )
    file.close()

#files = [ "a_example.txt",  "b_lovely_landscapes.txt",  "c_memorable_moments.txt",  "d_pet_pictures.txt",  "e_shiny_selfies.txt" ]
files = [ "d_pet_pictures.txt" ]

#read_files('a_example.txt')

for file in files:
    verticals, horizontals, tags_dir, traduction_dir = read_file(file)
    print( "file read completed")
    vertical_slides = merge_vertical_in_slide(verticals)
    horizontals += vertical_slides
    print("lists merged")
    result = slides( horizontals )
    write_results( result, "result.out")

