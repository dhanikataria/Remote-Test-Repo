### Overview. Okta API Script
- **Description**: A Python script to retrieve the type of devices used by users registered in Okta.
- **Details**:
  - This script uses the Okta API to fetch information about user devices being used by Okta users
 
### 1. Usage
- **Description**: Perform the following steps before using this script.
  
- **Step-1**: Setting the attributes (lines 5 to 6 in code)
  - **base_url** = Set the domain for your Okta domain
  - **api_key** = Generate the api_key from Okta. Either put directly in the script or set it as env variable.
 
- **Step-2**: Run the script

### 2. Output
- **Description**: Perform the following steps before using this script.
- **Details**:
  - It retrieves device attributes such as id, status, platform, manufacturer, model, and registration date.
  - The script also fetches user details linked to each device, including management status, first name, last name, login, and email.
  - Results are stored in a JSON format for easy readability and further processing.
    
