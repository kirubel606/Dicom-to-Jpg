import os
import pydicom
import numpy as np
from PIL import Image, ImageFilter
import shutil

def convert_dicom_to_jpg(input_filename, output_dir, quality=90):
    # Read the DICOM file
    ds = pydicom.dcmread(input_filename)

    # Extract the pixel array and convert to uint16
    img = ds.pixel_array
    img = img.astype('uint16')

    # Check if RescaleIntercept attribute is present
    if hasattr(ds, 'RescaleIntercept'):
        intercept = ds.RescaleIntercept
    else:
        intercept = 0.0

    # Check if RescaleSlope attribute is present
    if hasattr(ds, 'RescaleSlope'):
        slope = ds.RescaleSlope
    else:
        slope = 1.0

    # Rescale pixel values
    img = (img * slope + intercept).astype('float32')

    # Apply windowing
    window_center = ds.WindowCenter
    window_width = ds.WindowWidth
    img_min = window_center - (window_width / 2.0)
    img_max = window_center + (window_width / 2.0)
    img = np.clip(img, img_min, img_max)
    img = (img - img_min) / (img_max - img_min)
    img = (img * 255).astype('uint8')

    # Create PIL Image object and save as JPEG
    im = Image.fromarray(img)
    output_filename = os.path.splitext(os.path.basename(input_filename))[0] + ".jpg"
    output_filepath = os.path.join(output_dir, output_filename)
    im.save(output_filepath, quality=quality)

    # Apply median filter to reduce noise
    im = Image.open(output_filepath)
    im = im.filter(ImageFilter.MedianFilter(size=3))
    im.save(output_filepath, quality=quality)

def convert_directory(input_dir, output_dir, quality=90):
    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        full_filepath = os.path.join(input_dir, filename)
        if os.path.isdir(full_filepath):
            # Recursively call the function for subdirectories
            sub_output_dir = os.path.join(output_dir, filename)
            os.makedirs(sub_output_dir, exist_ok=True)
            convert_directory(full_filepath, sub_output_dir, quality=quality)
        elif filename.endswith(".dcm"):
            # Convert DICOM file to JPEG and save in output directory
            convert_dicom_to_jpg(full_filepath, output_dir, quality=quality)
        else:
            # Copy non-DICOM files to output directory
            output_filepath = os.path.join(output_dir, filename)
            shutil.copy(full_filepath, output_filepath)

# Example usage
input_dir = r"/path"  #insert path to directory that contains DICOM images
output_dir = r"/path"  #insert path where you want the JPG to be placed in if you want it in the same folder use the exact path on input_dir
quality = 90
convert_directory(input_dir, output_dir, quality=quality)
