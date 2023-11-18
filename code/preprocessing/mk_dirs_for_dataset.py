import os

# creates sub-directories into the Dataset directory

dirs = []
dataset_dir = 'C:/Users/exam18/Desktop/Home_Automation_using_GestureRecognition-main/Dataset'
gestures_file = 'C:/Users/exam18/Desktop/Home_Automation_using_GestureRecognition-main/preprocessing/gestures.txt'
all_dataset_dirs_file = 'C:/Users/exam18/Desktop/Home_Automation_using_GestureRecognition-main/preprocessing/all_dataset_dirs.txt'

if not os.path.isdir(dataset_dir):
    os.mkdir(dataset_dir)


#with open(f'./{os.path.dirname(__file__)}/{gestures_file}', 'r') as f:
with open(gestures_file, 'r') as f:
    for line in f:
        line = line.strip()

        imagesf = f'{dataset_dir}/{line}'

        if not os.path.isdir(imagesf):
            os.mkdir(imagesf)

        dirs.append(imagesf)


# write the created sub-directories into a text file
count = 0
#with open(f'./{os.path.dirname(__file__)}/{all_dataset_dirs_file}', 'w+') as f:
with open(all_dataset_dirs_file, 'w+') as f:

    for d in dirs:
        f.write(f"{d}\n")
