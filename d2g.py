import dicom2jpg

dicom_dir = "dcm"
export_location = "jpg"
if __name__ == '__main__':
    dicom2jpg.dicom2jpg(dicom_dir, target_root=export_location)  

