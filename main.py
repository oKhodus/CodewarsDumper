import requests as req
import re

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

response = req.get("https://www.codewars.com/api/v1/users/{user}/code-challenges/completed")
user = input("Enter your username: ")
# print(response)

if response.status_code == 200:
    data = response.json()
    jsn_items = data["totalItems"]
    jsn_data = data["data"]
    number_of_challenge = 0
    for challenge in jsn_data:
        
        challenge_id = challenge["id"]
        challenge_name = challenge["name"]

        challenge_req = req.get(f"https://www.codewars.com/api/v1/code-challenges/{challenge_id}")

        if challenge_req.status_code == 200:
            challenge_data = challenge_req.json()

            with open(f"all_challenges.txt", "w") as file:
                file.writelines(challenge_name)
                file.write("\n")
                file.write(f"Summary of all challenges: {str(jsn_items) + "\n"}" )
        else:
            print(f"Erorr:", challenge_req.status_code)

    
else:
    print(f"Erorr:", response.status_code)
