'''
Name Generators: By msharp

This file will contain all varients of my original name generator, originally
a bash script I created to practice bash back in 2017. The premise was to
generate names only by choosing a random next character based on the last character.

The original script was about 80 lines long, and in 2025 when I decided to transfer
it to python, I realized it only took about 3 lines to do so, which made me wonder
how I could make it even more compact. This file is the list of iterations on
that single function. Each name_generator function will have a number to show
which version it is, and the docstring will describe the changes made in that version.
'''
import random
import string


# Original next char dict.
# Key is previous letter
# Value is list of letters which could come after the previous letter in any context
next_char = {
    'a': 'abcdefghijklmnopqrstuvwxyz',
    'b': 'aeiloru',
    'c': 'aehikloruyz',
    'd': 'aeijoruy',
    'e': 'abcdefghijklmnpqrstvwxyz',
    'f': 'aeiloru',
    'g': 'aehiloruy',
    'h': 'aeiouy',
    'i': 'abcdefgjklmnopqrstvwz',
    'j': 'aeiou',
    'k': 'aeilnoruy',
    'l': 'aeilou',
    'm': 'aeiouy',
    'n': 'aeiou',
    'o': 'abcdefghijklmnopqrstuvwxyz',
    'p': 'aehilmnorsuy',
    'q': 'u',
    'r': 'aeiouy',
    's': 'acehiklmnopqrstuw',
    't': 'aehioruy',
    'u': 'abcdefghijklmnoprstvwxyz',
    'v': 'aeiou',
    'w': 'aehioru',
    'x': 'aeir',
    'y': 'aeiou',
    'z': 'aeiou',
}

def name_generator1( min_length=3, weight=0.7 ):
    '''
    Simplification of an old name generator I made for programming practice.
    Generates names by first choosing a length, and then picking a random character.
    The next character is randomly picked from a list character that might go after
    the previous character. Nothing more complicated is done.

    This generates some very fantacy like names, albiet sometimes hard to say. The
    next character list was made by finding what chars could come after the key char
    in almost any context without being too jarring to say. This was tweaked a bit
    after running it multiple times to remove characters that seemed to produce
    names that were too hard to say or wacky. This means that some real world names
    are impossible to make simply because they may have an instance of character
    pairs which are too context dependent, and can't exist in any random location
    inside a word or name. I have nothing at all against those names, my name is
    one of them. It just means your name is unique thats all.

    Current parameters are that this only generates names between 3 and 9 chars, just
    for simplicities sake. It also favors lengths 5 and 7 because of the weight value.
    '''
    name = ''
    for idx in range( -1, int((random.randint(1,9) * weight) + min_length) - 1 ):
        name += random.choice( next_char.get( name[idx:], string.ascii_lowercase ) )
    return name.title()


def name_generator2( min_length=3, weight=0.7 ):
    '''Generates a random var first to remove need for weird -1 index at beginning'''
    name = random.choice(string.ascii_lowercase)
    for idx in range( int((random.randint(1,9) * weight) + min_length) ):
        name += random.choice( next_char.get( name[idx], string.ascii_lowercase ) )
    return name.title()


def name_generator3( min_length=3, weight=0.7 ):
    '''
    Converts to list by using tuple to do two actions per iteration.
    First index adds latest char to the char list, second index builds
    name string from list of chars. it will do this each iteration so
    at the end we just have to pull the last index from the list, which
    will contain the list of chars and the name string, then we just pull
    the name out of that tuple.
    '''
    name = [random.choice(string.ascii_lowercase)]
    name = [
        ( name.append(char),''.join(name).title())
        for idx in range( int((random.randint(1,9) * weight) + min_length) )
        for char in random.choice( next_char.get( name[idx], string.ascii_lowercase ) )
    ]
    return name[-1][1]


def name_generator4( min_length=3, weight=0.7 ):
    '''
    Converts to first oneline version by making use of variable definition allowed
    by list comprehension when you do a for loop on a list of length 1.
    '''
    return [
        e for name in ([random.choice(string.ascii_lowercase)],) for e in [
            (''.join(name).title(), name.append(char))
            for idx in range( int((random.randint(1,9) * weight) + min_length) )
            for char in random.choice( next_char.get( name[idx], string.ascii_lowercase ) )
        ]
    ][-1][0]

if __name__ == '__main__':
    print( 'Name Generator V4:' )
    print( name_generator4() )