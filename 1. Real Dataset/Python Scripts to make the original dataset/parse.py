import re
import csv

def main():
	fname = 'APT1-parsed.csv'
	f = open("PEID Reports/APT1.txt", "r")
	for line in f:
		line = line.split("\\")
		substring = line[5]
		substring = re.compile("\s+::\t+").split(substring)
		try:
			with open(fname, 'a') as csvfile:
				writer = csv.writer(csvfile)
				writer.writerow([substring[0], substring[1].replace("\r\n","")])
		except IOError:
			print("I/O error")


if __name__ == "__main__":
	main()