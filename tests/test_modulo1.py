import pytest
from progetto.modulo1 import funzione_doppio, funzione_quadrato, ClasseParzialmenteImplementata

def test_funzione_doppio():
    x = 2
    # TODO Aggiungere 2 o più test per coprire funzione_doppio
    assert funzione_doppio(x) == 4
    

def test_funzione_quadrato():
    y = 3
    # TODO Aggiungere 2 o più test per coprire funzione_quadrato
    assert funzione_quadrato(y) == 9
import pytest
def test_metodo_esistente_classe():
    istanza = ClasseParzialmenteImplementata("Test")
    assert istanza.metodo_esistente() == "Ciao, sono Test!"

def test_metodo_da_completare_classe():
    istanza = ClasseParzialmenteImplementata("Test")
    istanza.metodo_da_completare("mario")
    # TODO: Aggiungere un'asserzione per verificare il comportamento del metodo
    assert istanza.metodo_da_completare("Mario") == "Test Mario"