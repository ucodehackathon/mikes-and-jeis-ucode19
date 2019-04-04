'''
* This file is part of Predict My Play.
*
* Copyright (C) 2019 Miguel Bolsa	<miguellbolsa at hotmail dot com>
*					 Jorgue Balzquez 	<jorgeblazher at gmail dot com>
*					 Miguel Crespo 		<mcrescas at gmail dot com>
*					 Juan Jose Gomez 	<jjgomez96 at hotmail com>
* For more information see <>
*
* Predict My Play is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* Predict My Play is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with Predict My Play. If not, see <http://www.gnu.org/licenses/>.
*
'''

import numpy as np
from numpy import genfromtxt

import scipy.io

import keras
from keras.models import model_from_json
from keras import backend as K



class Adidas_nn:
	#Loads the model into the class. It receives as parameters:
	#	-model_file: path to the json file that specifies the model architecture
	#	-weights_file: path to the h5 file that stores the nn weights

	def __init__(self, model_file, weights_file):
		json_file = open(model_file, 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		self.model = model_from_json(loaded_model_json)
		# load weights into new model
		self.model.load_weights(weights_file)

		self.model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])
		print("Loaded model from disk")
	def __del__(self):
		K.clear_session()


	#Predicts the class for X
	def predict_class(self, X):
		Y_prob = self.predict_prob(X)
		return Y_prob.argmax(axis=-1)

	#Predicts class probabilities for X
	def predict_prob(self,X):
		return self.model.predict(X)

	def predict_class_str(self,X):
		class_i = self.predict_class(X)
		to_return  = None
		if class_i == 0:
			to_return = "Dribbling"
		elif class_i == 1:
			to_return = "Pass_Left"
		elif class_i == 2:
			to_return = "Pass_Right"
		elif class_i == 3:
			to_return = "Running"
		elif class_i == 4:
			to_return = "Shot_Left"
		elif class_i == 5:
			to_return = "Shot_Right"
		elif class_i == 6:
			to_return = "Walking"

		return to_return


