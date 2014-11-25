challenge-app
=============

Aplikacja wspomagająca zadaniowe sesje CodeCarrots.


Wymagania
---------

Python 3.x (testowane z 3.4). Następnie:

      $ pip install -r requirements.txt


Uruchomienie
------------

Przed uruchomieniem należy zainicjować zmienną środowiskową
`SECRET_KEY` (wartością którą django zazwyczaj generuje przy tworzeniu
projektu i umieszcza w pliku `settings.py`).

      $ export SECRET_KEY=...
      $ cd app
      $ python ./manage.py migrate
      $ python ./manage.py runserver
