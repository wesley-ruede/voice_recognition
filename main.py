import numpy as np
from sklearn.metrics import accuracy_score
from keras.callbacks import EarlyStopping
 
from dataset import DatasetGenerator
 
DIR = 'input' # unzipped train and test data
 
INPUT_SHAPE = (177,98,1)
BATCH = 32
EPOCHS = 15
 
LABELS = 'yes no up'.split()
NUM_CLASSES = len(LABELS)
