import requests
import json
import csv

# Attributes to be set by the user
api_key = "PUT_YOUR_API_KEY_HERE"
limit_per_result = 25
provider = ["azurerm", "azuread"]
csv_file = "modules.csv"

# No Attributes to set after this line of code
headers = {
    "Authorization": "Bearer" + " "+api_key,
    "Accept": "application/json",
    "Content-Type": "application/json"
}
all_modules ={}
temp_modules_list=[]
for i in provider:
    base_url = f"https://terraform.cantire.com/api/registry/v1/modules?limit={limit_per_result}&provider={i}"
    next_url=base_url
    while True:
        response = requests.get(next_url, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            for module in data["modules"]:
                temp_modules_dict = {}
                # Create a dictionary in similar way here to retrieve additional info
                temp_modules_dict["name"] = module["name"]
                temp_modules_dict["version"]= module["version"]
                temp_modules_dict["published_at"] = module["published_at"]
                temp_modules_dict["downloads_this_year"]   = module["downloads"]
                temp_modules_dict["provider"] = module["provider"]
                temp_modules_list.append(temp_modules_dict)
            fixed_part_of_url = base_url[:54]
            try:
                next_url_part = data["meta"]["next_url"][41:]
                next_url = fixed_part_of_url + next_url_part
            except:
                break
all_modules["modules"] = temp_modules_list
# pretty_print = json.dumps(all_modules, indent=4)
# print(pretty_print)
modules = all_modules["modules"]
column_headers = ["name", "version", "published_at", "downloads_this_year", "provider"]
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=column_headers)
    writer.writeheader()
    for module in modules:
        writer.writerow(module)

print(f"File has been successfully created in project folder and named as {csv_file}")
