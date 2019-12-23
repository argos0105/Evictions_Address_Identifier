import pandas as pd
import random
import names
import math

path_address_file = "/Users/I516831/UW/evictions/king.csv"
def write_address_name():
	df_raw = pd.read_csv(path_address_file)
	df_seattle = df_raw[df_raw['CITY'] == 'SEATTLE']
	df_seattle = df_seattle.reset_index(drop = True)
	index = list(range(0,df_seattle.shape[0]))
	random.shuffle(index)

	train_index = index[:len(index)//2]
	file = open("train_ner.txt","w")
	for i in train_index:
		unit_number = df_seattle.iloc[i]['NUMBER']
		file.write(str(unit_number)+"\t"+"B-UNIT"+"\n")

		street_number = df_seattle.iloc[i]['STREET'].split()
		for word in street_number:
			file.write(str(word)+"\t"+"I-UNIT"+"\n")

		city = 	df_seattle.iloc[i]['CITY']
		if not str(city) == 'nan':
			file.write(str(city)+"\t"+"B-UNIT"+"\n")

		pin = 	df_seattle.iloc[i]['POSTCODE']
		file.write(str(pin)+"\t"+"B-PIN"+"\n")

		name = names.get_full_name().split()
		file.write(name[0]+"\t"+"0"+"\n")
		file.write(name[1]+"\t"+"0"+"\n")
	file.close()
	

	test_index = index[(len(index)//2)+1:]
	file = open("test_ner.txt","w")
	for i in test_index:
		unit_number = df_seattle.iloc[i]['NUMBER']
		file.write(str(unit_number)+"\t"+"B-UNIT"+"\n")

		street_number = df_seattle.iloc[i]['STREET'].split()
		for word in street_number:
			file.write(str(word)+"\t"+"I-UNIT"+"\n")

		city = 	df_seattle.iloc[i]['CITY']
		if not str(city) == 'nan':
			file.write(str(city)+"\t"+"B-UNIT"+"\n")

		pin = 	df_seattle.iloc[i]['POSTCODE']
		file.write(str(pin)+"\t"+"B-PIN"+"\n")

		name = names.get_full_name().split()
		file.write(name[0]+"\t"+"0"+"\n")
		file.write(name[1]+"\t"+"0"+"\n")
	file.close()

if __name__ == '__main__':
	write_address_name()		