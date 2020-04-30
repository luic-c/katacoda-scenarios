Now that we have a model ready, the next step is to develop an API for sending data and receiving prediction results.

## Task

Here we choose to use Flask to build API because it is more common. The same can be applied to other frameworks like Django.

To install Flask, you can run the following command:

`pip install Flask`{{execute}}

Create a new file called `app.py` and copy the below code to the file:

`touch app.py`{{execute}}

<pre class="file" data-target="editor">
from flask import Flask, request
import pickle 
import numpy as np
import sys
from sklearn.neighbors import KNeighborsClassifier
knn = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)
@app.route('/')
def home_endpoint():
    return 'Plz input some data!'
@app.route('/predict', methods=['GET','POST'])
def predict_iris():
    sl = request.args.get('sl')
    sw = request.args.get('sw')
    pl = request.args.get('pl')
    pw = request.args.get('pw')
    unseen = np.array([[sl, sw, pl, pw]])
    result = knn.predict(unseen)
    return 'Result of ' + str(unseen) + '=' + str(result) 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
</pre>



Decoding the script to create API:

1. We import flask and every packages required for the model and load the trained model

```python
from flask import Flask, request
import pickle 
import numpy as np
import sys
from sklearn.neighbors import KNeighborsClassifier

knn = pickle.load(open('model.pkl', 'rb'))
```

2. Initialize Flask object

``` python
app = Flask(__name__)
```

3. Define a 'home' and 'predict' endpoint

```python
@app.route('/')
def home_endpoint():
    return 'Plz input some data!'
@app.route('/predict', methods=['GET','POST'])
def predict_iris():
    sl = request.args.get('sl')
    sw = request.args.get('sw')
    pl = request.args.get('pl')
    pw = request.args.get('pw')

    unseen = np.array([[sl, sw, pl, pw]])
    result = knn.predict(unseen)
    
    return 'Result of ' + str(unseen) + '=' + str(result)
```

4. Declare main function

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0')
```



To run the flask app we run the command:

`python3 app.py`{{execute}}

Open a new terminal and run the command:

`curl "http://0.0.0.0:5000/predict?sl=4.5&sw=2.1&pl=3.5&pw=1.1"`{{execute}}

We input data to make predictions on the model. If you receive the output like this then it means you pass!

`Result of [['4.5' '2.1' '3.5' '1.1']]=[1]`