import json
import shutil
import os


def setup_training_data(annotation_dict_path, labels_dict_path, video_archive_path, training_data_path):
    
    try:
        with open(annotation_dict_path) as f:
            annotation_dict = json.load(f)
    except:
        print("Can't find annotation_dict.json")
    
    try: 
        with open(labels_dict_path) as f:
            labels_dict = json.load(f)
    except:
        print("Can't find annotation_dict.json")
        
    if not os.path.exists(training_data_path):
        os.mkdir(training_data_path)
        
    for i, annotation in enumerate(annotation_dict):
            annotation_str = str(annotation)
            video_name = f'{annotation_str}.mp4'
            video_class = str(annotation_dict[annotation])
            
            if(i%10!=0):
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
            
        
    
    return annotation_dict, labels_dict


if __name__ == "__main__":
    annotation_dict_path = "dataset/annotation_dict.json"
    labels_dict_path = "dataset/labels_dict.json"
    video_archive_path = "dataset/examples/"
    training_data_path = "dataset/training_data/"
    
    annotation_dict, labels_dict = setup_training_data(annotation_dict_path, labels_dict_path, video_archive_path, training_data_path)


    