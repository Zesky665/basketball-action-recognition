import json
import shutil
import os
import itertools
from augment_videos import augmentVideo
import pandas as pd


def setup_training_data(annotation_dict_path, labels_dict_path, video_archive_path, augmented_dict_path, augmented_video_archive_path):
    
    train_df = pd.DataFrame(columns=['file_name', 'class'])
    val_df = pd.DataFrame(columns=['file_name', 'class'])
    test_df = pd.DataFrame(columns=['file_name', 'class'])
    
    
    training_data_path = "Dataset\\training_data\\"
    if not os.path.exists(training_data_path):
        os.mkdir(training_data_path)
    
    with open(annotation_dict_path) as f:
        annotation_dict = json.load(f)
    
    with open(augmented_dict_path) as f:
        augmented_dict = json.load(f)
    
    with open(labels_dict_path) as f:
        labels_dict = json.load(f)
        
    # First with the regular videos
    
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
            file_name = f'{video_target_path}'
            new_row = {'file_name': file_name, 'class': video_class}
            train_df = pd.concat([train_df, pd.DataFrame([new_row])], ignore_index=True)
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
                file_name = f'{video_target_path}'
                new_row = {'file_name': file_name, 'class': video_class}
                val_df = pd.concat([val_df, pd.DataFrame([new_row])], ignore_index=True)
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
                file_name = f'{video_target_path}'
                new_row = {'file_name': file_name, 'class': video_class}
                test_df = pd.concat([test_df, pd.DataFrame([new_row])], ignore_index=True)
                shutil.copy(video_origin_path, data_class_path)
                
    # And now with the augmented videos
        
    n = len(augmented_dict) 
    m = round(n * 0.8)
    i = iter(augmented_dict.items())

    train = dict(itertools.islice(i, m))
    val_test = dict(i)
    
    for i, annotation in enumerate(train):
        annotation_str = str(annotation)
        video_name = f'{annotation_str}.mp4'
        video_class = str(augmented_dict[annotation])
        
        train_data_path = os.path.join(training_data_path, 'train')
        if not os.path.exists(train_data_path):
            os.mkdir(train_data_path)
        data_class_path = os.path.join(train_data_path, video_class)
        if not os.path.exists(data_class_path):
            os.mkdir(data_class_path)
                        
        video_origin_path = os.path.join(augmented_video_archive_path, video_name)
        video_target_path = os.path.join(data_class_path, video_name)
        if not os.path.exists(video_target_path):
            file_name = f'{video_target_path}'
            new_row = {'file_name': file_name, 'class': video_class}
            train_df = pd.concat([train_df, pd.DataFrame([new_row])], ignore_index=True)
            shutil.copy(video_origin_path, data_class_path)
            
        
    for i, annotation in enumerate(val_test):
        annotation_str = str(annotation)
        video_name = f'{annotation_str}.mp4'
        video_class = str(augmented_dict[annotation])
        
        if(i%2!=0):
            val_data_path = os.path.join(training_data_path, 'val')
            if not os.path.exists(val_data_path):
                os.mkdir(val_data_path)
            data_class_path = os.path.join(val_data_path, video_class)
            if not os.path.exists(data_class_path):
                os.mkdir(data_class_path)
                        
            video_origin_path = os.path.join(augmented_video_archive_path, video_name)
            video_target_path = os.path.join(data_class_path, video_name)
            if not os.path.exists(video_target_path):
                file_name = f'{video_target_path}'
                new_row = {'file_name': file_name, 'class': video_class}
                val_df = pd.concat([val_df, pd.DataFrame([new_row])], ignore_index=True)
                shutil.copy(video_origin_path, data_class_path)
        else:

            test_data_path = os.path.join(training_data_path, 'test')
            if not os.path.exists(test_data_path):
                os.mkdir(test_data_path)
            data_class_path = os.path.join(test_data_path, video_class)
                
            if not os.path.exists(data_class_path):
                os.mkdir(data_class_path)
                        
            video_origin_path = os.path.join(augmented_video_archive_path, video_name)
            video_target_path = os.path.join(data_class_path, video_name)
            if not os.path.exists(video_target_path):
                file_name = f'{video_target_path}'
                new_row = {'file_name': file_name, 'class': video_class}
                test_df = pd.concat([test_df, pd.DataFrame([new_row])], ignore_index=True)
                shutil.copy(video_origin_path, data_class_path)
                
        train_df.to_csv("Dataset\\train.csv", sep='\t', encoding='utf-8', header=False, index=False)
        val_df.to_csv("Dataset\\val.csv", sep='\t', encoding='utf-8', header=False, index=False)
        test_df.to_csv("Dataset\\test.csv", sep='\t', encoding='utf-8', header=False, index=False)
                    
                    
if __name__ == "__main__":
    annotation_dict_path = "Dataset\\annotation_dict.json"
    labels_dict_path = "Dataset\\labels_dict.json"
    video_archive_path = "Dataset\\examples\\"


    augmented_dict_path = "Dataset\\augmented_annotation_dict.json"
    augmented_video_archive_path = "Dataset\\augmented-videos\\"
    
    augmentVideo(annotation_dict_path, labels_dict_path)
    setup_training_data(annotation_dict_path, labels_dict_path, video_archive_path, augmented_dict_path, augmented_video_archive_path)