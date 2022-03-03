# import intro so i can get at the variables
from intro import mario, __version__

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
    char = file.read()
    # reader += char
    file.close()

    print(mario, __version__, char)


if __name__ == '__main__':
    main()
