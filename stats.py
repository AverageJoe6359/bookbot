def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_num_characters(words):
    character_dict = {}
    for ch in words:
        if ch.isalpha():
            ch = ch.lower()
            if ch not in character_dict:
                character_dict[ch]=1
            else:
                character_dict[ch] +=1
    return character_dict

def sorted_char(character_dict):
    result = [{"char": k, "num": v} for k, v in character_dict.items() if k.isalpha()]
    result.sort(key=lambda v: v["num"], reverse=True)
    return result 