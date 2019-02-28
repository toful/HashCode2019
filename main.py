#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

print("Hello World")

def merge_vertical_in_slide( verticals ):
    double_slides = []
    for elem1 in verticals:
        bestScore=0
        bestPhoto= None
        verticals.remove( elem1 )
        for elem2 in verticals:
            score = compare_tags( elem1, elem2 )
            if( score > bestScore ):
                bestScore = score
                bestPhoto = elem2
        double_slides += [ ( str( elem1[0]) +" "+ str( bestPhoto[0]) , elem1[1] + list(set(bestPhoto[1]) - set(elem1[1])) ) ]
        verticals.remove( bestPhoto )
        if( len(verticals) < 2 ):
            break



def compare_tags( photo1, photo2 ):
    common = len( set( photo1[1], photo2[1] ) )
    return len(photo1[1]) + len(photo2[1]) - common
