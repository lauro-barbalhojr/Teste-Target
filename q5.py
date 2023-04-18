# Declarando as variáveis"
string_original = "Inverter string"
string_invertida = ""

# Loop para percorrer a string original indexada ao contrário
for i in range(len(string_original) - 1, -1, -1):
    # Preenchendo a string invertida
    string_invertida += string_original[i]

print("String original:", string_original)
print("String invertida:", string_invertida)