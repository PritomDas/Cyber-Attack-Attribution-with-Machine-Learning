import json
import os
import csv

def main():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	loc = os.path.join(dir_path, "Virus Total Reports 2")
	file_list = os.listdir(loc)
        index = 0

        with open('entry_point.csv', 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Resource', 'Entry Point'])
        	for file in file_list:
        		fname = os.path.join(loc, file)
                        print(index)
        		with open(fname) as f:
                                try:
                                        data = json.load(f)
                                        resource = data['resource']
                                        pe = data["additional_info"]['pe-entry-point']
                                        writer.writerow([resource, pe])
        	  		except Exception as e:
                                        print("fail")
                        index = index + 1

if __name__ == "__main__":
	main()
