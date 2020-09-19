import os

directory = 'Source_Images/'

gt_files = os.listdir(os.path.join(directory, 'GT_Files'))
det_files = os.listdir(os.path.join(directory, 'Detection_Files'))

for gtf in gt_files:
    if gtf not in det_files:
        f = open(os.path.join(directory,"Detection_Files",gtf), "w")
        f.close()
