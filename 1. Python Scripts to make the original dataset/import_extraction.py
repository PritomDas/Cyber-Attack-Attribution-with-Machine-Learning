import json
import os
import csv

def main():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	loc = os.path.join(dir_path, "Virus Total Reports 2")
	file_list = os.listdir(loc)
        index = 0

        with open('imports.csv', 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Resource', 'DLL', 'Imports'])
        	for file in file_list:
        		fname = os.path.join(loc, file)
                        print(index)
        		with open(fname) as f:
                                try:
                                        data = json.load(f)
                                        resource = data['resource']
                                        link = data["additional_info"]['imports']

                                        for k,v in link.items():
                                                for item in v:
                                                        writer.writerow([resource, k, item])
        	  		except Exception as e:
                                        print("fail")
                        index = index + 1

if __name__ == "__main__":
	main()
