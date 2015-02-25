
'''Liczy statystyki zadan
'''

from optparse import make_option

from django.core.management.base import BaseCommand

from tasks.tasks import tasks as tasks_list
from tasks.models import UnlockedKey


class Command(BaseCommand):
    '''Glowna klasa zadaniowa (operacyjna)
    '''

    help = 'Liczy statystyki zadan'
    option_list = (
        make_option('-k', '--known-only',
            dest='known_only',
            action='store_true',
            default=False,
            help='statystyka tylko na bazie znanych kluczy zadan'),
    ) + BaseCommand.option_list

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)


    def handle(self, **options):

        users_stats_dc = {}
        for ukey in UnlockedKey.objects.all():
            key = ukey.key
            if key in users_stats_dc:
                users_stats_dc[key] += 1
            else:
                users_stats_dc[key] = 1

        all_keys = tasks_list.get_all_keys()

        known_only = options['known_only']

        row_fmt = '{0:20s}{1:10s}{2:6s}'
        row_sz = 36
        print(row_fmt.format('key', 'users #', 'known?') + '\n' + '=' * row_sz)
        for key in all_keys:
            known = False
            if known_only and key in users_stats_dc:
                known = True
            cnt = users_stats_dc.pop(key, 0)
            if not known_only or known:
                print(row_fmt.format(key, str(cnt),
                    str(known) if known_only else '-'))

        if users_stats_dc and not known_only:
            print('~' * row_sz)
            for key, cnt in users_stats_dc.items():
                print(row_fmt.format(key, str(cnt), '-'))


# vim: ts=4:sw=4:et:fdm=indent:ff=unix
