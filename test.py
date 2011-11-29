# coding: utf-8

import unittest
from nose.tools import *

import trans

class test(unittest.TestCase):

    def test_ansii(self):
        assert u'qwerty'.encode('trans') == u'qwerty'
        assert u'1 2 3 4 5 \n6 7 8 9'.encode('trans') == u'1 2 3 4 5 \n6 7 8 9'
        assert type(u'qwerty'.encode('trans')) is unicode
    
    
    def test_ansii_slug(self):
        assert u'1 2 3 4 5 \n6 7 8 9'.encode('trans/slug') == u'1_2_3_4_5__6_7_8_9'
        assert type(u'qwerty'.encode('trans/id')) is unicode
    
    
    def test_russian(self):
        assert u'йцукен'.encode('trans') == u'ycuken'
    
        s = u'''
        -- Раскудрить твою через коромысло в бога душу мать
                 триста тысяч раз едрену вошь тебе в крыло
                 и кактус в глотку! -- взревел разъяренный Никодим.
        -- Аминь, -- робко добавил из склепа папа Пий.
                     (c) Г. Л. Олди, "Сказки дедушки вампира".'''
    
        assert s.encode('trans') == u'''
        -- Raskudrit tvoyu cherez koromyslo v boga dushu mat
                 trista tysyach raz edrenu vosh tebe v krylo
                 i kaktus v glotku! -- vzrevel razyarennyy Nikodim.
        -- Amin, -- robko dobavil iz sklepa papa Piy.
                     (c) G. L. Oldi, "Skazki dedushki vampira".'''
    
        assert type(s.encode('trans')) is unicode
    
    
    def test_russian_slug(self):
        s = u'''
        -- Раскудрить твою через коромысло в бога душу мать
                 триста тысяч раз едрену вошь тебе в крыло
                 и кактус в глотку! -- взревел разъяренный Никодим.
        -- Аминь, -- робко добавил из склепа папа Пий.
                     (c) Г. Л. Олди, "Сказки дедушки вампира".'''
    
        assert s.encode('trans/slug')[-42:-1] == \
                u'_c__G__L__Oldi___Skazki_dedushki_vampira_'
    
    
    def test_russian_diphthongs(self):
        assert u'Юй Икари...'.encode('trans') == u'Yuy Ikari...'


    def test_my_table(self):
        trans.tables['my'] = {u'1': u'2', u'2': u'3'}
        assert u'1 2'.encode('trans/my') == u'2_3'

        trans.tables['my2'] = ({u'4 5': u'45'}, {u'1': u'11', u'2': u'22',
                                                 u'4': u'4', u'5': u'5',
                                                 None: u'-'})
        assert u'1 2 3 4 5 6 7 8 9'.encode('trans/my2') == u'11-22---45--------'


    def test_redefining_table(self):
        trans.tables['my'] = {u'1': u'2', u'2': u'2', None: u''}
        assert u'1 2'.encode('trans/my') == u'22'

        trans.tables['my'] = ({u'11': u'22'},
                              {u'2': u'2', u'3': u'22', None: u'-'})
        assert u'11 3'.encode('trans/my') == u'22-22'


    def test_encode_str_exc(self):
        self.assertRaises(TypeError, 'qwerty'.encode, 'trans')

