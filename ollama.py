import requests
import json

def get_data_from_ollama(prompt):
    url = "http://localhost:5000/ollama"
    headers = {"Content-Type": "application/json"}
    payload = {"prompt": prompt}
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code==200:
        return response.json()
    else:
        response.raise_for_status()
        
def save_data_to_file(data, filename="output.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        
def main():
    user_input = input("input : ")
    data = get_data_from_ollama(user_input)
    save_data_to_file(data)
    print("파일이 저장됨")
    
if __name__ == "__main__":
    main()