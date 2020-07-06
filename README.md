# COVID-19 Salamanca Triage Score Development Code

Usage:
* Install requirements in a your python environment: `pip install -r requirements.txt`
* Put your data in ./data/DevelopmentCohortDB.xlsx (to train a new model) or ./data/ExternalTestingDB.xlsx (to externally test the models tested)
* Edit user_Workflow_info.py to specify if there is going to be an external testing or not
* By default, the program will train logistic regression, random forest and xgboost models without hyperparameter tuning. You can edit user_MLmodels_info.py to change the default models.
* Run the program in the command line: `python -m luigi --module COVIDTriage AllTasks` (you may specify a number NN of concurrent processes by adding `--workers NN`)
* The program will run and create several new folders, like *intermediate*, *log*, *report-XXXXXX-XXXXXX* and *models*
* In the report folder you will find ROC and PR curve graphs in png format, descriptive tables of the data in excel format, and text files describing the best model in the internal validation and external testing, with thresholds points and the feature importance of each variable in the model.
* In the models folder you will find every model trained with the data of DevelopmentCohortDB.xlsx, and an excel table with the results of the different hyperparameters if the model was run through a *GridSearchCV* hyperparamater tuning function.
