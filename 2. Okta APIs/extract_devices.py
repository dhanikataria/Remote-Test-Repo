import requests
import json

# Attributes to be set by the user
base_url = "https://PUT_UR_DOMAIN_HERE/api/v1/devices?expand=userSummary"
api_key = "__PUT_YOUR_API_TOKEN_HERE"

def parameters(i):
    temp_lst=[]
    for l in ["id", "status"]:
        temp_dict = {}

        temp_dict.update({str(l): str(devices[i][l])})
        temp_lst.append(temp_dict)

    for l in ["platform", "manufacturer", "model", "registered"]:
        temp_dict = {}
        temp_dict.update({str(l): str(devices[i]["profile"][l])})
        temp_lst.append(temp_dict)

    return temp_lst

headers = {
    "Authorization": "SSWS " + api_key,
    "Accept": "application/json",
    "Content-Type": "application/json"
}
url = base_url

devices = []
response = requests.get(url, headers=headers)
while url:


    response = requests.get(url, headers=headers)

    users_data = json.loads(response.text)

    devices.extend(users_data)


    if 'next' in response.links:
        url = response.links['next']['url']
    else:
        url = None


k=1
final_data=[]
for i in range (0,len(devices)):

        temp_lst = []
        if not devices[i]["_embedded"]:
            temp_dict2 = {}
            generated_key="No user assigned to device" +"_"+str(k)
            k=k+1
            temp_lst=parameters(i)
            temp_dict2[generated_key] = temp_lst
            final_data.append(temp_dict2)
        else:
            temp_dict2 = {}
            temp_lst = parameters(i)
            temp_dict = {}
            temp_dict.update({str("managementStatus"): str(devices[i]["_embedded"]["users"][0]["managementStatus"])})
            temp_lst.append(temp_dict)

            for l in ["firstName","lastName","login","email"]:
                temp_dict = {}
                temp_dict.update({str(l): str(devices[i]["_embedded"]["users"][0]["user"]["profile"][l])})
                temp_lst.append(temp_dict)

            temp_dict2[devices[i]["_embedded"]["users"][0]["user"]["id"]] = temp_lst
            final_data.append(temp_dict2)

final = json.dumps(final_data, indent=2)
print(final)

