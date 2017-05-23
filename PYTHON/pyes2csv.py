import elasticsearch
import csv
import random
import unicodedata

es = elasticsearch.Elasticsearch(["127.0.0.1:9200"])
res = es.search(index="filebeat-*", body=
	{ 
  "query": {
    "filtered": {
      "query": {
        "query_string": {
          "query": "*",
          "analyze_wildcard": 'true'
        }
      },
      "filter": {
        "bool": {
          "must": [
            {
              "query": {
                "query_string": {
                  "analyze_wildcard": 'true',
                  "query": "*"
                }
              }
            },
            {
              "range": {
                "date_start": {
                  "gte": 1451649600000,
                  "lte": 1460376000000,
                  "format": "epoch_millis"
                }
              }
            },
            {
              "range": {
                "input_byte": {
                  "gte": 524288000
                }
              }
            }
          ],
          "must_not": []
        }
      }
    }
  },
  "aggs": {
            "1": {
              "sum": {
                "field": "input_byte"
              }
            }
  },
  "fields": ["date_start","date_end","source_ip","source_port","dest_ip","dest_port","input_byte","protocol"]
  ,
  "sort": { "input_byte": { "order": "desc" }}
  
}, size=500000)
random.seed(1)
sample = res['hits']['hits']
print("Got %d Hits:" % res['hits']['total'])

with open('outputfile.csv', 'w') as csvfile:   #set name of output file here
	filewriter = csv.writer(csvfile, delimiter=',',  # we use TAB delimited, to handle cases where freeform text may have a comma
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	# create header row
	filewriter.writerow(["source_ip", "source_port","dest_ip","dest_port","protocol","input_bytes","date_start","date_end"])    #change the column labels here
	for hit in sample:   #switch sample to randomsample if you want a random subset, instead of all rows
		try:			 #try catch used to handle unstructured data, in cases where a field may not exist for a given hit
			col1 = hit['fields']['source_ip'][0]
			#print(col1)
		except Exception as e:
			col1 = ""
			print(e)
		try:
			col2 = hit['fields']['source_port'][0] #replace these nested key names with your own
			#col2 = col2.replace('\n', ' ')
			#print(col2)
		except Exception as e:
			col2 = ""
			print(e)
                
		try:
                        col3 = hit['fields']['dest_ip'][0] #replace these nested key names with your own
                        #col3 = col3.replace('\n', ' ')
                        #print(col3)
		except Exception as e:
                        col3 = ""
                        print(e)
		try:
                        col4 = hit['fields']['dest_port'][0] #replace these nested key names with your own
                        #col4 = col4.replace('\n', ' ')
                        #print(col4)
		except Exception as e:
                        col4 = ""
                        print(e)
		try:
                        col5 = hit['fields']['protocol'][0] #replace these nested key names with your own
                        #col5 = col5.replace('\n', ' ')
                        #print(col5)
		except Exception as e:
                        col5 = ""
                        print(e)
		try:
                        col6 = hit['fields']['input_byte'][0] #replace these nested key names with your own
                        #col6 = col6.replace('\n', ' ')
                        #print(col6)
		except Exception as e:
                        col6 = ""
                        print(e)
		try:
                        col7 = hit['fields']['date_start'][0] #replace these nested key names with your own
                        #col7 = col7.replace('\n', ' ')
                        #print(col7)
		except Exception as e:
                        col7 = ""
                        print(e)
		try:
			col8 = hit['fields']['date_end'][0]  #replace these nested key names with your own
			#print(col8)
			col8 = col8.replace('\n', ' ')
		except Exception as e:
			col8 = ""
			print(e)
		filewriter.writerow([col1,col2,col3,col4,col5,col6,col7,col8])


