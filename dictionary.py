##working with dictionaries
import json
variant = "variant"
position = "position"

data = {variant : [], position : []}
data[variant].append("dubstep")
data[variant].append("wubstep")
data[variant].append("trubstep")
data[position].append(1)
data[position].append(2)
data[position].append(3)

new_key = {'lastPage' : None}
object = {'data' : data, 'lastPage' : None}

json_data = json.dumps(object)
print json_data
string  = "went to work for a thing"
words = string.split()
print words[0]
print words[2]