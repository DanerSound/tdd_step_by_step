

def string_joiner(current_string, join_to_string):

    current_string +=" "+join_to_string
    return current_string


def main():
    current = ""

    while True:
        user_input = input("Premi INVIO senza scrivere nulla per terminare: ")

        if user_input == "":
            break

        current =string_joiner(current, user_input)

    print("Risultato finale:", current)



if __name__ == '__main__':
    main()