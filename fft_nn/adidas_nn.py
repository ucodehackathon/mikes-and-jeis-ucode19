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

from matplotlib import pyplot as plt

import keras
from keras.models import model_from_json
from keras.models import clone_model

import tensorflow as tf

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

class Adidas_nn:
	#Loads the model into the class. It receives as parameters:
	#	-model_file: path to the json file that specifies the model architecture
	#	-weights_file: path to the h5 file that stores the nn weights
	def __init__(self, model_file, weights_file):
		json_file = open('model_file', 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		model = model_from_json(loaded_model_json)
		# load weights into new model
		model.load_weights("weights_file")

		print("Loaded model from disk")

	#Predicts the class for X
	def predict_class(self, X):
		Y_prob = self.predict_prob(X)
		return Y_prob.argmax(axis=-1)

	#Predicts class probabilities for X
	def predict_prob(self,X):
		return model.predict(X)


