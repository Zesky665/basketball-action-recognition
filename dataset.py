import json
import shutil
import os
import itertools
from augment_videos import augmentVideo

def setup_training_data(annotation_dict_path, labels_dict_path, video_archive_path):
    
    training_data_path = "dataset/training_data/"
    if not os.path.exists(training_data_path):
        os.mkdir(training_data_path)
    
    with open(annotation_dict_path) as f:
        annotation_dict = json.load(f)
    
    with open(labels_dict_path) as f:
        labels_dict = json.load(f)
        
    n = len(annotation_dict) 
    m = round(n * 0.8)
    i = iter(annotation_dict.items())

    train = dict(itertools.islice(i, m))
    val_test = dict(i)
    
    for i, annotation in enumerate(train):
        annotation_str = str(annotation)
        video_name = f'{annotation_str}.mp4'
        video_class = str(annotation_dict[annotation])
        
        train_data_path = os.path.join(training_data_path, 'train')
        if not os.path.exists(train_data_path):
            os.mkdir(train_data_path)
        data_class_path = os.path.join(train_data_path, video_class)
        if not os.path.exists(data_class_path):
            os.mkdir(data_class_path)
                        
        video_origin_path = os.path.join(video_archive_path, video_name)
        video_target_path = os.path.join(data_class_path, video_name)
        if not os.path.exists(video_target_path):
            shutil.copy(video_origin_path, data_class_path)
        
    for i, annotation in enumerate(val_test):
        annotation_str = str(annotation)
        video_name = f'{annotation_str}.mp4'
        video_class = str(annotation_dict[annotation])
        
        if(i%2!=0):
            val_data_path = os.path.join(training_data_path, 'val')
            if not os.path.exists(val_data_path):
                    os.mkdir(val_data_path)
            data_class_path = os.path.join(val_data_path, video_class)
            if not os.path.exists(data_class_path):
                    os.mkdir(data_class_path)
                        
            video_origin_path = os.path.join(video_archive_path, video_name)
            video_target_path = os.path.join(data_class_path, video_name)
            if not os.path.exists(video_target_path):
                    shutil.copy(video_origin_path, data_class_path)
        else:

            test_data_path = os.path.join(training_data_path, 'test')
            if not os.path.exists(test_data_path):
                    os.mkdir(test_data_path)
            data_class_path = os.path.join(test_data_path, video_class)
                
            if not os.path.exists(data_class_path):
                    os.mkdir(data_class_path)
                        
            video_origin_path = os.path.join(video_archive_path, video_name)
            video_target_path = os.path.join(data_class_path, video_name)
            if not os.path.exists(video_target_path):
                    shutil.copy(video_origin_path, data_class_path)
                    
                    
if __name__ == "__main__":
   annotation_dict_path = "dataset/annotation_dict.json"
   labels_dict_path = "dataset/labels_dict.json"
   video_archive_path = "dataset/examples/"


   augmented_duct_path = "dataset/augmented_annotation_dict.json"
   augmented_video_archive_path = "dataset/augmented-videos/"
    
   augmentVideo(annotation_dict_path, labels_dict_path)
   setup_training_data(annotation_dict_path, labels_dict_path, video_archive_path)
   setup_training_data(augmented_duct_path, labels_dict_path, augmented_video_archive_path)