"""
5° QUESTÃO
"""

def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

#TESTANDO
string_predefinida = "Target-Sistemas"
string_invertida_predefinida = inverter_string(string_predefinida)
print(f"String invertida (predefinida): {string_invertida_predefinida}")
