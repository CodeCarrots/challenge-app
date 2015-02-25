# -*- coding: utf-8 -*-

import random

from ..task import Task, format_data


class ASubstituteOfTask(Task):
    '''
    Mając trzy zmienne (a, b i c) przechowujące wartości liczbowe (x, y, z)
    połącz je w ciąg znaków postaci "@x&y^z@z&y^x". Przekształć liczby zmiennoprzecinkowe
    na całkowite jeżeli będzie taka potrzeba.

    Przykład:

        a=111
        b=222.2
        c=333.444

        # wynik:
        '@111&222^333@333&222^111'
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
        return ['@{0}&{1}^{2}@{2}&{1}^{0}'.format(*map(int, values))]
