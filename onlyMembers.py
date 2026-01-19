"""
Solamente per Soci
Scrivi un programma che a partire da un elemento e una lista di elementi dica in output se l'elemento passato sia presente o meno nella lista.

Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento tramite il metodo index.
"""

def memberCheck(check_element, member_list):

    if len(member_list) == 0 :
        raise ValueError(" list must contain at least one member")

    if not check_element :
        raise ValueError(" the element to search must be present")

    if check_element not in  member_list:
        raise ValueError(" element not present ")

    return member_list.index(check_element)