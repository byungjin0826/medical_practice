import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files


print(__doc__)

# filename = get_testdata_files('CT_small.dcm')[0]
folder_name = './CT image/siim-medical-images/dicom_dir'
filename = f'{folder_name}/ID_0000_AGE_0060_CONTRAST_1_CT.dcm'
dataset = pydicom.dcmread(filename)

# Normal mode:
print()
print(f"Filename: {filename}")
print(f"Storage type: {dataset.SOPClassUID}")
print()

pat_name = dataset.PatientName
display_name = f"{pat_name.family_name}, {pat_name.given_name}"
print()

if 'PixelData' in dataset:
    rows = int(dataset.Rows)
    cols = int(dataset.Columns)
    print(f"Image size: {rows}, {cols}, {rows*cols} bytes")

    if "PixelSpacing" in dataset:
        print(f"Pixel spacing: {dataset.PixelSpacing}")

plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
plt.show()
