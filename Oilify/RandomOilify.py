#!/usr/bin/env python


from gimpfu import *
from datetime import date
import random

def RandomOilify(image, drawable):

    mode = random.randint(0, 1)
    mask_size = random.randrange(5,50,1) #
    mask_size_map = random.randrange(3,50,1)
    exponent = random.randrange(1,20,1)
    exponent_map = random.randrange(1,20,1)

    #mask_size = 10 #
    #mask_size_map = 10
    #exponent = 5
    #exponent_map = 5



    #gimp.message('before')
    #pdb.plug_in_oilify_enhanced(image, drawable, mode, mask_size, mask_size_map, exponent, exponent_map)
   # gimp.message('Oilify done')
    pdb.plug_in_oilify(image, drawable, mask_size, 0)

    #gimp.message('unction')
    #The run mode { RUN-INTERACTIVE (0), RUN-NONINTERACTIVE (1) }

      
    

register(
    "python-fu-RandomOilify", #NAME-OF-MAIN-FUNCTION always should correspond to the file name where this main function exits. Change simultaneously in whole scipt
    "applies Oilify (enhanced) filter with random settings",
    "applies Oilify (enhanced) filter with random settings'",
    "Anasasia Romanova", "Anastasia Romanova", "2020",
    "RandomOilify",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        # basic parameters are: (UI_ELEMENT, "variable", "label", Default)
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        
    ],
    [],
    RandomOilify, menu="<Image>/File/Export/ForBIMP/Filters")  # second item is menu location

main()