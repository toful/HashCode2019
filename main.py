#!/usr/bin/python3
# -*- coding: utf-8 -*-


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
