import csv
import json

sentences = {}
current_sentence_num = None

with open('dataset/valid.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 4:
            continue
        
        first_col = row[0].strip()
        word = row[1].strip()
        tag = row[2].strip()
        pos = row[3].strip()
        
        if first_col.startswith("Sentence:"):
            current_sentence_num = int(first_col.split(":")[1].strip())
            sentences[current_sentence_num] = {
                "words": [],
                "tags": [],
                "pos": []
            }
        
        if current_sentence_num is not None:
            sentences[current_sentence_num]["words"].append(word)
            sentences[current_sentence_num]["tags"].append(tag)
            sentences[current_sentence_num]["pos"].append(pos)

# Prepara lista finale
final_data = []
for sent_num, content in sentences.items():
    sentence_text = " ".join(content["words"]).replace(" ,", ",").replace(" .", ".")
    final_data.append({
        "Sentence #": sent_num,
        "Sentence": sentence_text,
        "POS": content["pos"],
        "Tag": content["tags"]
    })

# Esporta in JSON
with open('valid_converted.json', 'w', encoding='utf-8') as f_json:
    json.dump(final_data, f_json, indent=2, ensure_ascii=False)

print("File JSON esportato con successo come 'dataset_converted.json'")
