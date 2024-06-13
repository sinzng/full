
import json
import os

dir_path = "아카이브"

file_paths=[]
jsonl_data = []

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    
print(file_paths)

for file_path in file_paths:

    print(file_path)

    # Load the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extract the utterances and reformat them
    messages = data['utterances']

    for i in range(0, len(messages), 2):
        user_message = messages[i]

        #마지막에 speaker가 마무리로 대답하는 경우가 있음, 이 경우 대답을 기대하거나 하는게 아니므로 공란 or 삭제 
        
        #이건 공란으로
        assistant_message = messages[i + 1] if i + 1 < len(messages) else {"role": "assistant", "text": ""}

        #삭제하고 싶다면
        #if assistant_message == {"role": "assistant", "text": ""}:
        #   continue

        jsonl_data.append({
            "messages": [
                {"role": "user", "content": user_message['text']},
                {"role": "assistant", "content": assistant_message['text']}
            ]
        })

# Save the reformatted data to a new JSONL file
output_path = 'all2one.jsonl'
with open(output_path, 'w', encoding='utf-8') as output_file:
    for entry in jsonl_data:
        output_file.write(json.dumps(entry, ensure_ascii=False) + '\n')

print(f"Conversion complete. Output saved to {output_path}")

