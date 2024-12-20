translit = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
            'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K',
            'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
            'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc',
            'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu',
            'Я': 'Ia', 'Ъ': '', 'Ь': ''}

with open("cyrillic.txt", "r", encoding="UTF-8") as file_in:
    text = file_in.readline().strip()

for s in text:
    text = text.replace(s, translit.get(s, s))
    text = text.replace(s, translit.get(t := s.upper(), s).lower())

with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    file_out.write(text)