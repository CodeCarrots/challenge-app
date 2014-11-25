import random
import textwrap
import pprint
import markdown


def format_data(var_name, data):
    '''A helper function that returns the passed data (mostly) nicely
    formatted.
    '''

    tmp_var = ' ' * max(len(var_name) - 2, 0)
    var_template = '{var_name: <2} = {data}'
    pretty_data = pprint.pformat({tmp_var: data}, compact=True, indent=1)
    return var_template.format(var_name=var_name,
                               data=pretty_data[len(tmp_var)+5:-1])


# please note: the class doc string is the actual (MarkDown formatted)
# task description that the challenge app uses to present the task to
# users
class Task:
    '''Abstract task class. Please override me!'''

    # default template for the generated task python file
    template = '''\
    # dane wejściowe zadania
    {var_eq_data}
    '''

    # task's title - must be nicely set
    title = 'Unnamed task'

    # default variable name that will appear in the generated python
    # file as the variable to which the task challenge data is
    # assigned
    variable_name = 'data'

    # sequence of (HTML formatted) hints that will be (randomly) shown
    # to the user on a failed attempt
    hints = ['<strong>To nie jest poprawne rozwiązanie</strong>'
             ' - spróbuj jeszcze raz.']

    # the (HTML formatted) message to show to user on solving the
    # challenge
    success_msg = '<strong>Gratulacje</strong> - zadanie rozwiązane!'

    # this shouldn't be used
    has_challenge = True


    def __init__(self, seed):
        '''The seed (string) will be persistently unique for each user.'''

        self.seed = seed


    def get_template(self):
        '''This method is used by the default implementation of challenge()
        method to return the cleaned-up template for the task's
        generated python file.
        '''

        return textwrap.dedent(self.template)


    def generate_data(self):
        '''This method is used by the default implementation of challenge()
        method to generate the task's challenge data.

        Two different invocations of generate_data() should return the
        same data if self.seed is the same.
        '''

        return []


    def challenge(self):
        '''This method should return the content of a python file that will be
        offered to the user for downloading.

        The default implementation returns a simple "data = [...]"
        using template returned by self.get_template() and data
        returned by self.generate_data().
        '''

        data = self.generate_data()
        template = self.get_template()
        return template.format(
            var_eq_data=format_data(self.variable_name, data)
        )


    def get_hint(self, attempt):
        '''This method should return a failure message / hint. It gets passed
        the last user's attempt.
        '''

        return random.choice(self.hints)


    def success_message(self, solution):
        '''This method should return a success / congrats message. It gets
        passed the actual solution that user submitted.
        '''

        return self.success_msg


    def solutions(self):
        '''This method should return a sequence of valid solutions (think -
        synonyms) for the challenge returned by the challenge() method
        (for the currently set self.seed value).
        '''

        return []


    @classmethod
    def get_doc(cls):
        return textwrap.dedent(cls.__doc__)

    @classmethod
    def markdown_doc(cls):
        return markdown.markdown(cls.get_doc())
