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


def name_generator5( min_length=3, weight=0.7 ):
    '''rearanges list comp to not be nested.'''
    return [
        (
            ''.join( name ),
            name.append(random.choice(next_char.get( name[idx], string.ascii_letters)))
        )
        for name in [[string.ascii_letters[random.randint(0,25)]]]
        for idx in range(int((random.randint(1,9) * weight) + min_length))
    ][-1][0].title()


def name_generator6( min_length=3, weight=0.7 ):
    '''
    removes string import and also moves to not use externally defined next_char dictionary
    since the goal is now to make a 100% self contained method. only thing left to remove is
    the random import
    '''
    return [
        (
            ''.join( name ),
            name.append(
                {
                    'a': 'abcdefghijklmnopqrstuvwxyz', 'b': 'aeiloruaeiloruaeiloruaeilo', 'c': 'aehikloruyzaehikloruyzaehi', 'd': 'aeijoruyaeijoruyaeijoruyae', 'e': 'abcdefghijklmnpqrstvwxyzab', 'f': 'aeiloruaeiloruaeiloruaeilo', 'g': 'aehiloruyaehiloruyaehiloru', 'h': 'aeiouyaeiouyaeiouyaeiouyae', 'i': 'abcdefgjklmnopqrstvwzabcde', 'j': 'aeiouaeiouaeiouaeiouaeioua', 'k': 'aeilnoruyaeilnoruyaeilnoru', 'l': 'aeilouaeilouaeilouaeilouae', 'm': 'aeiouyaeiouyaeiouyaeiouyae', 'n': 'aeiouaeiouaeiouaeiouaeioua', 'o': 'abcdefghijklmnopqrstuvwxyz', 'p': 'aehilmnorsuyaehilmnorsuyae', 'q': 'uuuuuuuuuuuuuuuuuuuuuuuuuu', 'r': 'aeiouyaeiouyaeiouyaeiouyae', 's': 'acehiklmnopqrstuwacehiklmn', 't': 'aehioruyaehioruyaehioruyae', 'u': 'abcdefghijklmnoprstvwxyzab', 'v': 'aeiouaeiouaeiouaeiouaeioua', 'w': 'aehioruaehioruaehioruaehio', 'x': 'aeiraeiraeiraeiraeiraeirae', 'y': 'aeiouaeiouaeiouaeiouaeioua', 'z': 'aeiouaeiouaeiouaeiouaeioua',
                }.get( name[idx], 'abcdefghijklmnopqrstuvwxyz')[random.randint(0,25)]
            )
        )
        for name in [['abcdefghijklmnopqrstuvwxyz'[random.randint(0,25)]]]
        for idx in range(int((random.randint(1,9) * weight) + min_length))
    ][-1][0].title()


def name_generator7(i=0):
    '''
    This iteration uses a Wichmann-Hill type PRNG to remove need for any imported modules

    The WH implementation chosen here is derived from this comment:
    https://stackoverflow.com/a/23374109/11234513

    My implementation attempted to use this without a class. But this version introduces
    a bug which can be seen if this is ran given a range of numbers from 0 - 100. The
    names it generates will often repeat or be extremely similar for every set of 5 names.
    This is due to the fact that the first value produced from the WH PRNG after seed
    seems to be a linear value which will go from 0-175 and then repeat. The prng below is
    updated a handlful of times when the name is being generated, but the starting value is
    only slightly different from the previous, so names are bound to look similar. This bug
    wasn't noticed until a few iterations later even though its so obvious, I had only
    tested it with single randomly chosen numbers.
    '''
    return [
        (''.join( name ),
        name.append({'a': 'abcdefghijklmnopqrstuvwxyz', 'b': 'aeiloruaeiloruaeiloruaeilo', 'c': 'aehikloruyzaehikloruyzaehi', 'd': 'aeijoruyaeijoruyaeijoruyae', 'e': 'abcdefghijklmnpqrstvwxyzab', 'f': 'aeiloruaeiloruaeiloruaeilo', 'g': 'aehiloruyaehiloruyaehiloru', 'h': 'aeiouyaeiouyaeiouyaeiouyae', 'i': 'abcdefgjklmnopqrstvwzabcde', 'j': 'aeiouaeiouaeiouaeiouaeioua', 'k': 'aeilnoruyaeilnoruyaeilnoru', 'l': 'aeilouaeilouaeilouaeilouae', 'm': 'aeiouyaeiouyaeiouyaeiouyae', 'n': 'aeiouaeiouaeiouaeiouaeioua', 'o': 'abcdefghijklmnopqrstuvwxyz', 'p': 'aehilmnorsuyaehilmnorsuyae', 'q': 'uuuuuuuuuuuuuuuuuuuuuuuuuu', 'r': 'aeiouyaeiouyaeiouyaeiouyae', 's': 'acehiklmnopqrstuwacehiklmn', 't': 'aehioruyaehioruyaehioruyae', 'u': 'abcdefghijklmnoprstvwxyzab', 'v': 'aeiouaeiouaeiouaeiouaeioua', 'w': 'aehioruaehioruaehioruaehio', 'x': 'aeiraeiraeiraeiraeiraeirae', 'y': 'aeiouaeiouaeiouaeiouaeioua', 'z': 'aeiouaeiouaeiouaeiouaeioua',
                    }.get( name[idx], 'abcdefghijklmnopqrstuvwxyz')[int(((((171*seed[0]) % 30269)/30269.0 + ((172 * seed[1]) % 30307)/30307.0 + ((170 * seed[2]) % 30323)/30323.0)%1)*25)]
        ),
        seed.extend([(171*seed[0]) % 30269, (172 * seed[1]) % 30307, (170 * seed[2]) % 30323]),
        seed.pop(0),seed.pop(0),seed.pop(0) )
        for seed
        in [[int( divmod((i + 1)*10_000_000_000_000_000, 30268)[1] ) + 1, int(  divmod( divmod((i + 1)*10_000_000_000_000_000, 30268)[0],30306)[1] ) + 1, int( divmod(divmod(divmod((i + 1)*10_000_000_000_000_000, 30268)[0],30306)[0],30322)[1]) + 1]]
        for name
        in [['abcdefghijklmnopqrstuvwxyz'[int(((((171*seed[0]) % 30269)/30269.0 + ((172 * seed[1]) % 30307)/30307.0 + ((170 * seed[2]) % 30323)/30323.0)%1)*25)]]]
        for idx
        in range( int( ( [1,2,3,4,5,5,6,7,8,9][int(((((171*seed[0]) % 30269)/30269.0 + ((172 * seed[1]) % 30307)/30307.0 + ((170 * seed[2]) % 30323)/30323.0)%1)*10)] * 0.7 ) + 3))
    ][-1][0].title()


def name_generator8( i=0 ):
    '''
    Removes the idx var which also removes the need for range.
    This is the first 100% self contained method, only making use of types.
    '''
    return [
        (
            ''.join( name ),
            name.append({'a': 'abcdefghijklmnopqrstuvwxyz', 'b': 'aeiloruaeiloruaeiloruaeilo', 'c': 'aehikloruyzaehikloruyzaehi', 'd': 'aeijoruyaeijoruyaeijoruyae', 'e': 'abcdefghijklmnpqrstvwxyzab', 'f': 'aeiloruaeiloruaeiloruaeilo', 'g': 'aehiloruyaehiloruyaehiloru', 'h': 'aeiouyaeiouyaeiouyaeiouyae', 'i': 'abcdefgjklmnopqrstvwzabcde', 'j': 'aeiouaeiouaeiouaeiouaeioua', 'k': 'aeilnoruyaeilnoruyaeilnoru', 'l': 'aeilouaeilouaeilouaeilouae', 'm': 'aeiouyaeiouyaeiouyaeiouyae', 'n': 'aeiouaeiouaeiouaeiouaeioua', 'o': 'abcdefghijklmnopqrstuvwxyz', 'p': 'aehilmnorsuyaehilmnorsuyae', 'q': 'uuuuuuuuuuuuuuuuuuuuuuuuuu', 'r': 'aeiouyaeiouyaeiouyaeiouyae', 's': 'acehiklmnopqrstuwacehiklmn', 't': 'aehioruyaehioruyaehioruyae', 'u': 'abcdefghijklmnoprstvwxyzab', 'v': 'aeiouaeiouaeiouaeiouaeioua', 'w': 'aehioruaehioruaehioruaehio', 'x': 'aeiraeiraeiraeiraeiraeirae', 'y': 'aeiouaeiouaeiouaeiouaeioua', 'z': 'aeiouaeiouaeiouaeiouaeioua',
                        }[name[-1]][int(((((171*seed[0]) % 30269)/30269.0 + ((172 * seed[1]) % 30307)/30307.0 + ((170 * seed[2]) % 30323)/30323.0)%1)*25)]
            ),
            seed.extend([(171*seed[0]) % 30269, (172 * seed[1]) % 30307, (170 * seed[2]) % 30323]),
            seed.pop(0),seed.pop(0),seed.pop(0)
        )
        for seed
        in [[int( divmod((i + 1)*10_000_000_000_000_000, 30268)[1] ) + 1, int(  divmod( divmod((i + 1)*10_000_000_000_000_000, 30268)[0],30306)[1] ) + 1, int( divmod(divmod(divmod((i + 1)*10_000_000_000_000_000, 30268)[0],30306)[0],30322)[1]) + 1]]
        for name
        in [['abcdefghijklmnopqrstuvwxyz'[int(((((171*seed[0]) % 30269)/30269.0 + ((172 * seed[1]) % 30307)/30307.0 + ((170 * seed[2]) % 30323)/30323.0)%1)*25)]]]
        for _
        in [0]*int( ( [1,2,3,4,5,5,6,7,8,9][int(((((171*seed[0]) % 30269)/30269.0 + ((172 * seed[1]) % 30307)/30307.0 + ((170 * seed[2]) % 30323)/30323.0)%1)*10)] * 0.7 ) + 3)
    ][-1][0].title()


def name_generator9( i=0 ):
    '''
    uses a lambda function for PRNG wrapping, this removes a lot of
    repeated code and shrinks the function a bit.
    '''
    return [
        (
            ''.join( name ),
            name.append({'a': 'abcdefghijklmnopqrstuvwxyz', 'b': 'aeiloruaeiloruaeiloruaeilo', 'c': 'aehikloruyzaehikloruyzaehi', 'd': 'aeijoruyaeijoruyaeijoruyae', 'e': 'abcdefghijklmnpqrstvwxyzab', 'f': 'aeiloruaeiloruaeiloruaeilo', 'g': 'aehiloruyaehiloruyaehiloru', 'h': 'aeiouyaeiouyaeiouyaeiouyae', 'i': 'abcdefgjklmnopqrstvwzabcde', 'j': 'aeiouaeiouaeiouaeiouaeioua', 'k': 'aeilnoruyaeilnoruyaeilnoru', 'l': 'aeilouaeilouaeilouaeilouae', 'm': 'aeiouyaeiouyaeiouyaeiouyae', 'n': 'aeiouaeiouaeiouaeiouaeioua', 'o': 'abcdefghijklmnopqrstuvwxyz', 'p': 'aehilmnorsuyaehilmnorsuyae', 'q': 'uuuuuuuuuuuuuuuuuuuuuuuuuu', 'r': 'aeiouyaeiouyaeiouyaeiouyae', 's': 'acehiklmnopqrstuwacehiklmn', 't': 'aehioruyaehioruyaehioruyae', 'u': 'abcdefghijklmnoprstvwxyzab', 'v': 'aeiouaeiouaeiouaeiouaeioua', 'w': 'aehioruaehioruaehioruaehio', 'x': 'aeiraeiraeiraeiraeiraeirae', 'y': 'aeiouaeiouaeiouaeiouaeioua', 'z': 'aeiouaeiouaeiouaeiouaeioua',
                        }[name[-1]][int(prng(seed)*25)]
            ),
            seed.extend([(171*seed[0]) % 30269, (172 * seed[1]) % 30307, (170 * seed[2]) % 30323]),
            seed.pop(0),seed.pop(0),seed.pop(0)
        )
        for seed in [[int( divmod((i + 1)*1_000_000_000_000_000, 30268)[1] ) + 1, int(  divmod( divmod((i + 1)*1_000_000_000_000_000, 30268)[0],30306)[1] ) + 1, int( divmod(divmod(divmod((i + 1)*1_000_000_000_000_000, 30268)[0],30306)[0],30322)[1]) + 1]]
        for prng in [lambda s:((((171*s[0]) % 30269)/30269.0 + ((172 * s[1]) % 30307)/30307.0 + ((170 * s[2]) % 30323)/30323.0)%1)]
        for name
        in [['abcdefghijklmnopqrstuvwxyz'[int(prng(seed)*25)]]]
        for _
        in [0]*int( ( [1,2,3,4,5,5,6,7,8,9][int(prng(seed)*10)] * 0.7 ) + 3)
    ][-1][0].title()


def name_generator10( i=0 ):
    '''
    fixes issue with prng producing what feels like repeating names every 5 names by running the prng a few cycles first before using it.
    The issue arises from the fact that the first number the prng generates after being seeded is linear up to 175 where it goes back to
    zero and then repeats. So the first value pulled from the prng will be repeatable, and since we only pull from the prng a handful of
    times, and we arent running far from the seed, we end up with what looks someone like name generation with a fractal nature. To see
    this issue, run
    '''
    return [
        (
            name.append(
                {
                    'a': 'abcdefghijklmnopqrstuvwxyz',
                    'b': 'aeiloruaeiloruaeiloruaeilo',
                    'c': 'aehikloruyzaehikloruyzaehi',
                    'd': 'aeijoruyaeijoruyaeijoruyae',
                    'e': 'abcdefghijklmnpqrstvwxyzab',
                    'f': 'aeiloruaeiloruaeiloruaeilo',
                    'g': 'aehiloruyaehiloruyaehiloru',
                    'h': 'aeiouyaeiouyaeiouyaeiouyae',
                    'i': 'abcdefgjklmnopqrstvwzabcde',
                    'j': 'aeiouaeiouaeiouaeiouaeioua',
                    'k': 'aeilnoruyaeilnoruyaeilnoru',
                    'l': 'aeilouaeilouaeilouaeilouae',
                    'm': 'aeiouyaeiouyaeiouyaeiouyae',
                    'n': 'aeiouaeiouaeiouaeiouaeioua',
                    'o': 'abcdefghijklmnopqrstuvwxyz',
                    'p': 'aehilmnorsuyaehilmnorsuyae',
                    'q': 'uuuuuuuuuuuuuuuuuuuuuuuuuu',
                    'r': 'aeiouyaeiouyaeiouyaeiouyae',
                    's': 'acehiklmnopqrstuwacehiklmn',
                    't': 'aehioruyaehioruyaehioruyae',
                    'u': 'abcdefghijklmnoprstvwxyzab',
                    'v': 'aeiouaeiouaeiouaeiouaeioua',
                    'w': 'aehioruaehioruaehioruaehio',
                    'x': 'aeiraeiraeiraeiraeiraeirae',
                    'y': 'aeiouaeiouaeiouaeiouaeioua',
                    'z': 'aeiouaeiouaeiouaeiouaeioua',
                }[name[-1]][int(prng(seed)*25)]
            ),
            ''.join( name ),
            seed.extend([(171*seed[0]) % a, (172 * seed[1]) % b, (170 * seed[2]) % c]),
            seed.pop(0),seed.pop(0),seed.pop(0)
        )
        for a in [30269] for b in [30307] for c in [30323]
        for ix in [divmod((i + 1)*1_000_000_000_000_000, a-1)]
        for iy in [divmod(ix[0],b-1)]
        for iz in [divmod(iy[0],c-1)]
        for seed in [[int(ix[1])+1, int(iy[1])+1, int(iz[1])+1]]
        for prng in [
            lambda s: [
                    (
                    (
                        (((171 * s[0]) % a) / a + ((172 * s[1]) % b) / b + ((170 * s[2]) % c) / c) % 1
                    ),
                    s.extend([(171 * s[0]) % a, (172 * s[1]) % b, (170 * s[2]) % c]),
                    s.pop(0),s.pop(0),s.pop(0)
                    )
                    for _ in [0] * ((
                        int(
                            (((171 * s[0]) % a) / a + ((172 * s[1]) % b) / b + ((170 * s[2]) % c) / c) % 1
                        ) * 100) + 5
                    )  # Run between 5 - 105 times
                ][-1][0]
            ]
        for name
        in [['abcdefghijklmnopqrstuvwxyz'[int(prng(seed)*25)]]]
        for _
        in [0]*int( ( [1,2,3,4,5,5,6,7,8,9][int(prng(seed)*10)] * 0.7 ) + 3)
    ][-1][1].title()

if __name__ == '__main__':
    print( 'Name Generator V10:' )
    print( name_generator10() )