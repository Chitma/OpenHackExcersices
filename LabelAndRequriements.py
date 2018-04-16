import numpy as np
import h5py
import os
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

# get the training labels

global_features = []
labels = []

train_path = "C://Users//Manish//Desktop//gear_images//axes01"
train_labels = os.listdir(train_path)

for train_label in train_labels:
    files = os.listdir(train_path+"//"+ train_label)
    print(train_labels)
    for file in files:
        path = train_path +"//" + train_label + '//' + file; 
        img = cv2.imread(path)
        print(img)
        global_features = np.hstack([img.reshape(-1,1)])
# # sort the training labels
# train_labels.sort()
# print(train_labels)


# empty lists to hold feature vectors and labels

for train_label in train_labels:
    labels.append(train_label)

targetNames = np.unique(labels)
le = LabelEncoder()
target = le.fit_transform(labels)

print("[STATUS] target labels: {}".format(target)) 

scaler = MinMaxScaler(feature_range=(0, 1))
rescaled_features = scaler.fit_transform(global_features)
print(rescaled_features)

h5f_data = h5py.File('C://Users//Manish//Desktop//data.h5', 'w')
h5f_data.create_dataset('dataset_1', data=np.array(rescaled_features))

h5f_label = h5py.File('C://Users//Manish//Desktop//labels.h5', 'w')
h5f_label.create_dataset('dataset_1', data=np.array(target))

h5f_data.close()
h5f_label.close()

h5f_data = h5py.File('C://Users//Manish//Desktop//data.h5', 'r')
h5f_label = h5py.File('C://Users//Manish//Desktop//data.h5', 'r')

global_features_string = h5f_data['dataset_1']
global_labels_string = h5f_label['dataset_1']

global_features = np.array(global_features_string)
global_labels = np.array(global_labels_string)

h5f_data.close()
h5f_label.close()

# verify the shape of the feature vector and labels
print("[STATUS] features shape: {}".format(global_features.shape))
print("[STATUS] labels shape: {}".format(global_labels.shape))