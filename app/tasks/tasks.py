import random

from collections import OrderedDict as odict

from .task import Task


class TaskList:
    def __init__(self, all_tasks, user_keys=()):
        self._keys = odict((lock, key) for lock, _cls, key in all_tasks)
        self._tasks = {key: (cls, lock) for lock, cls, key in all_tasks}

    def __contains__(self, key):
        return key in self._tasks

    def get_task_key(self, lock):
        return self._keys[lock]

    def get_task_lock(self, key):
        return self._tasks[key][1]

    def get_task(self, key):
        return self._tasks[key][0]

    def get_user_tasks(self, user_keys):
        user_keys = set(user_keys)
        user_tasks = []
        for lock, key in self._keys.items():
            if lock not in user_keys:
                continue
            cls = self._tasks[key][0]
            user_tasks.append({'unlocked': key in user_keys,
                               'title': cls.title,
                               'key': key})
        return user_tasks


START_KEY = '_start'


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


class WellDone(Task):
    '''
    Na razie nie ma więcej zadań do rozwiązania ale możesz rozejrzeć
    się czy ktoś inny nie potrzebuje pomocy.

    Możesz również wrócić do poprzednich zadań i zastanowić się czy
    Twoje rozwiązania można jakoś ulepszyć. Oczywiście, możesz również
    spróbować zmierzyć się z wyzwaniami ze strony [Python
    Challenge](http://www.pythonchallenge.com/)...
    '''

    title = 'Gratulacje!'

    has_challenge = False


from .taskpack01.onlydots import OnlyDotsTask
from .taskpack01.orderchaos import OrderedChaosTask
from .taskpack01.foldnfind import FoldNFindTask
from .taskpack01.dictworm import DictWormTask

tasks = TaskList([
    (START_KEY, SumNSliceTask, 'sumnslice'),
    ('sumnslice', OnlyDotsTask, 'onlydots'),
    ('onlydots', OrderedChaosTask, 'orderchaos'),
    ('orderchaos', FoldNFindTask, 'foldnfind'),
    ('foldnfind', DictWormTask, 'dictworm'),
    # ...
    ('dictworm', WellDone, 'welldone'),
])
