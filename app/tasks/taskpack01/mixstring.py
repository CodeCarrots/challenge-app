import random

from ..task import Task, format_data


class MixStringTask(Task):
    '''Mając dwa ciągi przepleć je zaczynając od pierwszego znaku pierwszego
    ciągu. Jeśli zabraknie kolejnego znaku do pary (parę tworzą znaki na tych
    samych indeksach z obu ciągów) w którymkolwiek z ciągów - zakończ operację.

    Przykład: `ciag_a="abcd", ciag_b="EFG" -> "aEbFcG"`
    '''

    title = "Mixstring"

    success_msg = 'Normalnie jak DJ... :)'

    variable_names = ['ciag_a', 'ciag_b']

    template = '''\
    # dana
    {var_eq_data}
    '''

    all_words = ['trzy suwaczki', 'czterdzieści dwa zameczki', 'mendel zapinek',
        'stos guziczków', 'sznur pętelek']

    def generate_data(self):
        rnd = random.Random()
        rnd.seed(self.seed)
        return rnd.sample(self.all_words, len(self.variable_names))


    def challenge(self):
        values = self.generate_data()
        template = self.get_template()
        out_templates = []
        for idx, var_name in enumerate(self.variable_names):
            out_templates.append(template.format(
                var_eq_data=format_data(var_name, values[idx])
            ))
        return ''.join(out_templates)


    def solutions(self):
        words = self.generate_data()
        return [''.join([''.join(item) for item in zip(*words)])]

