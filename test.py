# coding: utf8

import sys
import unittest

from nose.plugins.skip import SkipTest

from trans import trans

PY2 = sys.version_info[0] == 2


def py2(func):
    '''Mark test as work only with python 2'''
    def wrapper(self):
        if not PY2:
            raise SkipTest
        else:
            return func(self)

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


class TransTests(unittest.TestCase):
    s = u'''
    -- Раскудрить твою через коромысло в бога душу мать
             триста тысяч раз едрену вошь тебе в крыло
             и кактус в глотку! -- взревел разъяренный Никодим.
    -- Аминь, -- робко добавил из склепа папа Пий.
                 (c) Г. Л. Олди, "Сказки дедушки вампира".'''

    s_encoded = u'''
    -- Raskudrit tvoyu cherez koromyslo v boga dushu mat
             trista tysyach raz edrenu vosh tebe v krylo
             i kaktus v glotku! -- vzrevel razyarennyy Nikodim.
    -- Amin, -- robko dobavil iz sklepa papa Piy.
                 (c) G. L. Oldi, "Skazki dedushki vampira".'''

    def tearDown(self):
        for table in ['my_simple', 'my_complex']:
            if table in trans.tables:
                del trans.tables[table]

    def test_ansii(self):
        self.assertEquals(trans(u'qwerty'), u'qwerty')
        self.assertTrue(isinstance(trans(u'qwerty'), unicode if PY2 else str))

    def test_ansii_slug(self):
        self.assertEquals(trans(u'1 2 3 4 5 \n6 7 8 9', 'slug'), u'1_2_3_4_5__6_7_8_9')
        self.assertTrue(isinstance(trans(u'qwerty', 'slug'), unicode if PY2 else str))

    def test_russian(self):
        self.assertEquals(trans(u'йцукен'), u'ycuken')
        self.assertEquals(trans(self.s), self.s_encoded)
        self.assertTrue(isinstance(trans(self.s), unicode if PY2 else str))

    def test_russian_slug(self):
        self.assertEquals(trans(self.s, 'slug')[-42:-1],
                u'_c__G__L__Oldi___Skazki_dedushki_vampira_')

    def test_russian_diphthongs(self):
        self.assertEquals(trans(u'Юй Икари...'), u'Yuy Ikari...')

    def test_my_table_simple(self):
        my_simple = {u'1': u'2', u'2': u'3'}
        self.assertEquals(trans(u'1 2', my_simple), u'2_3')

    def test_my_table_complex(self):
        my_complex = ({u'4 5': u'45'}, {u'1': u'11', u'2': u'22',
                                     u'4': u'4', u'5': u'5',
                                     None: u'-'})

        self.assertEquals(trans(u'1 2 3 4 5 6 7 8 9', my_complex), u'11-22---45--------')

    def test_my_table_simple_register(self):
        trans.tables['my_simple'] = {u'1': u'2', u'2': u'3'}
        self.assertEquals(trans(u'1 2', 'my_simple'), u'2_3')

    def test_my_table_complex_register(self):
        trans.tables['my_complex'] = ({u'4 5': u'45'}, {u'1': u'11', u'2': u'22',
                                                 u'4': u'4', u'5': u'5',
                                                 None: u'-'})

        self.assertEquals(trans(u'1 2 3 4 5 6 7 8 9', 'my_complex'), u'11-22---45--------')

    def test_encode_bytes_exc(self):
        if PY2:
            self.assertRaises(TypeError, trans, str('qwerty'))
        else:
            self.assertRaises(TypeError, trans, bytes('qwerty', 'utf8'))


class CodecTests(unittest.TestCase):
    s = u'''
    -- Раскудрить твою через коромысло в бога душу мать
             триста тысяч раз едрену вошь тебе в крыло
             и кактус в глотку! -- взревел разъяренный Никодим.
    -- Аминь, -- робко добавил из склепа папа Пий.
                 (c) Г. Л. Олди, "Сказки дедушки вампира".'''

    s_encoded = u'''
    -- Raskudrit tvoyu cherez koromyslo v boga dushu mat
             trista tysyach raz edrenu vosh tebe v krylo
             i kaktus v glotku! -- vzrevel razyarennyy Nikodim.
    -- Amin, -- robko dobavil iz sklepa papa Piy.
                 (c) G. L. Oldi, "Skazki dedushki vampira".'''

    def tearDown(self):
        for table in ['my_simple', 'my_complex']:
            if table in trans.tables:
                del trans.tables[table]

    @py2
    def test_ansii(self):
        self.assertEquals(u'qwerty'.encode('trans'), u'qwerty')
        self.assertEquals(u'1 2 3 4 5 \n6 7 8 9'.encode('trans'), u'1 2 3 4 5 \n6 7 8 9')
        self.assertTrue(isinstance(u'qwerty'.encode('trans'), unicode))

    @py2
    def test_ansii_slug(self):
        self.assertEquals(u'1 2 3 4 5 \n6 7 8 9'.encode('trans/slug'), u'1_2_3_4_5__6_7_8_9')
        self.assertTrue(isinstance(u'qwerty'.encode('trans/slug'), unicode))

    @py2
    def test_russian(self):
        self.assertEquals(u'йцукен'.encode('trans'), u'ycuken')
        self.assertEquals(self.s.encode('trans'), self.s_encoded)
        self.assertTrue(isinstance(self.s.encode('trans'), unicode))

    @py2
    def test_russian_slug(self):
        self.assertEquals(self.s.encode('trans/slug')[-42:-1],
                u'_c__G__L__Oldi___Skazki_dedushki_vampira_')

    @py2
    def test_russian_diphthongs(self):
        self.assertEquals(u'Юй Икари...'.encode('trans'), u'Yuy Ikari...')

    @py2
    def test_my_table_simple(self):
        trans.tables['my_simple'] = {u'1': u'2', u'2': u'3'}
        self.assertEquals(u'1 2'.encode('trans/my_simple'), u'2_3')

    @py2
    def test_my_table_complex(self):
        trans.tables['my_complex'] = ({u'4 5': u'45'}, {u'1': u'11', u'2': u'22',
                                                 u'4': u'4', u'5': u'5',
                                                 None: u'-'})
        self.assertEquals(u'1 2 3 4 5 6 7 8 9'.encode('trans/my_complex'),
                            u'11-22---45--------')

    @py2
    def test_encode_str_exc(self):
        self.assertRaises(TypeError, 'qwerty'.encode, 'trans')
