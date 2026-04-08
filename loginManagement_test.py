"""
Scrivi un programma che crei un file CSV per memorizzare in un dizionario i dati degli utenti registrati su un sito web.
I dati richiesti per ogni utente sono: username, password, email e data di registrazione. 
Il programma deve permettere di salvare le informazioni nel file, leggere i dati e stamparli a schermo.

allora ci sono deiverse cose che devono considerare , le cose del programma e la logia del dominio 
da definire con i contratti del TDD, la logica che a noi interessa e' gestire le credenziali degli utenti
quindi operazione di creazione, memorizzazione leggere stampare a schermo non fanno parte del dominio da testare 
(cioe' quella da mettere al sicuro con i contratti del TDD) perche sono relativi al linguaggio e il 99% delle folte ci sono delle funzioni 
standard

io ho una funzione che prende un dizionario , se il dizionario ha tutti i dati validi , tutti i campi sono presenti 
allora salva e va avanti
se invece manca un campo o c'e' un campo con un dato non valido , allora alzo un eccezione e non salvo niente
per semplicita mette io le condizioni che la password sia almeno di 8 caratteri , che l'email abbia una @ e che la data di registrazione sia in formato YYYY-MM-DD
poi non sapresi che altro aggiungere per testare
"""

import unittest

from loginManagement import validate_user_data

class TestLoginManagement(unittest.TestCase):

    def test_GIVEN_valid_user_data_WHEN_validated_THEN_user_is_accepted(
            self):
        
        user_data = {
            "username": "testuser",
            "password": "strongpassword",
            "email": "testuser@example.com",
            "registration_date": "2023-01-01"
        }
        
        self.assertTrue(validate_user_data(user_data))