# In this archive we have to define the dictionary ml_info. This is a dictionary of dictionaries, that for each of the ML models we want
# assigns a dictionary that contains:
#
# 'clf': a scikit-learn classifier, or any object that implements the functions fit, and predict_proba or decision_function in the same way.
# 'formal_name': name to be used in plots and report
# 'calibration': can be None, 'sigmoid' or 'isotonic' 
#


import sklearn.ensemble as sk_en
import sklearn.linear_model as sk_lm
import sklearn.pipeline as sk_pl
import sklearn.model_selection as sk_ms
import xgboost as xgb

import sklearn.naive_bayes as sk_nb
import sklearn.neural_network as sk_nn
import sklearn.neighbors as sk_knn
import sklearn.gaussian_process as sk_gp
import sklearn.svm as sk_svm
import sklearn.discriminant_analysis as sk_da
import sklearn.feature_selection as sk_fs
import sklearn.preprocessing as sk_pp


ML_info ={}

ML_info['RF'] = {'formal_name': 'Random Forest',
                    'clf': sk_en.RandomForestClassifier(n_estimators = 100, max_features = 'auto'),
                    'calibration': None}

ML_info['LR'] = {'formal_name': 'l2-regularized Logistic Regression',
                    'clf': sk_lm.LogisticRegression(),
                    'calibration': None}
					
ML_info['XGB'] = {'formal_name': 'XGBoost',
					'clf': xgb.XGBClassifier(n_estimators=100),
					'calibration': None}

#To perform the training with hyperparameter tuned classification algorithms, uncomment the following lines
					
# pipeline_lr = sk_pl.Pipeline(steps=[('scl',sk_pp.StandardScaler()),('lr', sk_lm.LogisticRegression())])
# grid_params_lr=[{'lr__penalty':['l1', 'l2'], 'lr__C':[0.1,1.,10.,100.], 'lr__solver':['saga']},
               # {'lr__penalty':['elasticnet'], 'lr__l1_ratio':[0.5], 'lr__C':[0.1,1.,10.,100.], 'lr__solver':['saga']},
               # {'lr__penalty':['none'], 'lr__solver':['saga']}]
# tuned_lr=sk_ms.GridSearchCV(pipeline_lr,grid_params_lr, cv=10,scoring ='roc_auc', return_train_score=False, verbose=1)
# ML_info['LR_SCL_pipeline'] = {'formal_name': 'Logistic Regression (Hyperparameters)',
                    # 'clf': tuned_lr,
                    # 'calibration': 'sigmoid'}

# pipeline_bt = sk_pl.Pipeline(steps=[("xgb",xgb.XGBClassifier(n_estimators=100))])
# grid_params_bt=[{'xgb__n_estimators':[100], 'xgb__max_depth':[1,2,5], 'xgb__learning_rate':[0.05,0.1,0.25,0.5], 'xgb__gamma':[0,1,5,20]}]
# tuned_bt=sk_ms.GridSearchCV(pipeline_bt,grid_params_bt, cv=10,scoring ='roc_auc', return_train_score=False, verbose=1)
# ML_info['XGB_pipeline3'] = {'formal_name': 'XGBoost (Hyperparameters)',
                          # 'clf': tuned_bt,
                          # 'calibration': 'sigmoid'}


# pipeline_rf = sk_pl.Pipeline(steps=[("rf",sk_en.RandomForestClassifier())])
# grid_params_rf =[{ 'rf__n_estimators':[100], 'rf__max_depth':[None, 1,2,5], 'rf__max_features':[1,'auto']}]
# tuned_rf = sk_ms.GridSearchCV(pipeline_rf,grid_params_rf, cv=10,scoring ='roc_auc', return_train_score=False, verbose=1)
# ML_info['RF_pipeline'] = {'formal_name': 'Random Forest (Hyperparameters)',
                 # 'clf': tuned_rf,
                 # 'calibration': 'sigmoid'}

