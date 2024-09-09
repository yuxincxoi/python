import ollama
import json

def get_data_from_ollama(prompt):
    response = ollama.chat(model='llama2', messages = [
      {
        'role': 'user',
        'content': prompt
      }
    ])
    return response
        
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