#!/usr/bin/env python


from gimpfu import *
from datetime import date
import random

def RandomMosaic(image, drawable):

    col1 = random.randrange(1,255,1)
    col2 = random.randrange(1,255,1)
    col3 = random.randrange(1,255,1)
    gimp.set_background(col1, col2, col3)
    gimp.set_foreground(col1, col2, col3)

    tile_size = random.randrange(5,100,1) #Average diameter of each tile (in pixels) (1 <= tile-size <= 1000) 
    tile_height = random.randrange(5,200,1) #Apparent height of each tile (in pixels) (1 <= tile-height <= 1000)
    tile_spacing = random.randrange(1,25,1) #Inter_tile spacing (in pixels) (0.1 <= tile-spacing <= 1000)
    tile_neatness =  random.randrange(1,10,1)/10 #Deviation from perfectly formed tiles (0 <= tile-neatness <= 1)
    tile_allow_split = random.randint(0, 1) #INT Allows splitting tiles at hard edges (0 <= tile-allow-split <= 1)
    light_dir = random.randrange(1,360,1) #Direction of light_source (in degrees) (0 <= light-dir <= 360)
    color_variation = random.randrange(1,10,1)/10 #Magnitude of random color variations (0 <= color-variation <= 1)
    antialiasing = random.randint(0, 1) # INT Enables smoother tile output at the cost of speed (0 <= antialiasing <= 1)
    color_averaging = 1 # INT Tile color based on average of subsumed pixels (0 <= color-averaging <= 1)
    tile_type = random.randint(0, 3)#INT Tile geometry { SQUARES (0), HEXAGONS (1), OCTAGONS (2), TRIANGLES (3) } (0 <= tile-type <= 3)
    tile_surface = random.randint(0, 1) #INT Surface characteristics { SMOOTH (0), ROUGH (1) } (0 <= tile-surface <= 1)
    grout_color = random.randint(0, 1) #INT Grout color (black/white or fore/background) { BW (0), FG-BG (1) } (0 <= grout-color <= 1)
    
    image = pdb.plug_in_mosaic(image, drawable, tile_size, tile_height, tile_spacing, tile_neatness, tile_allow_split, light_dir, color_variation, antialiasing, color_averaging, tile_type, tile_surface, grout_color)
    
    

register(
    "python-fu-RandomMosaic", #NAME-OF-MAIN-FUNCTION always should correspond to the file name where this main function exits. Change simultaneously in whole scipt
    "applies Mosaic filter with random settings",
    "applies Mosaic filter with random settings'",
    "Anasasia Romanova", "Anastasia Romanova", "2020",
    "RandomMosaic",
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
    RandomMosaic, menu="<Image>/File/Export/ForBIMP/Filters")  # second item is menu location

main()