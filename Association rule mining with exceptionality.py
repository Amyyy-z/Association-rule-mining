#import libraries
import pandas as pd
import numpy as np
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, fpgrowth
from mlxtend.frequent_patterns import association_rules

#load health records
data = pd.read_csv('Hospital_partial.csv')
data.head()

#identify unique and missing varaible
data.Class.unique()
data = data.replace('?', np.NaN) #replace missing variales with '?'

data.isnull().sum()

#exclude instances with missing sex or age
data = data[~(data['Sex'].isnull())]
data = data[~(data['Age'].isnull())]

#define variables to exclude blood examination results
data = data[['Age', 'Sex', 'On thyroxine', 'On antithyroid medication','Sick', 'Pregnant', 
             'Thyroid surgery', 'I131 treatment', 'Query hypothyroid', 'Query hyperthyroid', 
             'Goiter', 'Tumor', 'Psych', 'Vitamin D Deficiency', 'Hypertension', 'Diabetes', 
             'Depression', 'Obesity', 'Radiation', 'Status']]


#replace f with 'not_' and t with ''
data['On thyroxine'] = data['On thyroxine'].replace('f', 'Not_Thyroxine')
data['On thyroxine'] = data['On thyroxine'].replace('t', 'Thyroxine')

data['On antithyroid medication'] = data['On antithyroid medication'].replace('f', 'Not_On antithyroid medication')
data['On antithyroid medication'] = data['On antithyroid medication'].replace('t', 'On antithyroid medication')

data['Sick'] = data['Sick'].replace('f', 'Not_Sick')
data['Sick'] = data['Sick'].replace('t', 'Sick')

data['Pregnant'] = data['Pregnant'].replace('f', 'Not_Pregnant')
data['Pregnant'] = data['Pregnant'].replace('t', 'Pregnant')

data['Thyroid surgery'] = data['Thyroid surgery'].replace('f', 'Not_Thyroid surgery')
data['Thyroid surgery'] = data['Thyroid surgery'].replace('t', 'Thyroid surgery')

data['I131 treatment'] = data['I131 treatment'].replace('f', 'Not_I131')
data['I131 treatment'] = data['I131 treatment'].replace('t', 'I131')

data['Query hypothyroid'] = data['Query hypothyroid'].replace('f', 'Not_Query hypothyroid')
data['Query hypothyroid'] = data['Query hypothyroid'].replace('t', 'Query hypothyroid')

data['Query hyperthyroid'] = data['Query hyperthyroid'].replace('f', 'Not_Query hyperthyroid')
data['Query hyperthyroid'] = data['Query hyperthyroid'].replace('t', 'Query hyperthyroid')

data['Goiter'] = data['Goiter'].replace('f', 'Not_Goiter')
data['Goiter'] = data['Goiter'].replace('t', 'Goiter')

data['Tumor'] = data['Tumor'].replace('f', 'Not_Tumor')
data['Tumor'] = data['Tumor'].replace('t', 'Tumor')

data['Psych'] = data['Psych'].replace('f', 'Not_Psych')
data['Psych'] = data['Psych'].replace('t', 'Psych')

data['Vitamin D Deficiency'] = data['Vitamin D Deficiency'].replace('f', 'Not_Vitamin_D_Deficiency')
data['Vitamin D Deficiency'] = data['Vitamin D Deficiency'].replace('t', 'Vitamin_D_Deficiency')

data['Hypertension'] = data['Hypertension'].replace('f', 'Not_Hypertension')
data['Hypertension'] = data['Hypertension'].replace('t', 'Hypertension')

data['Diabetes'] = data['Diabetes'].replace('f', 'Not_Diabetes')
data['Diabetes'] = data['Diabetes'].replace('t', 'Diabetes')

data['Depression'] = data['Depression'].replace('f', 'Not_Depression')
data['Depression'] = data['Depression'].replace('t', 'Depression')

data['Obesity'] = data['Obesity'].replace('f', 'Not_Obesity')
data['Obesity'] = data['Obesity'].replace('t', 'Obesity')

data['Radiation'] = data['Radiation'].replace('f', 'Not_Radiation')
data['Radiation'] = data['Radiation'].replace('t', 'Radiation')

#divide data into health risk groups and gender groups
data_healthy = data[data['Status'] == 'negative']
data_sick = data[data['Status'] == 'positive']

data_male = data[data['Sex'] == 'Male']
data_female = data[data['Sex'] == 'Female']

#remove column names
data_healthy.columns = [''] * len(data_healthy.columns)
data_sick.columns = [''] * len(data_sick.columns)

data_male.columns = [''] * len(data_male.columns)
data_female.columns = [''] * len(data_female.columns)

#convert dataframe into lists
data_healthy = data_healthy.values.tolist()
data_sick = data_sick.values.tolist()

data_male = data_male.values.tolist()
data_female = data_female.values.tolist()

data_healthy = [[s for s in sub_list if s] for sub_list in data_healthy]
data_sick = [[s for s in sub_list if s] for sub_list in data_sick]

data_male = [[s for s in sub_list if s] for sub_list in data_male]
data_female = [[s for s in sub_list if s] for sub_list in data_female]

#convert list into transcation dataframe
te = TransactionEncoder()
te_ary_healthy = te.fit(data_healthy).transform(data_healthy)
df_healthy = pd.DataFrame(te_ary_healthy, columns=te.columns_)
df_healthy

te = TransactionEncoder()
te_ary_sick = te.fit(data_sick).transform(data_sick)
df_sick = pd.DataFrame(te_ary_sick, columns=te.columns_)
df_sick

te = TransactionEncoder()
te_ary_male = te.fit(data_male).transform(data_male)
df_male = pd.DataFrame(te_ary_male, columns=te.columns_)
df_male

te = TransactionEncoder()
te_ary_female = te.fit(data_female).transform(data_female)
df_female = pd.DataFrame(te_ary_female, columns=te.columns_)
df_female

#frequent itemsets generations
frequent_itemsets_healthy = apriori(df_healthy, min_support=0.8, use_colnames=True)
frequent_itemsets_healthy['length'] = frequent_itemsets_healthy['itemsets'].apply(lambda x: len(x))
frequent_itemsets_healthy

frequent_itemsets_sick = apriori(df_sick, min_support=0.8, use_colnames=True)
frequent_itemsets_sick['length'] = frequent_itemsets_sick['itemsets'].apply(lambda x: len(x))
frequent_itemsets_sick

frequent_itemsets_male = apriori(df_male, min_support=0.8, use_colnames=True)
frequent_itemsets_male['length'] = frequent_itemsets_male['itemsets'].apply(lambda x: len(x))
frequent_itemsets_male

frequent_itemsets_female = apriori(df_female, min_support=0.8, use_colnames=True)
frequent_itemsets_female['length'] = frequent_itemsets_female['itemsets'].apply(lambda x: len(x))
frequent_itemsets_female

#common rules generation
rules_healthy = association_rules(frequent_itemsets_healthy, metric = "confidence", min_threshold = 0.9)
rules_sick = association_rules(frequent_itemsets_sick, metric = "confidence", min_threshold = 0.9)
rules_male = association_rules(frequent_itemsets_male, metric = "confidence", min_threshold = 0.9)
rules_female = association_rules(frequent_itemsets_female, metric = "confidence", min_threshold = 0.9)

#CPIR calculation
rules_healthy["CPIR"] = (rules_healthy["support"]-rules_healthy["antecedent support"]*rules_healthy["consequent support"])/(rules_healthy["antecedent support"]*(1-rules_healthy["consequent support"]))
rules_sick["CPIR"] = (rules_sick["support"]-rules_sick["antecedent support"]*rules_sick["consequent support"])/(rules_sick["antecedent support"]*(1-rules_sick["consequent support"]))
rules_male["CPIR"] = (rules_male["support"]-rules_male["antecedent support"]*rules_male["consequent support"])/(rules_male["antecedent support"]*(1-rules_male["consequent support"]))
rules_female["CPIR"] = (rules_female["support"]-rules_female["antecedent support"]*rules_female["consequent support"])/(rules_female["antecedent support"]*(1-rules_female["consequent support"]))

#exclude all the rules with CPIR less than 0.5, this can be defined by user
rules_healthy = rules_healthy[rules_healthy['CPIR'] >= 0.5]
rules_sick = rules_sick[rules_sick['CPIR'] >= 0.5]
rules_male = rules_male[rules_male['CPIR'] >= 0.5]
rules_female = rules_female[rules_female['CPIR'] >= 0.5]

#convert frozenset to string
def frozenset_to_str(x):
    x = list(x)
    x = str(x).lstrip('[').rstrip(']').strip()
    return x

#apply to all the rules
rules_healthy['antecedents'] = rules_healthy['antecedents'].apply(lambda x: frozenset_to_str(x))
rules_healthy['consequents'] = rules_healthy['consequents'].apply(lambda x: frozenset_to_str(x))

rules_sick['antecedents'] = rules_sick['antecedents'].apply(lambda x: frozenset_to_str(x))
rules_sick['consequents'] = rules_sick['consequents'].apply(lambda x: frozenset_to_str(x))

rules_male['antecedents'] = rules_male['antecedents'].apply(lambda x: frozenset_to_str(x))
rules_male['consequents'] = rules_male['consequents'].apply(lambda x: frozenset_to_str(x))

rules_female['antecedents'] = rules_female['antecedents'].apply(lambda x: frozenset_to_str(x))
rules_female['consequents'] = rules_female['consequents'].apply(lambda x: frozenset_to_str(x))

#sort the rules in descending order based on confidence and CPIR scores
rules_healthy = rules_healthy.sort_values(['confidence', 'CPIR'], ascending =[False, False])
rules_sick = rules_sick.sort_values(['confidence', 'CPIR'], ascending =[False, False])
rules_male = rules_male.sort_values(['confidence', 'CPIR'], ascending =[False, False])
rules_female = rules_female.sort_values(['confidence', 'CPIR'], ascending =[False, False])

#define rules with customization
final_rules_healthy = rules_healthy[rules_healthy['consequents'].str.contains('negative')]
final_rules_sick = rules_sick[rules_sick['consequents'].str.contains('positive')]


#exceptionality extraction, given an example of female groups
frequent_itemsets_female_exp = apriori(df_female, min_support=0.2, use_colnames=True) #set the minimum support to 0.2 as threshold
frequent_itemsets_female_exp['length'] = frequent_itemsets_female_exp['itemsets'].apply(lambda x: len(x))
frequent_itemsets_female_exp

#define confidence first, otherwise the rules cannot be generated since there might be empty antecedents or consequences
rules_female_exp = association_rules(frequent_itemsets_female_exp, metric = "confidence", min_threshold = 0.9)

#exclude all the rules with support value above 0.4
rules_female_exp = rules_female_exp[rules_female_exp['support'] <= 0.4]

#calculate CPIR for exceptions 
rules_female_exp["CPIR"] = (rules_female_exp["support"]-rules_female_exp["antecedent support"]*rules_female_exp["consequent support"])/(rules_female_exp["antecedent support"]*(rules_female_exp["consequent support"]))

#exclude rules with CPIR below 0.2
rules_female_exp = rules_female_exp[rules_female_exp['CPIR'] >= 0.2]

#sort rules
rules_female_exp = rules_female_exp.sort_values(['confidence', 'CPIR'], ascending =[False, False])

#convert frozenset to strings
rules_female_exp['antecedents'] = rules_female_exp['antecedents'].apply(lambda x: frozenset_to_str(x))
rules_female_exp['consequents'] = rules_female_exp['consequents'].apply(lambda x: frozenset_to_str(x))

#define final rules
final_rules_female_exp = rules_female_exp[rules_female_exp['consequents'].str.contains('positive')]
final_rules_female_exp = final_rules_female_exp[final_rules_female_exp['antecedents'].str.contains('F')]

#plot the final rules
import matplotlib.pyplot as plt
import networkx as nx

fig, ax=plt.subplots(figsize=(15, 15))
GA=nx.from_pandas_edgelist(final_rules_female_exp,source='antecedents',target='consequents')
nx.draw(GA,style='-.', alpha= 0.7, node_color= '#8B8378', edge_color='#8B8378', node_size=300, node_shape='o', 
        edge_cmap=plt.cm.Blues, with_labels=True)
# plt.savefig('final_rules_female_exp_Apriori.png')
plt.show()


