
import json
import re
import csv

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
     print old
     print new
     self.json_updated_data['body'] = new
     
   def add_key(self,key_name,key_value) :   # this is used to add 'soc5'
     self.json_updated_data[key_name] = key_value


# here I want to read the mapping scheme from csv
my_onet_to_soc = {}

with open('map_onet_soc.csv','r') as fcsv :
   reader = csv.reader(fcsv, delimiter=',')
   for row in reader :
#      print row
      my_onet_to_soc[row[0]] = row[1]

#print my_onet_to_soc

# below I want to read json from file
fout = open('test-out','w')

with open('test-inp','r') as fin :
   for line in fin:
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

fin.close()
fout.close()



