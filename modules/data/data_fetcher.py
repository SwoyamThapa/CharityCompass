import requests
import json


class data_fetcher:

    @staticmethod
    def get_data():
        api_url = "https://api.globalgiving.org/api/public/projectservice/all/projects/active"

        api_key = "f7a3ec25-cf95-4e66-bdcf-f31fbf8e1e9b"

        headers = {
            "Accept": "application/json",
        }

        params = {
            "api_key": api_key,  
        }


        response = requests.get(api_url, headers=headers, params=params)

        if response.status_code == 200:
            try:
                data = json.loads(response.text)["projects"]["project"] 

                with open("modules/data/output_data.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)

                print("Data has been stored in 'project_data.json'")

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON response: {e}")
        else:
            print(f"Error: Unable to retrieve data. Status code: {response.status_code}")