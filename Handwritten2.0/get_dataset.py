import numpy as np 
import matplotlib.pyplot as plt 
import os 
import cv2
import pickle
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout, Activation, Flatten, Conv2D, MaxPooling2D
DATADIR = "orig_slike/"

CATEGORIES = ["0","1","2","3","4","5","6","7","8","9", "+", "-"]
IMG_SIZE = 28

training_data = []

def create_training_data():
	for category in CATEGORIES:
		path = os.path.join(DATADIR, category)
		class_num = CATEGORIES.index(category)
		for img in os.listdir(path):
			try:
				img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
				new_array = cv2.resize(img_array, (IMG_SIZE,IMG_SIZE))
				training_data.append([new_array, class_num])
				print(img)
			except Exception as e:
				pass

create_training_data()
random.shuffle(training_data)
X = []
y = []

for features, label in training_data:
	X.append(features)
	y.append(label)

X = np.array(X).reshape(-1,IMG_SIZE,IMG_SIZE,1)
y = np.array(y)

print(X.shape, y.shape)

y = y.reshape(-1, 1) == np.arange(12).reshape(1, -1)
print(y.shape)
pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()

X = pickle.load(open("X.pickle","rb"))
y = pickle.load(open("y.pickle","rb"))

X = X/255.0


model = Sequential()

model.add(Conv2D(32,(3,3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dropout(0.2))

model.add(Dense(64))

model.add(Dense(12))
model.add(Activation('softmax'))
print("Učenje")
model.compile(loss='categorical_crossentropy',
			optimizer='adam',
			metrics=['accuracy'])
model.fit(X, y, batch_size=32, epochs=10, validation_split=0.3)
save_dir = "results/"
model_name = 'dataset.h5'
model_path = os.path.join(save_dir, model_name)
model.save(model_path)
