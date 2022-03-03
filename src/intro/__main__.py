# import intro so i can get at the variables
from intro import __version__
from scoping import scoping as scoped

# or
# from intro import a file called readme, or anything declared.
from os import getcwd
from os.path import exists, dirname, join as osjoin

file_base = 'dev-dependencies.txt'


def main():

    wrong_file_path = getcwd() + '/dev-dependencies.txt'
    print(wrong_file_path)
    main_wd = dirname(__file__)
    print(main_wd)

    correct_file_path = osjoin(main_wd, 'dev-dependencies.txt')
    # __file__ gets me the current working dirname of the file getting run
    # wheras cwd gets me the current working directy of the executable.
    # which is right at the src.
    '''
    $ $HOME/$CODING_DIR/intro-to-ai-python/intro/intro/src/dev-dependencies.txt
    $ $HOME/$CODING_DIR/intro-to-ai-python/intro/intro/src/intro

    current working directory of the src vs current cwd of the main.
    '''
    print(exists(correct_file_path))
    file = open(correct_file_path)
    # reader = ''
    data = file.read()
    # reader += char
    print(data)
    print('-' * 10)

    file.close()

    with open(correct_file_path) as file:
        print(file.read(10))
        # the cursor reads and moves
        # when it picks up again, it is at offset10.
        datad = file.read()
        print(datad)
    collected = []
    with open(correct_file_path) as file:
        for line in file:

            collected.append(line.replace('\n', ''))
            # by default strip takes away the newline
            # also strip is edge only. if there are no
            # collected.append(line.strip('co')) will strip colorama to lorama but withotu that c, you never get to that o.

    print(collected)
    frank = 4
    with scoped():
        frank = 3
    try:
        assert frank == 2, "Tuple error message"
        # when you assert, you have to also add the error message
    except AssertionError as e:
        print('{}'.format(e), 'there is an assertion error')
    finally:
        print('prints regardless')


if __name__ == '__main__':
    main()
