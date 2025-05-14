preeti_map = {
    "क": "s", "ख": "v", "ग": "u", "घ": "3", "ङ": "ª",
    "प": "k", "फ": "km", "ब": "a", "भ": "e", "म": "d",
    "न": "h", "त": "t", "थ": "y", "द": "b", "ध": "w",
    "न": "h", "ल": "g", "स": "l", "ह": "x",
    "ा": "f", "ि": "c", "ी": "cf", "ु": "j", "ू": "jf",
    "े": "r", "ै": "rf", "ो": "o", "ौ": "of", "ं": "]",
}

reverse_preeti_map = {v: k for k, v in preeti_map.items()}

def convert(from_script: str, text: str) -> str:
    converted = []
    mapping = preeti_map if from_script.lower() == "unicode" else reverse_preeti_map
    for char in text:
        converted.append(mapping.get(char, char))  # fallback to original if not mapped
    return ''.join(converted)
