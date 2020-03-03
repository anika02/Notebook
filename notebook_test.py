import sys
from notebook import Notebook, Note
from menu import Menu


if __name__ == "__main__":

    print('___'*30)

    n1 = Note("hello first")
    n2 = Note("hello again")
    print('\nClass Note')
    print('ID of the first note:', n1.id)  # 1
    print('ID of the second note:', n2.id)  # 2
    print('Function match, the first note:', n1.match('hello'))  # True
    print('Function match, the second note:', n2.match('second'))  # False
    print('\ndir, class Note:', dir(Note))
    print('\ndir, the first note:', dir(n1))
    print("\ndir, n1.match", dir(n1.match))
    print('\nn1 is Note:', isinstance(n1, Note))
    print('n1 is object:', isinstance(n1, object))
    print('type of n1.id:', type(n1.id))
    print('type of n1.tags:', type(n1.tags))
    print('type of n1.creation_date:', type(n1.creation_date))
    print('\ndict of n1:', n1.__dict__)

    print('___'*30)

    n = Notebook()
    n.new_note("hello world")
    n.new_note("hello again")
    print('\nClass Notebook')
    print('n.notes:', n.notes)
    print('id of the 0th note:', n.notes[0].id)
    print('id of the 1st note:', n.notes[1].id)
    print('message of the 0th note:', n.notes[0].memo)
    print("Function search (n.search('hello')):", n.search('hello'))
    print("Function search (n.search('world')):", n.search('world'))
    n.modify_memo(1, "h1 world")
    print("Modified message of the 0th note", n.notes[0].memo)
    print('\ndir, class Notebook:', dir(Notebook))
    print('\ndir, n:', dir(n))
    print("\ndir, n.new_note / n._find_note / n.modify_memo\
 / n.modify_tags / n.search:\n", dir(n.new_note))
    print('\nn is Notebook:', isinstance(n, Notebook))
    print('n is object:', isinstance(n, object))
    print('type of n.notes:', type(n.notes))
    print('\ndict of n:', n.__dict__)

    print('___'*30)

    a = Menu()
    print('\nClass Menu')
    print('\ndir, class Menu:', dir(Menu))
    print('\ndir, a:', dir(a))
    print("\ndir, a.display_menu / a.run / a.show_notes / \
a.search_notes / a.add_note / a.modify_note / a.quit:\n", dir(a.display_menu))
    print('\na is Menu:', isinstance(a, Menu))
    print('a is object:', isinstance(a, object))
    print('type of a.notebook:', type(a.notebook))
    print('type of a.choices:', type(a.choices))
    print('\ndict of a:', a.__dict__)

    print('___'*30)
