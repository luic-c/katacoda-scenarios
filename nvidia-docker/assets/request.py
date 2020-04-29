# import Flask 
from flask import Flask, request
# import every packages required for the model
import pickle 
import numpy as np
import sys
from sklearn.neighbors import KNeighborsClassifier

#Load trained model 
knn = pickle.load(open('iris_model.pkl', 'rb'))

#Initialize Flask app
app = Flask(__name__)

@app.route('/predict')
def predict_iris():
    # Read all necessary request parameters
    sl = request.args.get('sl')
    sw = request.args.get('sw')
    pl = request.args.get('pl')
    pw = request.args.get('pw')

    # Use the predict method of the model to 
    # get the prediction for unseen data
    unseen = np.array([[sl, sw, pl, pw]])
    result = knn.predict(unseen)
    
    # return the result back
    return 'Predicted result for observation ' + str(unseen) + ' is: ' + str(result)

# By default will use port 5000
if __name__ == '__main__':
    app.run()