import random

from ..task import Task


class SumNSliceTask(Task):
    '''
    Dodaj do siebie wszystkie elementy podanej listy a następnie z
    otrzymanej sumy wybierz co drugą cyfrę rozpoczynając od cyfry
    najbardziej znaczącej - wybrane cyfry złącz w jeden ciąg w
    oryginalnej kolejności.
    '''

    title = "Sum'n'Slice"

    success_msg = 'Bardzo dobrze. To nie było takie trudne, prawda?'

    variable_name = 'numbers'

    def generate_data(self):
        r = random.Random()
        r.seed(self.seed)
        data = [r.randrange(10**13, 10**14)
                for _ in range(r.randrange(80, 121))]
        return data

    def solutions(self):
        return [str(sum(self.generate_data()))[::2]]

