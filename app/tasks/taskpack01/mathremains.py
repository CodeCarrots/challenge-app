# -*- coding: utf-8 -*-

import random

import markdown
import textwrap

from ..task import Task, format_data


class MathRemainsTask(Task):
    '''
    Mając dane wartości zmiennych (a, b, ..., f) oraz wyrażenie w postaci wzoru
    (poniżej) - wylicz wartość wyrażenia. Odpowiedzią jest część ułamkowa
    wyniku.

    $${}$$
    '''

    template = '''\
    # dana
    {var_eq_data}
    '''

    title = "Math remains"

    success_msg = 'Trochę matematyki ale chyba nikt się nie zgubił?'

    variable_names = ['a', 'b', 'c', 'd', 'e', 'f']

    def _get_raw_data(self, rnd):
        '''Returns sample variables and formula (no eval checks performed!)
        '''
        values = list(rnd.randrange(1e0, 1e1)
            for _ in range(len(self.variable_names)))
        ops = ['+', '-', '*', '/', '**']
        vals = rnd.sample(''.join(self.variable_names) * 10, len(ops) + 1)

        lst = []
        for val, oper in zip(vals, rnd.sample(ops, len(ops))):
            lst.extend([val, oper])
        lst.pop()
        try:
            div_pos = lst.index('/')
            lst.insert(div_pos, ')')
            lst.insert(div_pos + 2, '(')
            lst.insert(0, '(')
            lst.append(')')
        except ValueError:
            pass
        formula = ''.join(lst)
        return (values, formula)


    def _check_values(self, values, py_formula):
        '''Checks formula against values
        '''
        values_dc = {var_name: values[idx]
            for idx, var_name in enumerate(self.variable_names)}
        try:
            return eval(py_formula, {}, values_dc)
        except ArithmeticError:
            return None


    def _py2md_math(self, py_formula):
        '''Converts Python formula to Markdown/MathJax
        '''
        return py_formula.replace('(', '').replace(')', '')\
            .replace('**', '^').replace('/', ' \\over ')


    def generate_data(self):
        rnd = random.Random()
        rnd.seed(self.seed)
        while True:
            values, py_formula = self._get_raw_data(rnd)
            evaluated = self._check_values(values, py_formula)
            if evaluated is not None:
                md_formula = self._py2md_math(py_formula)
                return [values, py_formula, evaluated, md_formula]


    def challenge(self):
        values, _, _, _ = self.generate_data()
        template = self.get_template()
        out_templates = []
        for idx, var_name in enumerate(self.variable_names):
            out_templates.append(template.format(
                var_eq_data=format_data(var_name, values[idx])
            ))
        return ''.join(out_templates)


    def solutions(self):
        _, _, evaluated, _ = self.generate_data()
        return [str(evaluated)]


    def get_doc(self):
        _, _, _, md_formula = self.generate_data()
        start = '$${'
        stop = '}$$'
        return textwrap.dedent(self.__doc__.replace(start + stop,
            start + md_formula + stop))


    def markdown_doc(self):
        return markdown.markdown(self.get_doc())

