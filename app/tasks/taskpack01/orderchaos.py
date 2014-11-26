import random

from ..task import Task


class OrderedChaosTask(Task):
    '''
    W tym zadaniu należy:

    1. przejrzeć długi napis w zmiennej `data`,
    2. odrzucić wszystkie znaki, ktore nie są literami,
    3. jeżeli posortujesz litery malejąco pod względem występowania
       otrzymasz słowo, które jest rozwiązaniem zadania.

    Przykład:
    Rozwiazaniem dla `"@t12k@k50ko342o"` jest slowo `"kot"`.
    '''

    title = 'Porządkowanie chaosu'

    variable_name = 'data'

    template = '''\
    ########################
    # Porzadkowanie chaosu #
    ########################

    import string

    # Przyda sie:
    # To czy znak nalezy do jakiegos zbioru mozna sparwdzic przy pomocy
    # wyrazenia "in" w nastepujacy sposob:
    # "a" in "abc" zwroci True
    # "d" in "abc" zwroci False

    # Warto rowniez sprawdzic co zawiera zmienna ascii_letters
    # zdefiniowana w bibliotece zaimportowanej powyzej...

    {var_eq_data}
    '''

    success_msg = 'Wyłuskane i uporządkowane. Bardzo dobrze, tak trzymać!'

    hints = ['Pełne chaosu to zadanie jest... raz jeszcze spróbuj.']

    codewords = [
        'marchew',
        'lampion'
        'beton',
        'figaro',
        'mozart',
        'chopin',
        'chanel',
        'mruczek',
        'relatywni',
        'ambitne',
        'trapez',
        'poduszka',
    ]

    def generate_data(self):
        r = random.Random()
        r.seed(self.seed)
        codeword = r.choice(self.codewords)
        noise_chars = list('0123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~')
        r.shuffle(noise_chars)
        runs = []
        count = r.randrange(5, 10)
        for c in reversed(codeword):
            count += r.randrange(1, 20)
            runs.append(c * count)
        count = 128
        for c in noise_chars[:r.randrange(6, 12)]:
            count += r.randrange(15, 30)
            runs.append(c * count)

        data = list(''.join(runs))
        r.shuffle(data)

        return ''.join(data)

    def solutions(self):
        r = random.Random()
        r.seed(self.seed)
        codeword = r.choice(self.codewords)
        return [codeword]
