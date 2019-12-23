# Evictions_Address_Identifier
Retrained stanford ner model to identify addresses.
Contains the train and test datasets along with the raw data and script to generate the training data in the format required.

Download all the dependencies from:
https://nlp.stanford.edu/software/CRF-NER.shtml

Commands:
Training - java -cp "*" edu.stanford.nlp.ie.crf.CRFClassifier -prop addresses.prop
Testing - java -cp "*" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -testFile test_ner.tsv
Infer - java -cp "*" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -textFile out.txt -outputFormat tabbedEntities 2> /dev/null
