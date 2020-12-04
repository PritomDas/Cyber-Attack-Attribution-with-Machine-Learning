import requests
import pandas
import csv
import time
import json

url = 'https://www.virustotal.com/vtapi/v2/file/report'
key = ''

links = {}

def get_url(resource, hash_type):
	try:
		params = {'apikey': key, 'resource': resource, 'allinfo':'true'}
		response = requests.get(url, params=params)
		r = response.json()

		try:
			fname = "Virus Total Reports 2/" + str(resource) + '.json'
			with open(fname, 'w') as json_file:
				json.dump(r, json_file)
		except IOError:
			print("I/O error")
	except Exception as e:
		print('e')
	return


def main():
	df = pandas.read_csv('overview-sha1.csv', keep_default_na=False, usecols=['SHA1', 'MD5', 'SHA256'])

	i = 0
	ind = 0

	for index, row in df.iterrows():
		print(ind)
		if row['SHA1'] != "":
			print(row['SHA1'])
			print('sha1')
			get_url(row['SHA1'], 'SHA1')
		elif row['SHA256'] != "":
			print(row['SHA256'])
			print('sha256')
			get_url(row['SHA256'], 'SHA256')
		elif row['MD5'] != "":
			print(row['MD5'])
			print('MD5')
			get_url(row['MD5'], 'MD5')
		else:
			continue

		ind = ind + 1
		# i = i +1
		# if i == 4:
		# 	time.sleep(60)
		# 	i=0



if __name__ == "__main__":
	main()



