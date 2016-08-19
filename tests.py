#!/usr/bin/env python
# coding: utf8

import sys

import pytest

import trans as trans_module

if sys.version_info < (3, 0):
    unistr = unicode  # noqa
    unibytes = str
    to_bytes = str

    def _encode(input, table=None):
        if not table:
            return input.encode('trans')
        else:
            return input.encode('trans/' + table)

    trans_funcs = [trans_module.trans, _encode]

else:
    unistr = str
    unibytes = bytes
    to_bytes = lambda string: bytes(string, 'utf8')  # noqa
    trans_funcs = [trans_module.trans]


@pytest.fixture(scope='module')
def ru_src():
    return u"""
    -- Раскудрить твою через коромысло в бога душу мать
             триста тысяч раз едрену вошь тебе в крыло
             и кактус в глотку! -- взревел разъяренный Никодим.
    -- Аминь, -- робко добавил из склепа папа Пий.
                 (c) Г. Л. Олди, "Сказки дедушки вампира"."""  # noqa


@pytest.fixture(scope='module')
def ru_encoded():
    return u"""
    -- Raskudrit tvoyu cherez koromyslo v boga dushu mat
             trista tysyach raz edrenu vosh tebe v krylo
             i kaktus v glotku! -- vzrevel razyarennyy Nikodim.
    -- Amin, -- robko dobavil iz sklepa papa Piy.
                 (c) G. L. Oldi, "Skazki dedushki vampira"."""  # noqa


@pytest.fixture(scope='module')
def farsi_src():
    return (u'همه‌ی افراد بشر آزاد به دنیا می‌آیند و ا'
            u'ز دید حیثیت و حقوق با هم برابرند')


@pytest.fixture(scope='module')
def farsi_encoded():
    return (u'hmhye afrad bshr azad bh dnyea myeayend '
            u'wa az dyed hyethyet wa hqwaq ba hm brabrnd')


@pytest.yield_fixture(scope='function')
def simple_table():
    yield {u'1': u'2', u'2': u'3'}
    trans_module.trans.tables.pop('my_simple', None)


@pytest.yield_fixture(scope='function')
def complex_table():
    yield ({u'4 5': u'45'},
           {u'1': u'11', u'2': u'22', u'4': u'4', u'5': u'5', None: u'-'})

    trans_module.trans.tables.pop('my_simple', None)


@pytest.mark.parametrize('trans', trans_funcs)
def test_ansii(trans):
    assert trans(u'qwerty') == u'qwerty'
    assert isinstance(trans(u'qwerty'), unistr)


@pytest.mark.parametrize('trans', trans_funcs)
def test_ansii_slug(trans):
    assert trans(u'1 2 3 4 5 \n6 7 8 9', 'slug') == u'1_2_3_4_5__6_7_8_9'
    assert isinstance(trans(u'qwerty', 'slug'), unistr)


@pytest.mark.parametrize('trans', trans_funcs)
def test_natural(trans, ru_src, ru_encoded, farsi_src, farsi_encoded):
    assert trans(u'йцукен') == u'ycuken'
    assert trans(ru_src) == ru_encoded
    assert isinstance(trans(ru_src), unistr)

    assert trans(farsi_src) == farsi_encoded
    assert isinstance(trans(farsi_src), unistr)


@pytest.mark.parametrize('trans', trans_funcs)
def test_russian_slug(trans, ru_src):
    assert trans(ru_src, 'slug')[-42:-1] == u'_c__G__L__Oldi___Skazki_dedushki_vampira_'


@pytest.mark.parametrize('trans', trans_funcs)
def test_russian_diphthongs(trans):
    assert trans(u'Юй Икари...') == u'Yuy Ikari...'


@pytest.mark.parametrize('trans', trans_funcs)
def test_my_table_simple_register(trans, simple_table):
    trans_module.trans.tables['my_simple'] = simple_table
    assert trans(u'1 2', 'my_simple') == u'2_3'


@pytest.mark.parametrize('trans', trans_funcs)
def test_my_table_complex_register(trans, complex_table):
    trans_module.trans.tables['my_complex'] = complex_table
    assert trans(u'1 2 3 4 5 6 7 8 9', 'my_complex') == u'11-22---45--------'


@pytest.mark.parametrize('trans', trans_funcs)
def test_encode_bytes_exc(trans):
    with pytest.raises(TypeError):
        trans(to_bytes('qwerty'))


def test_my_table_simple():
    my_simple = {u'1': u'2', u'2': u'3'}
    assert trans_module.trans(u'1 2', my_simple) == u'2_3'


def test_my_table_complex():
    my_complex = (
        {u'4 5': u'45'},
        {u'1': u'11', u'2': u'22', u'4': u'4', u'5': u'5', None: u'-'})

    assert trans_module.trans(u'1 2 3 4 5 6 7 8 9', my_complex) == u'11-22---45--------'
