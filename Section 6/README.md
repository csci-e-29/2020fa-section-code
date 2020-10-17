# Section 7 - 2020sp - Luigi

### Key points/notes

#### Slides notes:
  - What is a DAG? DAG - Directed Acyclic Graph. Directed meaning arrow from one node to another, acyclic meaning no loops.
  - A ML workflow is often thought of in steps -- there are clear, distinct sections throughout this process. 
  - A graphical program is exactly the same idea -- we can accomplish this with luigi. Each of these circles represents a component within the data science pipeline -- you have specific code that preprocesses data, trains data, evaluate the model, etc. We thus separate our code in each of these luigi tasks in a DAG. 
  - Thinking of code and operations as graphs is found in many different places - tensorflow graphs, dask graphs, etc. Very important and useful concept!
  - In the realm of ML development, you’ll see a lot of cutting edge techniques highlight this idea. Shown here are Kubeflow, Tensorflow Extended, and Airflow (by Apache)
  

#### Details
- What is an External Task? https://luigi.readthedocs.io/en/stable/api/luigi.task.html#luigi.task.ExternalTask
- What is a Task? https://luigi.readthedocs.io/en/stable/tasks.html
     
#### Section Guide

1. Install everything via pipenv
2. For example1, run luigi commands (at top of module)
3. Run commands for example2
4. Look over tests for ideas about what to use for pset4 testing
5. Walk through objective of pst & show example
a. Run python download_save_models.py
b. ```python neural_style/neural_style.py eval --content-image images/content-images/amber.jpg --model saved_models/candy.pth --output-image "section-example.jpg" --cuda 0```