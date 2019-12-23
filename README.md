# Evictions_Address_Identifier
Retrained stanford ner model to identify addresses.
Contains the train and test datasets along with the raw data and script to generate the training data in the format required.

Download all the dependencies from:
https://nlp.stanford.edu/software/CRF-NER.shtml

Commands:
Training - java -cp "*" edu.stanford.nlp.ie.crf.CRFClassifier -prop addresses.prop
Testing - java -cp "*" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -testFile test_ner.tsv
Infer - java -cp "*" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -textFile out.txt -outputFormat tabbedEntities 2> /dev/null


Output of the current model - 
Ralph Furley	0
4712	B-UNIT
, Someplace Ln GA 3 DAY DEMAND Thothertown , 90210 FOR POSSESSION	I-UNIT
Jack Tripper	0
123	B-UNIT
Homeward Place Apt. 3B Anytown ,	0
54320	B-UNIT
DATE OF NOTICE :	I-UNIT
July 9 ,	0
2015	B-UNIT
TENANT IN POSSESSION : Jack Tripper RE : Notice	I-UNIT
of Eviction and Demand	0
for	B-UNIT
possession of property located at :	I-UNIT
123 Homeward Place	0
Apt.	B-UNIT
3B in	I-UNIT
_ Anytown ,	0
54320	B-UNIT
You are hereby notified that there is now due to the Landlord the sum of $ 1250.00 _ - including rent and late charges for the premises .	I-UNIT
