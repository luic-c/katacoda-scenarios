Firstly, we should have a ML model. We use the basic iris dataset image classification model as a simple example. 

## Task











After running the model, it will be stored as a pickle file. This pickle file is important for later usage as we create a REST API for the model and dockerize it. 











Clone our example repository that contains the set of documentation with the following command:

`git clone https://github.com/katacoda/scenario-examples.git katacoda-scenario-examples`{{execute}}

Within the repository, you will see a set of examples of implementing various Katacoda functionality.

The scenario you are currently reading is in the directory `ls -lha katacoda-scenario-examples/create-scenario-101`{{execute}}. The directory name is what defines the URL.

An example of the current step is `katacoda-scenario-examples/create-scenario-101/step1.md`{{open}}

All the steps are collected via a JSON file, for example, `katacoda-scenario-examples/create-scenario-101/index.json`{{open}}.

The JSON file defines the scenario title, the description, steps order, the UI layout and environment. You can find more about the layouts within our scenarios at [katacoda.com/docs/scenarios/layouts](https://katacoda.com/docs/scenarios/layouts) and environments at [katacoda.com/docs/scenarios/environments](https://katacoda.com/docs/scenarios/environments).