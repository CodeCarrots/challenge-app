# -*- coding: utf-8 -*-

import random

from ..task import Task, format_data


class ASubstituteOfTask(Task):
    '''
    Mając trzy zmienne (a, b i c) przechowujące wartości liczbowe (X, Y, Z)
    połącz je w ciąg postaci "aXbYcZaZbYcX". Przy wartościach typu
    zmiennoprzecinkowego obetnij część ułamkową.

    Przykład: a=1.1, b=2, c=3.4 -> "a1b2c3"
    '''

    template = '''\
    # dana
    {var_eq_data}
    '''

    title = "A substitute of..."

    success_msg = 'Jak widać: nie trzeba się było zbytnio wysilać'

    variable_names = ['a', 'b', 'c']

    def generate_data(self):
        rnd = random.Random()
        rnd.seed(self.seed)
        values = list(rnd.randrange(1e5, 1e10)
            for _ in range(len(self.variable_names)))
        for idx, val in enumerate(values):
            if rnd.randint(0, 1):
                values[idx] = float(val + rnd.randrange(1e5, 1e10) / 1e10)
        return values


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
        values = self.generate_data()
        return ['a{0}b{1}c{2}a{2}b{1}c{0}'.format(*map(int, values))]

