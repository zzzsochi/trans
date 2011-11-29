# coding: utf-8

ur"""

This module translates national characters into similar sounding
latin characters (transliteration).
At the moment, Czech, Greek, Latvian, Polish, Turkish, Russian, Ukrainian
alphabets are supported (it covers 99% of needs).

  >>> # coding: utf-8
  >>> import trans
  >>> u'Hello World!'.encode('trans')
  u'Hello World!'
  >>> u'Привет, Мир!'.encode('trans')
  u'Privet, Mir!'

Читайте документацию для того, чтобы узнать больше.
Please read the documentation for 

"""

__version__ = '1.3'
__author__ = 'Zelenyak Aleksandr aka ZZZ <zzz.sochi@gmail.com>'

latin = {
    u'à': u'a',  u'á': u'a',  u'â': u'a', u'ã': u'a', u'ä': u'a', u'å': u'a',
    u'æ': u'ae', u'ç': u'c',  u'è': u'e', u'é': u'e', u'ê': u'e', u'ë': u'e',
    u'ì': u'i',  u'í': u'i',  u'î': u'i', u'ï': u'i', u'ð': u'd', u'ñ': u'n',
    u'ò': u'o',  u'ó': u'o',  u'ô': u'o', u'õ': u'o', u'ö': u'o', u'ő': u'o',
    u'ø': u'o',  u'ù': u'u',  u'ú': u'u', u'û': u'u', u'ü': u'u', u'ű': u'u',
    u'ý': u'y',  u'þ': u'th', u'ÿ': u'y',

    u'À': u'A',  u'Á': u'A',  u'Â': u'A', u'Ã': u'A', u'Ä': u'A', u'Å': u'A',
    u'Æ': u'AE', u'Ç': u'C',  u'È': u'E', u'É': u'E', u'Ê': u'E', u'Ë': u'E',
    u'Ì': u'I',  u'Í': u'I',  u'Î': u'I', u'Ï': u'I', u'Ð': u'D', u'Ñ': u'N',
    u'Ò': u'O',  u'Ó': u'O',  u'Ô': u'O', u'Õ': u'O', u'Ö': u'O', u'Ő': u'O',
    u'Ø': u'O',  u'Ù': u'U',  u'Ú': u'U', u'Û': u'U', u'Ü': u'U', u'Ű': u'U',
    u'Ý': u'Y',  u'Þ': u'TH', u'ß': u'ss'
}

greek = {
    u'α': u'a', u'β': u'b', u'γ': u'g', u'δ': u'd', u'ε': u'e',  u'ζ': u'z',
    u'η': u'h', u'θ': u'8', u'ι': u'i', u'κ': u'k', u'λ': u'l',  u'μ': u'm',
    u'ν': u'n', u'ξ': u'3', u'ο': u'o', u'π': u'p', u'ρ': u'r',  u'σ': u's',
    u'τ': u't', u'υ': u'y', u'φ': u'f', u'χ': u'x', u'ψ': u'ps', u'ω': u'w',
    u'ά': u'a', u'έ': u'e', u'ί': u'i', u'ό': u'o', u'ύ': u'y',  u'ή': u'h',
    u'ώ': u'w', u'ς': u's', u'ϊ': u'i', u'ΰ': u'y', u'ϋ': u'y',  u'ΐ': u'i',

    u'Α': u'A', u'Β': u'B', u'Γ': u'G', u'Δ': u'D', u'Ε': u'E',  u'Ζ': u'Z',
    u'Η': u'H', u'Θ': u'8', u'Ι': u'I', u'Κ': u'K', u'Λ': u'L',  u'Μ': u'M',
    u'Ν': u'N', u'Ξ': u'3', u'Ο': u'O', u'Π': u'P', u'Ρ': u'R',  u'Σ': u'S',
    u'Τ': u'T', u'Υ': u'Y', u'Φ': u'F', u'Χ': u'X', u'Ψ': u'PS', u'Ω': u'W',
    u'Ά': u'A', u'Έ': u'E', u'Ί': u'I', u'Ό': u'O', u'Ύ': u'Y',  u'Ή': u'H',
    u'Ώ': u'W', u'Ϊ': u'I', u'Ϋ': u'Y'
}

turkish = {
    u'ş': u's', u'Ş': u'S', u'ı': u'i', u'İ': u'I', u'ç': u'c', u'Ç': u'C',
    u'ü': u'u', u'Ü': u'U', u'ö': u'o', u'Ö': u'O', u'ğ': u'g', u'Ğ': u'G'
}

russian = (
    {u'юй': u'yuy', u'ей': u'yay',
     u'Юй': u'Yuy', u'Ей': u'Yay'},
    {
    u'а': u'a',  u'б': u'b',  u'в': u'v',  u'г': u'g', u'д': u'd', u'е': u'e',
    u'ё': u'yo', u'ж': u'zh', u'з': u'z',  u'и': u'i', u'й': u'y', u'к': u'k',
    u'л': u'l',  u'м': u'm',  u'н': u'n',  u'о': u'o', u'п': u'p', u'р': u'r',
    u'с': u's',  u'т': u't',  u'у': u'u',  u'ф': u'f', u'х': u'h', u'ц': u'c',
    u'ч': u'ch', u'ш': u'sh', u'щ': u'sh', u'ъ': u'',  u'ы': u'y', u'ь': u'',
    u'э': u'e',  u'ю': u'yu', u'я': u'ya',

    u'А': u'A',  u'Б': u'B',  u'В': u'V',  u'Г': u'G', u'Д': u'D', u'Е': u'E',
    u'Ё': u'Yo', u'Ж': u'Zh', u'З': u'Z',  u'И': u'I', u'Й': u'Y', u'К': u'K',
    u'Л': u'L',  u'М': u'M',  u'Н': u'N',  u'О': u'O', u'П': u'P', u'Р': u'R',
    u'С': u'S',  u'Т': u'T',  u'У': u'U',  u'Ф': u'F', u'Х': u'H', u'Ц': u'C',
    u'Ч': u'Ch', u'Ш': u'Sh', u'Щ': u'Sh', u'Ъ': u'',  u'Ы': u'Y', u'Ь': u'',
    u'Э': u'E',  u'Ю': u'Yu', u'Я': u'Ya'
})

ukrainian = (russian[0].copy(), {
    u'Є': u'Ye', u'І': u'I', u'Ї': u'Yi', u'Ґ': u'G',
    u'є': u'ye', u'і': u'i', u'ї': u'yi', u'ґ': u'g'
})
ukrainian[1].update(russian[1])

czech = {
    u'č': u'c', u'ď': u'd', u'ě': u'e', u'ň': u'n', u'ř': u'r', u'š': u's',
    u'ť': u't', u'ů': u'u', u'ž': u'z',
    u'Č': u'C', u'Ď': u'D', u'Ě': u'E', u'Ň': u'N', u'Ř': u'R', u'Š': u'S',
    u'Ť': u'T', u'Ů': u'U', u'Ž': u'Z'
}

polish = {
    u'ą': u'a', u'ć': u'c', u'ę': u'e', u'ł': u'l', u'ń': u'n', u'ó': u'o',
    u'ś': u's', u'ź': u'z', u'ż': u'z',
    u'Ą': u'A', u'Ć': u'C', u'Ę': u'e', u'Ł': u'L', u'Ń': u'N', u'Ó': u'o',
    u'Ś': u'S', u'Ź': u'Z', u'Ż': u'Z'
}

latvian = {
    u'ā': u'a', u'č': u'c', u'ē': u'e', u'ģ': u'g', u'ī': u'i', u'ķ': u'k',
    u'ļ': u'l', u'ņ': u'n', u'š': u's', u'ū': u'u', u'ž': u'z',
    u'Ā': u'A', u'Č': u'C', u'Ē': u'E', u'Ģ': u'G', u'Ī': u'i', u'Ķ': u'k',
    u'Ļ': u'L', u'Ņ': u'N', u'Š': u'S', u'Ū': u'u', u'Ž': u'Z'
}



ascii_str = u'''_0123456789
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
!"#$%&'()*+,_-./:;<=>?@[\\]^`{|}~ \t\n\r\x0b\x0c'''

ascii = ({}, dict(zip(ascii_str, ascii_str)))
for t in [latin, greek, turkish, russian, ukrainian, czech, polish, latvian]:
    if isinstance(t, dict):
        t = ({}, t)
    ascii[0].update(t[0])
    ascii[1].update(t[1])
ascii[1][None] = u'_'
del t


slug = (ascii[0].copy(), ascii[1].copy())
for c in '''!"#$%&'()*+,_-./:;<=>?@[\\]^`{|}~ \t\n\r\x0b\x0c''':
    del slug[1][c]


def trans(input, table=ascii):
    '''Translate unicode string, using 'table'.
       Table may be tuple (diphthongs, other) or dict (other).'''
    if not isinstance(input, unicode):
        raise TypeError, 'trans codec support only unicode string, %r given.' \
                                                        % type(input)
    if isinstance(table, dict):
        table = ({}, table)

    first = input
    for diphthong, value in table[0].items():
        first = first.replace(diphthong, value)

    default = table[1].get(None, u'_')
    
    second = u''
    for char in first:
        second += table[1].get(char, default)

    return second, len(second)

tables = {'ascii': ascii, 'text': ascii, 'slug': slug, 'id': slug}

import codecs

def encode(input, errors='strict', table_name='ascii'):
    try:
        table = tables[table_name]
    except KeyError:
        raise ValueError, 'Table "%s" not found in tables!' % table_name
    else:
        return trans(input, table)

def no_decode(input, errors='strict'):
    raise TypeError("trans codec does not support decode.")

def trans_codec(enc):
    if enc == 'trans':
        return codecs.CodecInfo(encode, no_decode)
#    else:
    try:
        enc_name, table_name = enc.split('/', 1)
    except ValueError:
        return None
    if enc_name != 'trans':
        return None
    if table_name not in tables:
        raise ValueError, 'Table "%s" not found in tables!' % table_name

    return codecs.CodecInfo(lambda i, e='strict': encode(i, e, table_name),
                            no_decode)

codecs.register(trans_codec)

