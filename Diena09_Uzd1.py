txt = "Naujas savarankiškas projektas"
print(txt)

for r in txt:
    print(r, end=" ")
print()
print("Nuskaitymas po vieną raide baigtas! \nPabaiga")

# Papildomas kodas
print(f"Programoje kintamasis 'txt' užima atminties {txt.__sizeof__()} baitų")
