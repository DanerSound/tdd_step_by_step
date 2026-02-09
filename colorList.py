

def find_color(list_of_colors, letter):

    foundlist = []
    letter = letter.lower()

    if not isinstance(letter, str):
        raise TypeError('letter must be a string')
    if len(letter) > 1:
        raise ValueError('you must enter a single letter')
    if not letter.isalpha():
        raise ValueError('you must enter an alphabet character')

    for color in list_of_colors:
        if not isinstance(color, str):
            raise TypeError('color must be a string')
        else:
            if color.startswith(letter):
                foundlist.append(color)

    return foundlist


def main():
    colors = []

    print("Inserisci 10 colori:")

    for i in range(10):
        color = input(f"Colore {i + 1}: ")
        colors.append(color)

    letter = input("Inserisci una lettera per filtrare i colori: ")

    result = find_color(colors, letter)

    if result:
        print("Colori trovati:")
        for color in result:
            print(color)
    else:
        print("Nessun colore trovato con quella lettera.")



if __name__ == '__main__':
    main()