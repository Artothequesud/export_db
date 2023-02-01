import csv
import json
import time

# 570
csv_file = 'data_ori.csv' #input

# output
json_file = 'data.json'

# json output structure (input key : output key)
json_structure_size = {
        "framed": {
            "height": 0,
            "lenght": 0
        },
        "unframed": {
            "height": 0,
            "lenght": 0
        }
}

json_structure = {
    # local data
    "Anges (collection)": "id",
    "Nom de loeuvre": "name",

    # author
    "Prenom": "firstname",
    "Nom": "lastname",

    # process
    "Technique": "process",

    #here
    "size" : "size"
}


# convert main
def convert_to_json_structure(data, json_structure):
    json_data = json_structure
    print(data)
    output = {}
    for key, value in json_structure.items():
        if value != "size":
            if isinstance(value, dict):
                output[value] = convert_to_json_structure(data, value)
            elif isinstance(value, list):
                output[value] = data[key]
        else:
            print(value)
    return output

# open csv
start_time = time.time()
data = []
with open(csv_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        json_data = convert_to_json_structure(row, json_structure)
        data.append(json_data)
        print("Convert row ", row, "\n")

# write json
with open(json_file, 'w') as jsonfile:
    json.dump(data, jsonfile, sort_keys=True, indent=4, ensure_ascii=False)

end_time = time.time()
elapsed_time = end_time - start_time

print("Time elapsed: {:.2f} s".format(elapsed_time))