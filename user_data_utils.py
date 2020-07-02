#Import libraries
import pandas as pd
import numpy as np
import datetime as dt
from user_variables_info import dict_var


def load_database():
	df = pd.read_excel('./data/DevelopmentCohortDB.xlsx')
	
	
	return df

def clean_database(df):
	df = df.T.drop_duplicates().T
	df['Exitus/Intubation'] = 0
	df.loc[df['Exitus']==1, 'Exitus/Intubation'] = 1
	df.loc[df['Intubation']==1, 'Exitus/Intubation'] = 1

	return df

def process_database(df):
	return df

def fillna_database(df):

	for i in dict_var.keys():
		if (df[i].dtype == 'float64'):
			if(len(df[i].value_counts())<15):
				df[i]=df[i].fillna(df[i].mode()[0])
			else:
				df[i]=df[i].fillna(df.loc[(df[i]<df[i].quantile(0.95))&(df[i]>df[i].quantile(0.05)),i].mean())
		elif (df[i].dtype == 'int64'):
			df[i]=df[i].fillna(df[i].mode())
			
	return df

def preprocess_filtered_database(df, wf_name):
	return df
