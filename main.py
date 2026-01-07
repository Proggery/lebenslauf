import pandas as pd
import os

# 1. Excel fájl beolvasása
df = pd.read_excel('data.xlsx', usecols=['name', 'mail'])

# 2. Sablon szöveg betöltése
template_file = 'template.txt'
with open(template_file, 'r', encoding='utf-8') as f:
    template_text = f.read()

# 3. Data mappa létrehozása, ha nem létezik
output_dir = 'data'
os.makedirs(output_dir, exist_ok=True)

# 4. Halmazok a már meglévő nevek és emailek ellenőrzésére
existing_names = set()
existing_mails = set()

# 5. TXT fájlok létrehozása minden sorhoz, ha nincs duplikátum
file_counter = 1  # Fájlszámláló a folyamatos nevekre
for _, row in df.iterrows():
    name = row['name']
    mail = row['mail']
    
    # Ellenőrzés: ha már létezik a név vagy az email, kihagyjuk
    if name in existing_names or mail in existing_mails:
        continue
    
    # Sablon szöveg módosítása
    text_filled = template_text.replace('__name__', name).replace('__mail__', mail)
    
    # Fájl név folyamatos számozással
    output_file = os.path.join(output_dir, f'job{file_counter}.txt')
    
    # Fájl írása
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text_filled)
    
    # Hozzáadjuk a halmazokhoz a nevet és emailt
    existing_names.add(name)
    existing_mails.add(mail)
    
    # Számláló növelése
    file_counter += 1

print(f"{file_counter-1} fájl létrehozva a '{output_dir}' mappában.")
