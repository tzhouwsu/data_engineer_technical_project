
import json
import re

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
     


# below I want to read json from file
fout = open('test-out','w')

with open('test-inp','r') as fin :
   for line in fin:
      current = my_json_obj(line)
      current.update_body()
      print(current.json_updated_data['body'])
      json.dump(current.json_updated_data,fout)
      fout.write('\n')
      fout.flush()

fin.close()
fout.close()



