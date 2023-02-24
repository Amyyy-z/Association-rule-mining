# Association-rule-mining
This project involves integrating text mining process, association rule mining, with exceptionality identification.

The text mining implementation and association rule extraction were stored in seperate files.

---------------------------------------------------

## Datasets

The open-access thyroid disease-related dataset can be found through: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/thyroid+disease).

The partial private dataset is available through [Hospital_partial.csv](https://github.com/Amyyy-z/Association-rule-mining/blob/main/Hospital_partial.csv)
Please email xinyu.zhang@monash.edu for full access to the dataset.
--------------------------

## Implementation Requirements

The overall flow of the project is as follows:
* Apply text mining procedures to extract key terminologies from raw digital medical reports. 
* The specific text mining process was implemented through R, and in this case, we uses Chinese health reports for terminologies extraction. 
* The overall text mining process is available through [Text mining for PDF.R](https://github.com/Amyyy-z/Association-rule-mining/blob/main/Text%20mining%20from%20PDF.R)
* Store extracted terminologies into a .csv file
* Use the .csv file to apply association rule mining algorithms for rules extraction. 
* The step-by-step common and exception rules generation procedures are available through [Association rule mining with exceptionality.py](https://github.com/Amyyy-z/Association-rule-mining/blob/main/Association%20rule%20mining%20with%20exceptionality.py)
* Store or plot the generated rules.

> TAHNK YOU!
  

