import dicom2jpg

dicom_dir = "/dcm" #insert your directory here
export_location = "/jpg" #insert the directory you want your jpg to be in  
if __name__ == '__main__':
    dicom2jpg.dicom2jpg(dicom_dir, target_root=export_location)  #converts all dicom to jpg and moves to specified export location

