## FINAL
import sys
import csv
def main(argv):
    data_num = argv[0]
    data_month = argv[1]
    date = "2016-"+data_month + "-"+ data_num + " 00:00:00"
    wf = open("/mnt/ssd2/rawdata/2016/ASDATA/" + data_month + "" + data_num +"2016_mod.csv", 'w')
    with open("/mnt/ssd2/rawdata/2016/ASDATA/" + data_month + "" + data_num +"2016.csv") as f:
        for line in csv.reader(f):
            sas = line[1].strip()
            das = line[2].strip()
            size = line[0].strip()
            wf.write(date + "," + sas + "," + das + "," + size + "\n")

    f.close()
    wf.close()
    print("Done Writing")
if __name__ == "__main__":
   main(sys.argv[1:])    
