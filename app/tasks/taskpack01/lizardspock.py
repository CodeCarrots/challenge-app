import random

from ..task import Task


class LizardSpockTask(Task):
    '''
    Ktoś wpadł na "genialny" pomysł żeby zakodować rozwiązanie tego
    zadania niezbyt wyszukanym sposobem wykorzystującym grę [Papier,
    kamień, nożyce, jaszczurka, Spock](http://pl.wikipedia.org/wiki/Papier,_kamie%C5%84,_no%C5%BCyce,_jaszczurka,_Spock) (PKNJS).

    W wiadomości zakodowanej w zmiennej `message` poprawne wybory
    ruchu gry reprezentowane są przez następujące znaki:

    * __Kamień__: `k`, `a`, `f`, `m`, `u`, `z`;
    * __Nożyce__: `n`, `b`, `g`, `o`, `v`, ` ` (odstęp);
    * __Papier__: `p`, `c`, `h`, `q`, `w`, `,` (przecinek);
    * __Jaszczurka__: `j`, `d`, `i`, `r`, `x`, `-` (myślnik/minus);
    * __Spock__: `s`, `e`, `l`, `t`, `y`, `?` (znak zapytania).

    Każde kolejne dwa znaki ciągu `message` mogą zawierać:

    * dwa znaki reprezentujące ruchy gry PKNJS zgodnie z powyższymi
      listami - znak wygrywający zgodnie z regułami PKNJS jest częścią
      zakodowanego hasła,
    * jeden lub dwa znaki spoza wymienionych powyżej znaków
      reprezentujących ruchy gry - taka para znaków nie zawiera żadnej
      litery zakodowanego hasła.

    Odkodowane części zakodowanego hasła należy poskładać w kolejności
    występowania w wiadomości `message`.
    '''

    title = "Powrót Spock'a"

    passphrases = [
        'za rok, w tym samym miejscu',
        'jutro, o tej samej porze?',
        'wtorek - trzynastego',
        'sto siedem i trzy czwarte',
        'marchewkowe programowanie',
        'sosna, siedemnasta wiosna',
        'wszystko zgodnie z planem',
    ]

    template = '''\
    ##################
    # Powrót Spock'a #
    ##################

    # listy alternatywnych znaków dla danych ruchów, zgodnie z treścią
    # zadania:
    moves_K = 'kafmuz'
    moves_N = 'nbgov '
    moves_P = 'pchqw,'
    moves_J = 'jdirx-'
    moves_S = 'selty?'

    # zakodowana wiadomość:
    {var_eq_data}
    '''

    variable_name = 'message'

    success_msg = 'Oczywiście, właśnie tak.'

    stretch_factor = 9

    neutral = '+=~*@$#%^'
    synonyms = {
        'k': 'kafmuz',
        'n': 'nbgov ',
        'p': 'pchqw,',
        'j': 'jdirx-',
        's': 'selty?',
    }
    reverse = {c: move
               for (move, syns) in synonyms.items()
               for c in syns}
    # key beats any of the values
    loses = {
        'k': 'nj',
        'n': 'pj',
        'p': 'ks',
        'j': 'ps',
        's': 'kn',
    }

    def generate_data(self):
        r = random.Random()
        r.seed(self.seed)
        code = r.choice(self.passphrases)

        return self._encode(code)

    def _encode(self, msg):
        neutral = self.neutral
        synonyms = self.synonyms
        moves = list(synonyms.keys())
        reverse = self.reverse
        loses = self.loses

        r = random.Random()
        r.seed(self.seed)

        stretched = [None] * r.randrange(0, self.stretch_factor)

        for c in msg:
            stretched.append(c)
            stretched.extend([None] * r.randrange(0, self.stretch_factor))

        last = r.choice(synonyms[r.choice(moves)])
        coded = [last]

        while stretched:
            c = stretched[0]
            last_move = reverse[last]
            if c is None:
                # select a drawing c2 here (always possible) or inject
                # a neutral
                last = r.choice(synonyms[last_move])
                # inject a neutral char sometimes
                if r.randrange(0, 10) == 0:
                    coded.append(r.choice(neutral))
                stretched.pop(0)
            elif c == last:
                # select a losing c2 here (always possible)
                last = r.choice(synonyms[r.choice(loses[last_move])])
                stretched.pop(0)
            else:
                # c needs to be winning with last here (not always
                # immediately possible)
                c_move = reverse[c]
                if c_move in loses[last_move]:
                    last = c
                    coded.append(r.choice(neutral))
                elif c in synonyms[last_move]:
                    # inject c as a draw here
                    last = c
                else:
                    # c wins here
                    last = c
                    stretched.pop(0)

            coded.append(last)

        return ''.join(coded)

    def solutions(self):
        r = random.Random()
        r.seed(self.seed)
        code = r.choice(self.passphrases)
        return [code]
