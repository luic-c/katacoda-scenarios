
#Importing necessary packages
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


# In[2]:


#Loading Dataset
iris = datasets.load_iris()


# # Exploratory Data Analysis (EDA)

# In[3]:


#Show the header (keys) of datasaet
print(iris.keys())


# In[4]:


#Description of the dataset
print(iris['DESCR'])


# In[5]:


#Exploring the values of each features
print('target_name:')
print(iris['target_names'])

print('data:')
print(iris['data'][:5])

print('target:')
print(iris['target'])

print('feature_names:')
print(iris['feature_names'])


# In[6]:


#Preparing for the Analysis
Data = iris['data']
target = iris['target']
anaDf = pd.DataFrame(Data, columns = iris['feature_names'])
anaDf.head()


# In[7]:


#Plot the data
_ = pd.plotting.scatter_matrix(anaDf, c = target, figsize = [10, 10], s = 150, marker = 'D')


# The three species can be clearly categorized by using the combination of petal length and petal width. Therefore, it is reasonable and suitable to use k Nearest Neighbors model for this application

# In[8]:


#Drop the features
DataDrop = np.delete(iris['data'], [0,1], 1)
print(DataDrop[:].shape)
print(iris['data'].shape)


# In[9]:


iris['feature_names'][2:4]


# In[10]:


anaDfDrop = pd.DataFrame(DataDrop, columns = iris['feature_names'][2:4])
anaDfDrop.head()


# In[11]:


#Plot the data
_ = pd.plotting.scatter_matrix(anaDfDrop, c = target, figsize = [10, 10], s = 150, marker = 'D')


# # Train the Model

# In[32]:


#Importing necessary packages
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from seaborn import heatmap


# In[33]:


#Splitting dataset into Training and Testing datasets
Data_train, Data_test, target_train, target_test = train_test_split(Data, target, test_size = 0.2, random_state = 21, stratify = target)


# In[34]:


#Declare the number of nearest neighbors to be observed
knn = KNeighborsClassifier(n_neighbors = 4)


# In[35]:


#Fitting training data to the model
knn.fit(Data_train, target_train)


# In[36]:


#Predicting with the test data
target_predict = knn.predict(Data_test)


# In[37]:


target_predict


# In[38]:


#Checking performance of the model
knn.score(Data_test, target_test)


# In[39]:


cm = confusion_matrix(target_test, target_predict)
type(cm)


# In[40]:


cmdf = pd.DataFrame(cm)
cmdf


# # Testing performance with different k factor

# In[41]:


# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))


# In[42]:


# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knnPer
    knnPer = KNeighborsClassifier(n_neighbors = k)

    # Fit the classifier to the training data
    knnPer.fit(Data_train, target_train)
    
    #Compute accuracy on the training set
    train_accuracy[i] = knnPer.score(Data_train, target_train)

    #Compute accuracy on the testing set
    test_accuracy[i] = knnPer.score(Data_test, target_test)


# In[43]:


# Generate plot
plt.title('kNN Performace and Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()


# From the line chart above, the best k factor could be 4

# # K-Folds Cross Validation

# In[44]:


from sklearn.model_selection import KFold


# In[45]:


foldsplit = 10


# In[46]:


kf = KFold(n_splits = foldsplit, random_state = 4)


# In[47]:


train_accuracy_fold = np.empty(foldsplit)
test_accuracy_fold = np.empty(foldsplit)


# In[48]:


knnFold = KNeighborsClassifier(n_neighbors = 4)
for k, (train_index, test_index) in enumerate(kf.split(DataDrop)):
    Data_train, Data_test = DataDrop[train_index], DataDrop[test_index]
    target_train, target_test = iris.target[train_index], iris.target[test_index]
    knnFold.fit(Data_train, target_train)
    train_accuracy_fold[k] = knnFold.score(Data_train, target_train)
    test_accuracy_fold[k] = knnFold.score(Data_test, target_test)
    #print "[fold {0}] score: {1:.5f}".format(k, train_accuracy[k])


# In[49]:


test_accuracy_fold


# In[50]:


plt.title('kNN Performance with differrent Folds')
plt.plot(test_accuracy_fold, label = 'Test Accuracy')
plt.plot(train_accuracy_fold, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Folds')
plt.ylabel('Accuracy')
plt.ylim(0.70, 1.025)
plt.xlim(0, 9)
plt.show()


# In[51]:


print(iris['data'][:50])


# # Save Model

# In[52]:


import pickle


# In[55]:


with open('./model.pkl', 'wb') as model_pkl:
    pickle.dump(knn, model_pkl)

