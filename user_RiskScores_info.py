# In this archive we have to define the dictionary RS_info. This is a dictionary of dictionaries, that for each of the Risk Scores
# assigns a dictionary that contains:
#
# feature_oddratio: A dictionary with the variables that take part in the score with their odd ratios
# formal_name: name to be used in plots and report
# refit_oddratios: 'No' or 'Yes', the program will refit the odd ratios with new values


RS_info = {}

RS_info['updatedCHARLSON'] = {'feature_oddratio':{'updatedCHARLSON':1
											},
						'formal_name': 'CHARLSON updated',
						'refit_oddratios':'No'}

RS_info['Age'] = {'feature_oddratio':{'Age':1
											},
						'formal_name': 'Age',
						'refit_oddratios':'No'}
