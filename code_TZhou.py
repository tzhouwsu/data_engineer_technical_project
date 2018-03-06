
import json
import re
import csv
import sys

# here I define my-json-object
class my_json_obj :
   original_string = '{"key1":"val1","key2":"val2"}'
   json_original_data = json.loads('{"key1":"val1","key2":"val2"}')
   json_updated_data = json.loads('{"key1":"val1","key2":"val2"}')

   def __init__(self,string_to_be_read) :
     self.original_string = string_to_be_read   # this is a line-string to be read from file
     self.json_original_data = json.loads(string_to_be_read)
     self.json_updated_data = self.json_original_data

   def update_body(self) :  # this is to remove the html tags
     old = self.json_original_data['body']
     new = re.sub('<.*?>','',old)
#     print old
#     print new
     self.json_updated_data['body'] = new
     
   def add_key(self,key_name,key_value) :   # this is used to add 'soc5'
     self.json_updated_data[key_name] = key_value


# here I'm reading file-names from command-line arguments
if len(sys.argv) != 3 :
   print 'use this code by:\n python {} csv-file sample-file\n'.format(sys.argv[0])
   sys.exit()
else :
   fname_csv = sys.argv[1]
   fname_sample = sys.argv[2]


# here I want to read the mapping scheme from csv
my_onet_to_soc = {}

with open(fname_csv,'r') as fcsv :
   reader = csv.reader(fcsv, delimiter=',')
   for row in reader :
#      print row
      my_onet_to_soc[row[0]] = row[1]

#print my_onet_to_soc


# below I want to read json from file
fname_output = fname_sample + ".out"
fout = open(fname_output,'w')

line_number = 0
with open(fname_sample,'r') as fin :
   for line in fin:
      line_number = line_number + 1
      print line_number
      current = my_json_obj(line)

      current.update_body()  # this is to remove html tags
#      print(current.json_updated_data['body'])

      onet_value = current.json_original_data['onet']
      if onet_value in my_onet_to_soc :
         soc5_value = my_onet_to_soc[onet_value]
      else :
         soc5_value = 'null'
      current.add_key('soc5',soc5_value)  # this is to add the key 'soc5' to json

      json.dump(current.json_updated_data,fout)
      fout.write('\n')
      fout.flush()

fout.close()



