import csv
with open("/home/aasingh/environments/flowpro/outputfile.csv","r") as f:
	with open("/home/aasingh/environments/flowpro/outputfilefinal.csv","w") as outf:
		writer = csv.writer(outf, lineterminator='\n')
		reader = csv.reader(f)
		all=[]
		for row in reader:
			year_start = row[6].replace(' ','-').split("-")[0] 
			month_start =  row[6].replace(' ','-').split("-")[1]
			day_start =  row[6].replace(' ','-').split("-")[2]
			year_end = row[7].replace(' ','-').split("-")[0]
			month_end =  row[7].replace(' ','-').split("-")[1]
			day_end =  row[7].replace(' ','-').split("-")[2]
			row.append(year_start)
			row.append(month_start)
			row.append(day_start)
			row.append(year_end)
			row.append(month_end)
			row.append(day_end)
			all.append(row)
		writer.writerows(all)	



