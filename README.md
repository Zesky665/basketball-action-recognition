### Basketball Action Recognition

This is a updated version of https://github.com/hkair/Basketball-Action-Recognition

The original was a bit messy. This version should be able to run without any tweaking.  

## Setup

### Env

With venv:
1. Run `python -m venv space-jam-fork`
2. Select `space-jam-fork` as the python env in vscode. 
3. Run `source space-jam-fork/bin/activate`
4. Install packages with `pip install -r requirements.txt`

### Dataset

1. Download the dataset from the following link:
https://www.kaggle.com/datasets/antocommii/spacejam-action-recognition

Download the zip, uncompress it and move the `examples` folder into the Dataset directory. 


2. Augment the dataset. 
Run the `augment_videos.py` script. 

### Train 

Run the `train.py` script.
`python train.py`

The train.py script is automatically set to TEST mode. 
To Set to to TRAIN mode, open the file and change the TRAIN global value to True. 

### Run the model

Still trying to figure this one out. 

The main.py file uses a built in model and manual selection. 
