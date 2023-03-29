

# DICOM to JPEG Converter
This is a Python script that converts DICOM files to JPEG files using the Pydicom and Pillow libraries. The script also applies windowing and a median filter to reduce noise. The converted files are saved to an output directory, which can be specified by the user.

## Prerequisites
1. Python 3.x
2. Pydicom
3. Pillow
## Installation
1. Clone the repository or download the zip file.
2. Install the Pydicom and Pillow libraries using: 
> **pip install pydicom Pillow**

## Usage
Open the command prompt or terminal.

Navigate to the directory where the **dicom** file is located.

Run the following command:
```
python D2J.py 

```
4. Press Enter to run the command.

5. The script will convert all DICOM files in the input directory and its subdirectories to JPEG files and save them in the output directory. Non-DICOM files in the input directory and its subdirectories will be copied to the output directory.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
