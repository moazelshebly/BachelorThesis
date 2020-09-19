import os, shutil
import numpy as np
directory = 'Source_Images/'
gt_dir = os.path.join(directory, 'GT_Files')
det_dir = os.path.join(directory, 'Detection_Files')
with open(os.path.join(directory,'detection_results.txt')) as f:
        lines = f.readlines()


for line in lines:
    split_line = line.split()
    file_path = split_line[0]
    bboxes = split_line[1:]
    image_gt_filename = file_path.split('/')[-1].replace('.jpg', '.txt')
    with open(os.path.join(det_dir,image_gt_filename), "w") as f:
        for bbox in bboxes:
            bbox_coordinates = bbox.split(',')[:-1]
            f.write("trash ")
            for item in bbox_coordinates:
                f.write(item + " ")
            f.write('\n')
    f.close()

                
