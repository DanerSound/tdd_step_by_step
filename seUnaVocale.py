

def vowel_checker(letter):

    if isinstance(letter, int):
        raise TypeError("vowel_cheker only works with letters, insert only letters")

    if len(letter)>1 :
        raise ValueError("vowel_checker only works for single letters")

    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f"Il carattere '{letter.lower()}' è una vocale")
        return True

    print(f"Il carattere '{letter.lower()}' non è una vocale")
    return False