import random
import string
import itertools

from ..task import Task


class DictWormTask(Task):
    '''
    W tym zadaniu dany jest słownik `codedict` mapujący napisy
    dwuznakowe na dwuelementowe krotki napisów dwuznakowych -
    zakodowane zostało w nim hasło które jest rozwiązaniem zadania.

    Aby znaleźć zakodowane hasło należy "przejść" po słowniku,
    rozpoczynając od klucza `'aa'`, podążając za odpowiednimi
    elementami krotek wartości:

    * części zakodowanego hasła zawsze znajdują się w elementach na
      pozycji `1` - w tych krotkach element `0`-wy zawiera klucz
      kolejnego elementu "ścieżki" kodującej hasło,
    * pomocnicze elementy "ścieżki" to krotki które nie zawierają
      części hasła:
        - w elemencie na pozycji `0` zawierają napis który nie jest
          poprawnym kluczem w danym słowniku,
        - w elemencie o indeksie `1` wskazują kolejny fragment ścieżki
          lub sygnalizują koniec "ścieżki" kodującej hasło jeżeli są
          napisem który nie jest kluczem żadnej wartości w danym
          słowniku.

    Znalezione fragmenty hasła należy połączyć w kolejności podążania
    "ścieżką" kodującą dane hasło.

    Dla przykładu, hasło `"kod"` mógłby kodować następujący słownik:

        codedict = {'dd': ('yy', 'zz'), 'ee': ('ff', 'gg'), 'cc': ('dd', 'd '),
                    'aa': ('bb', 'ko'), 'bb': ('xx', 'cc')}

    Ze ścieżką prowadzącą przez klucze `'aa'` -> `'bb'` -> `'cc'` -> `'dd'`.
    '''

    title = 'Mól słownikowy'

    template = '''\
    ##################
    # Mól słownikowy #
    ##################

    # W tym zadaniu nie potrzebne są żadne dodatkowe biblioteki
    # wystarczy sam zakodowany słownik:
    {var_eq_data}
    '''

    codewords = [
        'programowalny',
        'marchewkowo',
        'skonfudowany',
        'wielokrotnie',
        'siedmioliterowa',
        'abrakadabra',
        'abramakabra',
        'skomplikowani',
    ]

    variable_name = 'codedict'

    success_msg = 'Słownik kodowy przegryziony!'

    hints = ['<strong>*tuuu* *tyy* *ti*</strong>...'
             ' Nie ma takiego rozwiązania!']

    stretch_factor = 7

    def generate_data(self):
        r = random.Random()
        r.seed(self.seed)
        codeword = r.choice(self.codewords)
        if len(codeword) % 2:
            codeword += ' '

        chars_1 = string.ascii_lowercase
        chars_2 = string.ascii_lowercase + ' '

        stretched = [None] * r.randrange(0, self.stretch_factor)

        for dg in (codeword[i:i+2] for i in range(0, len(codeword), 2)):
            stretched.append(dg)
            stretched.extend([None] * r.randrange(0, self.stretch_factor))

        stretched.append(None)

        dgs = [a + b for a, b in itertools.product(chars_1, chars_2)]

        r.shuffle(dgs)

        key = 'aa'
        data = {}
        for dg in stretched:
            new_key = dgs.pop()
            if dg is None:
                data[key] = (dgs.pop(), new_key)
            else:
                data[key] = (new_key, dg)
            key = new_key

        for _ in range(r.randrange(50, 80)):
            data[dgs.pop()] = (r.choice(chars_1) + r.choice(chars_2),
                               r.choice(chars_1) + r.choice(chars_2))

        return data

    def solutions(self):
        r = random.Random()
        r.seed(self.seed)
        codeword = r.choice(self.codewords)
        return [codeword]
