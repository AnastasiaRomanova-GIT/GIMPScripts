#!/usr/bin/env python


from gimpfu import *
from datetime import date
import random

def RandomCartoon(image, drawable):

    
    mask_radius = random.randrange(1,50,1) #Cartoon mask radius (radius of pixel neighborhood) [1:50]    
    pct_black = random.randrange(3,10,1)/10 #Percentage of darkened pixels to set to black (0.0 - 1.0)
    
    image = pdb.script_fu_predator(image, drawable, value, toggle, value, toggle, toggle)
    
    

register(
    "python-fu-RandomCartoon", #NAME-OF-MAIN-FUNCTION always should correspond to the file name where this main function exits. Change simultaneously in whole scipt
    "applies cubist filter with random settings",
    "applies cubist filter with random settings'",
    "Anasasia Romanova", "Anastasia Romanova", "2020",
    "RandomCartoon",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        # basic parameters are: (UI_ELEMENT, "variable", "label", Default)
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        #(PF_STRING, "filename_input", "File Name", ".jpeg"),
        #(PF_TEXT, "description", "Description", "Put description here"),
        #(PF_DIRNAME, "directory", "Working Directory", "D:/Anastasia/Documents/StockBusiness/ShutterstockPatterns"),
        #(PF_SLIDER, "quality", "Quality", 1, (0, 1, 0.2)),
        #(PF_SLIDER, "smoothing", "Smoothing", 1, (0, 1, 0.2)),
        #(PF_TOGGLE, "optimize", "Optimize", 1),
        #(PF_TOGGLE, "progressive", "Progressive", 1),
        #(PF_TEXT, "comment", "Comment", "Anastasia Romanova (c)")

        #(PF_SLIDER, "amount", _("Amount"), 5.0, (0, 1, 0.05) #- something is wrong here
        # PF_SLIDER, SPINNER have an extra tuple (min, max, step)
        # PF_RADIO has an extra tuples within a tuple:
        # eg. (("radio_label", "radio_value), ...) for as many radio buttons
        # PF_OPTION has an extra tuple containing options in drop-down list
        # eg. ("opt1", "opt2", ...) for as many options
        # see ui_examples_1.py and ui_examples_2.py for live examples
    ],
    [],
    RandomCartoon, menu="<Image>/File/Export/ForBIMP/Filters")  # second item is menu location

main()