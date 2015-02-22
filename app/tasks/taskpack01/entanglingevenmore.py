import random
import string

from ..task import Task, format_data


class EntanglingEvenMoreTask(Task):
    '''
    Mając dwa ciągi `ciag_a` (znaki) oraz `ciag_b` (cyfry) złóż je "na suwak"
    tak aby stworzyć układ: znak, liczba, znak, liczba, ..., znak (znak powinien
    być ostatnim elementem po ostatniej dostępnej cyfrze). Jeśli "dostępne znaki
    (`ciag_a`) się skończą" należy zacząć ponownie od pierwszego.

    Przykład:

        ciag_a="@->"
        ciag_b="12345"

        # wynik
        "@1-2>3@4-5>"`
    '''

    title = "Entangling even more"

    success_msg = 'Pomieszanie z poplątaniem ale... wyszło!'

    variable_names = ['ciag_a', 'ciag_b']

    template = '''\
    # dana
    {var_eq_data}
    '''

    def generate_data(self):
        rnd = random.Random()
        rnd.seed(self.seed)

        dist = 5
        signs = ''.join(rnd.sample(string.punctuation, dist))
        digits = ''.join([str(rnd.randint(1e10, 1e20)) for _ in range(dist)])

        return [signs, digits]

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
        signs, digits = self.generate_data()
        return [''.join([''.join(item) for item in list(zip(signs * len(digits),
            digits * 2))[:len(digits) + 1]])[:-1]]
