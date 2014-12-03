import random
import string

from ..task import Task


def uniq_key(s):
    return ''.join(sorted(set(s)))


class AnagramsTask(Task):
    '''
    W zmiennej `anagrams` umieszczono wymieszaną listę anagramów
    różnych słów i fragmentów słów (oddzielonych znakiem
    odstępu). Wśród tych anagramów ukryte jest rozwiązanie.

    Any odnaleźć rozwiązanie należy:

    1. Pogrupować dane według oryginalnego słowa użytego do utworzenia
       anagramów. Innymi słowy - rozbić dane na rozłączne pozdzbiory
       takie że w ramach jednego takiego podzbioru każdy jego element
       jest anagramem każdego innego elementu tego podzbioru.
    2. Poszeregować te grupy według ich liczebności i wybrać
       _element środkowy_ (_medianę_).
    3. W wybranej grupie poszeregować anagramy według kolejności ich
       występowania w oryginalnej liście wszystkich anagramów i z tego
       szeregu ponownie wybrać _element środkowy_ - ten
       element będzie rozwiązaniem zadania.
    '''

    title = '!gnaraAmy'

    variable_name = 'anagrams'

    codewords = [
        'marchewkowo',
        'skonfudowany',
        'wielokrotnie',
        'siedmioliterowa',
        'abrakadabra',
        'abramakabra',
        'skomplikowani',
        'programowalny',
        'lampion',
        'beton',
        'figaro',
        'mozart',
        'chopin',
        'mruczek',
        'relatywni',
        'ambitne',
        'trapez',
        'poduszka',
        'marchew',
    ]

    template = '''\
    #############
    # !gnaraAmy #
    #############

    # "stóg" anagramów do przeszukania:
    {var_eq_data}
    '''

    success_msg = 'Znalezione!'


    fill_factor = 5
    grow_factor = 3

    def gen_similar(self, word):
        r = random.Random()
        r.seed(self.seed)

        len_min = len(word) - 2
        len_max = len(word)

        ret = {uniq_key(word): word}

        for _ in range(len(word) - 4):
            generated = r.sample(word, r.randrange(len_min, len_max))
            ret[uniq_key(generated)] = ''.join(generated)

        return ret

    def gen_anagrams(self, word, n):
        r = random.Random()
        r.seed(self.seed)

        count = len(word)
        return [''.join(r.sample(word, count)) for _ in range(n)]

    def generate_data(self):
        r = random.Random()
        r.seed(self.seed)
        code = r.choice(self.codewords)

        rest = set(self.codewords) - {code}

        data = []
        data2 = []

        noise = {}

        fill_words = r.sample(rest, self.fill_factor)

        for fill_word in r.sample(self.codewords, self.fill_factor):
            noise.update(self.gen_similar(fill_word))

        code_key = uniq_key(code)

        if code_key in noise:
            del noise[code_key]

        noise = list(noise.values())[:(len(noise) | 1) ^ 1]
        r.shuffle(noise)

        count = 5
        for word in noise[:len(noise) // 2]:
            count += r.randrange(1, self.grow_factor)
            data.append(word)
            data.extend(self.gen_anagrams(word, count))

        count += r.randrange(1, self.grow_factor)
        count = ((count | 1) ^ 1) + 2

        fill1 = self.gen_anagrams(code, count // 2)
        fill2 = self.gen_anagrams(code, count // 2)

        for word in noise[len(noise) // 2:]:
            count += r.randrange(1, self.grow_factor)
            data.append(word)
            data.extend(self.gen_anagrams(word, count))

        r.shuffle(data)

        ratio = r.randrange(1, len(data) * 3 // 4)

        data2 = data[ratio:]
        data = data[:ratio]

        data.extend(fill1)
        data2.extend(fill2)

        r.shuffle(data)
        r.shuffle(data2)

        data.append(code)
        data.extend(data2)

        return ' '.join(data)

    def solutions(self):
        r = random.Random()
        r.seed(self.seed)

        code = r.choice(self.codewords)
        return [code]
