### 1. Overview: Terraform Registry API Script
- **Description**: A Python script that uses the Terraform Registry API to retrieve required information.
- **Details**:
  - This script retrieves modules from specified providers using the Terraform Registry API.
  - It fetches details such as module name, version, published date, downloads overall, and provider.
  - The retrieved data is saved into a CSV file for easy access and analysis.
    
### 2. Usage
- **Description**: Perform the following steps before using this script.
- **Step-1**: Setting the attributes (lines 6 to 9 in code)
  - **api_key** = Generate the api_key from Terraform Enterprise. Either put directly in the script or set it as env variable.
  - **limit_per_result** = This will set the amount of result per response. The maximum results per page is 100.
  - **provider** = List all the providers for which you want to retrive the information.
  - **csv_file** = Provide the name of the output csv file which will include the retrieved information
    
- **Step-2**: Setting the base_url domain (line 20 in code)
  - **base_url** = Set your actual domain name in the URL

- **Step-3**: (Optional) Retrieving additional Information
  - **Additional Information** = If you want to retrive additional information than what is mentioned in lines 28 to 32 of the code. Just create another key-value pair for that.

- **Step-4**: Run the script
### 3. Output
- **Description**: A csv file will be automatically generated with the name provided under parameter csv_file.
