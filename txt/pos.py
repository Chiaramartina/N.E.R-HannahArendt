import pandas as pd
import nltk
from nltk import pos_tag

# Scarica i modelli richiesti
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Carica il file CSV
df = pd.read_csv("dataset/valid.csv")

# Rimuovi righe con valori NaN nella colonna Word
df = df[df['Word'].notna()]

# Assicurati che siano tutte stringhe
df['Word'] = df['Word'].astype(str)

# Esegui POS tagging
words = df['Word'].tolist()
pos_tags = pos_tag(words)

# Aggiungi la colonna POS al DataFrame
df['POS'] = [tag for (_, tag) in pos_tags]

# Salva il risultato
df.to_csv("train_with_pos.csv", index=False)

print("File salvato come train_with_pos.csv")
