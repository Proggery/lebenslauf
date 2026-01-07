import pandas as pd
import os

# 1. Excel fájl beolvasása
df = pd.read_excel('data.xlsx', usecols=['name', 'mail'])

# 2. Sablon szöveg betöltése
template_file = 'template.txt'  # Ez legyen a meglévő txt fájl
with open(template_file, 'r', encoding='utf-8') as f:
    template_text = f.read()

# 3. Data mappa létrehozása, ha nem létezik
output_dir = 'data'
os.makedirs(output_dir, exist_ok=True)

# 4. TXT fájlok létrehozása minden sorhoz
for idx, row in df.iterrows():
    name = row['name']
    mail = row['mail']
    
    # Sablon szöveg módosítása
    text_filled = template_text.replace('__name__', name).replace('__mail__', mail)
    
    # Fájl név
    output_file = os.path.join(output_dir, f'job{idx+1}.txt')
    
    # Fájl írása
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text_filled)

print(f"{len(df)} fájl létrehozva a '{output_dir}' mappában.")
