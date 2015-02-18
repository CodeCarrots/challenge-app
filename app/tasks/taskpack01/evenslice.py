import random
import string

from ..task import Task


def char_gen(rnd, dist):
    for _ in range(dist):
        yield rnd.choice(string.digits + string.ascii_letters
            + string.punctuation)


class EvenSliceTask(Task):
    '''Mając ciąg wybierz znaki znajdujące się pod dodatnim i jednocześnie
    parzystym indeksem.
    '''

    title = "Even slice"

    success_msg = 'Bardzo dobrze. Nic się nie zacięło!'

    variable_name = 'words'

    all_words = ['suwaczki', 'zameczki', 'zapinki', 'guziczki', 'pętelki']

    def generate_data(self):
        rnd = random.Random()
        rnd.seed(self.seed)
        clean_words = ' '.join(rnd.sample(self.all_words, 3))

        scram = list(zip(list(char_gen(rnd, 1)) + list(clean_words),
            list(char_gen(rnd, 1)) + [char for char in char_gen(rnd,
            len(clean_words))]))
        data = ''.join([''.join(item) for item in scram])

        return data


    def solutions(self):
        scram = self.generate_data()
        return [scram[2::2]]

