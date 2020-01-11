import numpy as np
from keras.models import load_model
ha2p = np.array([[12,15,2019,27,4,2,0,0,0,37,2019,4.8,5.2,0.16,0.091,0.297,0.309,4.7,4.9,0.198,0.124,0.282,0.235,18.6,20.5,18.3,16.4,0.339,0.364,38,42,0.342,0.595,0.358,0.359,43,40,0.512,0.575]])


model=load_model('model_home.h5')
print(model.predict(ha2p))