### Basketball Action Recognition

This is a updated version of https://github.com/hkair/Basketball-Action-Recognition

The original was a bit messy. This version should be able to run without any tweaking.  

## Setup

### Env

With venv:
1. Run `python -m venv space-jam-fork`
2. Select `space-jam-form` as the python env in vscode. 
3. Run `source space-jam-fork/bin/activate`
4. Install packages with `pip install -r requirements.txt`

### Dataset

1. Download the dataset from the follwoing link:
https://www.kaggle.com/datasets/antocommii/spacejam-action-recognition

The link provided in the original repo seems to have some issue with it. 

2. Augment the dataset. 
Run the `augment_videos.py` script. 


### Run the model

Still trying to figure this one out. 

The main.py file uses a built in model and manual selection. 
