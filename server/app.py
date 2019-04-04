from flask import Flask, request, render_template, send_from_directory
import os
import pandas
import json
import numpy as np
from adidas_nn import Adidas_nn
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

def prepocess_data(X):
    L = X.shape[0]
    
    dim = X[:,0]
    Y = np.fft.fft(dim)
    P2 = np.abs(np.true_divide(Y, L))
    P1 = P2[0:int(L/2)+1]
    P1[1:int(L/2)] = np.dot(2,P1[1:int(L/2)])

    #final = np.transpose(P1[0:30])
    final = np.asmatrix(P1[0:30])
    final = np.transpose(final)
    
    for i in range(1, 12):
        dim = X[:,i]
        Y = np.fft.fft(dim)
        P2 = np.abs(np.true_divide(Y, L))
        P1 = P2[0:int(L/2)+1]
        P1[0:int(L/2)] = np.dot(2,P1[0:int(L/2)])

        res = np.asmatrix(P1[0:30])
        res = np.transpose(res)
        final = np.concatenate((final, res), axis=1)
    final = np.reshape(final, (1, 360))
    return final
    
    


@app.route('/find', methods=['POST'])
def upload_file():
    nn=Adidas_nn("model/model.json","model/model.h5")


    filee=request.data
    filej=json.loads(filee)
    filed=filej['file'].encode('utf-8')

    csv = open("test.csv","wb") 
    print(filed)
    csv.write(filed) 
    csv.close() 

    dt = pandas.read_csv("test.csv").values

    datos_fft=prepocess_data(dt)
    es=nn.predict_class_str(datos_fft)

    del(nn)
    return es, 200
    
    


if __name__ == '__main__':
    app.run(debug=True, port=8080)