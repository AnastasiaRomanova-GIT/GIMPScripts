#!/usr/bin/env python

# Import required modules
from gimpfu import *
import random 
import time
import shutil
import os

# Define the main function for the GIMP plug-in
def Batch_CubistEffectOnFiles(image, drawable, WorkingDirectory, quality, smoothing, optimize, progressive, comment):
    # Create a directory for processed files
    CubicDirectory = WorkingDirectory+'/CubicProcessedFiles'
    if os.path.exists(CubicDirectory):
        shutil.rmtree(CubicDirectory)
    os.mkdir(CubicDirectory)

    # List to store image file paths and names
    ImageFilesList = []
    FileNameList = []
    # Traverse the working directory and add file paths and names to the lists
    for r, d, f in os.walk(WorkingDirectory): 
        for file in f:
            ImageFilesList.append(os.path.join(r, file))
            FileNameList.append(file)
    
    # Load the first image in the list as a layer
    NNPictureLayer = pdb.gimp_file_load_layer(image, ImageFilesList[0])
    pdb.gimp_image_insert_layer(image, NNPictureLayer, None, 0)

    # JPEG saving options
    baseline = 1
    subsmp = 2 # Sub-sampling type
    restart = 8 # Interval of restart markers
    dct = 2 # DCT method

    # Process each file in the list
    for f in ImageFilesList:
        NNPicture = pdb.file_jpeg_load(f, f)
        CubicFilename = CubicDirectory + str(f)
        pdb.file_jpeg_save(image, drawable, CubicFilename, CubicFilename, quality, smoothing, optimize, progressive, comment, subsmp, baseline, restart, dct)

    # Additional processing could be added here

# Register the plug-in within GIMP
register(
    "python-fu-Batch_Batch_CubistEffectOnFiles",
    "Applies cubist effect to files",
    "Applies artistic cubist effect with all random characteristics to all files in a folder",
    "Anastasia Romanova", "Anastasia Romanova", "2020",
    "Batch_CubistEffectOnFiles",
    "",
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        (PF_DIRNAME, "WorkingDirectory", "Working Directory", "D:/Anastasia/Documents/StockBusiness/ShutterstockPatterns"), 
        (PF_SLIDER, "quality", "Quality", 1, (0, 1, 0.2)),
        (PF_SLIDER, "smoothing", "Smoothing", 1, (0, 1, 0.2)),
        (PF_TOGGLE, "optimize", "Optimize", 1),
        (PF_TOGGLE, "progressive", "Progressive", 1),
        (PF_TEXT, "comment", "Comment", "Anastasia Romanova (c)")
    ],
    [],
    Batch_CubistEffectOnFiles, menu="<Image>/Filters/")

# Start the plug-in
main()
