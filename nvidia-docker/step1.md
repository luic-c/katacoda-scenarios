Firstly, we should have a ML model. We use the basic iris dataset image classification model as a simple example. 

## Background

For some of you, docker may not look very interesting to you. If you are familiar with Docker, you can skip to the task. If you aren't, why not try a little test? Try to run the following command:

`python3 iris_model.py`{{execute}}

You would find there is an ImportError. That's normal because we haven't install necessary modules. We can install it using `pip install`, but things get tricky for your clients who may have a very complicated infrastructure, or they are too lazy to simply track what they have installed. 

Let's not start to talk about the difference between different package versions. 

What to do then? Ditch your work? Pray to God that your model hopefully works on your client's machine?

A simpler and safer way would be to use Docker.

Docker, to summarize, is to unify the runtime environment of the application by providing a Docker image. It also prevents the need to install packages manually by the client, which is very useful in this case.



> _Fun fact: Did you know the mascot for Docker is a whale? Just like the Linux penguin Tux, the Docker whale also has a name called Moby Dock. If you stumbled upon any 404 error pages on Docker website you might be lucky to come across him!_ 



## Generate Pickle File

We need to prepare a model for us to train and deploy. For simplicity, we have a simple image classification model against the iris dataset (iris_model.py) as an example. You can prepare one on your own, but an important note is the model will be stored as a pickle file after executing it. This allows us to open it later and reuse the model for prediction by calling the function `predict()` using new input data.

> NOTE: To store the model as a pickle file, add the following command at the end of the script:

```python
import pickle
pickle.dump(classifier, open('path/to/picklefile.pickle', 'wb'))
```

Run the following command:

`pip install sklearn pandas matplotlib seaborn`{{execute}}

This installs all the necessary packages for the model to run.

Now run the model:

`python3 iris_model.py`{{execute}}

Notice that `model.pkl` has been generated in the directory. 



