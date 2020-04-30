Now that we have a model ready, the next step is to develop an API for sending data and receiving prediction results.

## Task

Here we choose to use Flask to build API because it is more common. The same can be applied to other frameworks like Django.

To install Flask, you can run the following command:

`pip install Flask`{{execute}}

Create a new file called `app.py` and copy the below code to the file:

`touch app.py`{{execute}}

``` 
from flask import Flask, request
import pickle 
import numpy as np
import sys
from sklearn.neighbors import KNeighborsClassifier

knn = pickle.load(open('iris_model.pkl', 'rb'))

app = Flask(__name__)
@app.route('/predict')
def predict_iris():
    # The model requires 4 arguments
    sl = request.args.get('sl')
    sw = request.args.get('sw')
    pl = request.args.get('pl')
    pw = request.args.get('pw')

    unseen = np.array([[sl, sw, pl, pw]])
    result = knn.predict(unseen)
    
    return 'Predicted result for observation ' + str(unseen) + ' is: ' + str(result)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```



Decoding the script to create API:

1. We import flask and every packages required for the model and load the trained model

```python
from flask import Flask, request
import pickle 
import numpy as np
import sys
from sklearn.neighbors import KNeighborsClassifier

knn = pickle.load(open('iris_model.pkl', 'rb'))
```

2. Initialize Flask object

``` python
app = Flask(__name__)
```

3. Define a 'predict' endpoint

```python
@app.route('/predict')
def predict_iris():
    # The model requires 4 arguments
    sl = request.args.get('sl')
    sw = request.args.get('sw')
    pl = request.args.get('pl')
    pw = request.args.get('pw')

    unseen = np.array([[sl, sw, pl, pw]])
    result = knn.predict(unseen)
    
    return 'Predicted result for observation ' + str(unseen) + ' is: ' + str(result)
```

4. Declare main function

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```



To run the flask app we run the command:

`python3 app.py`{{execute}}

