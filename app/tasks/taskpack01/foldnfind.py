import random
import string

from ..task import Task


class FoldNFindTask(Task):
    '''
    W zmiennej `crypto_data` dany jest długi ciąg znaków. Jego
    całkowita długość to iloczyn dwóch liczb pierwszych. Ciąg należy
    połamać na równe części (okres/długość łamania jest jednym z
    czynników iloczynu) i ułożyć je jedna pod drugą w kolejności
    dzielenia.

    Dla uproszczenia przyjmujemy, że ten iloczyn jest mniejszy niż 128
    a każdy z czynników - większy od 10.

    Oto [przykładowa metoda](http://stackoverflow.com/questions/18833759/python-prime-number-checker) weryfikująca czy podana liczba jest liczbą pierwszą:

        def is_prime(num):
            if num % 2 == 0 and num > 2:
                return False
            return all(num % test for test in range(3, int(math.sqrt(num)) + 1, 2))

    Hasło (proste, kilkuwyrazowe, ze znakami interpunkcyjnymi zamiast spacji)
    jest ukryte w pierwszej i ostatniej kolumnie tak ułożonego bloku (tzn.
    odczyt następuje z góry na dół a następnie od lewej do prawej). Przykład
    dla trochę krótszego ciągu wejściowego:

        * ciąg 21-znakowy (spacje są tylko dla poprawienia czytelności):
            PBC DEF HYI JKL MOT ARS PUN
        * liczby pierwsze: 3 oraz 7
        * bloki (oba przykłady dzielenia 3x7 + 7x3):
            PBC
            DEF
            HYI
            JKL
            MOT
            ARS
            PUN
            hasło(?): PDHJMAPCFILTSN - hmm... :/

            PBCDEFH
            YIJKLMO
            TARSPUN
            hasło(?): PYTHON - :)
    '''

    title = "Fold'n'Find"

    success_msg = 'Super! Szybko, co nie?'

    variable_name = 'crypto_data'

    # note: all passphrases must be 22 characters long a.t.m.
    passwords_list = [
        'ala.ma.kota.a.kot.wasy',
        'ja.tu.tylko.programuje',
        'ktos.szuka.tego.hasla?',
        'czy.juz.mamy.to.haslo?',
        'zadanie.podprogramowe!',
        'ktos.to.moze.znajdzie?',
        'absolutnie.taki.ukryty',
    ]

    # note: this method currently only generates correct data for the
    # 11 x 11 case
    def generate_data(self):
        all_chars = string.ascii_letters + '!,-.?'
        rows, columns = 11, 11

        r = random.Random()
        r.seed(self.seed)

        passphrase = r.choice(self.passwords_list)

        lines = [(char_left +
                  ''.join(r.choice(all_chars) for _ in range(columns - 2))
                  + char_right)
                 for char_left, char_right
                 in zip(passphrase[:rows], passphrase[rows:])]

        return ''.join(lines)


    def solutions(self):
        r = random.Random()
        r.seed(self.seed)

        passphrase = r.choice(self.passwords_list)
        return [passphrase]
