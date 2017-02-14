# coding=utf-8

import unicodedata

import nltk
import six
from nltk.corpus import mac_morpho

from bm25 import BM25


def normalize_terms(terms):
    """Remove diacritics from terms and turn case to lowercase"""
    # Aqui você pode adicionar outros tratamentos:
    # - remover stopwords
    # - remover numerais
    # - stemming
    return [remove_diacritics(term).lower() for term in terms]


def remove_diacritics(text, encoding='utf8'):
    """Remove diacritics from bytestring or unicode, returning an unicode string"""
    nfkd_form = unicodedata.normalize('NFKD', to_unicode(text, encoding))
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii.decode(encoding)


def to_unicode(text, encoding='utf8'):
    """Convert a string (bytestring in `encoding` or unicode), to unicode."""
    if isinstance(text, six.text_type):
        return text
    return text.decode(encoding)


# nltk.download('mac_morpho')
# `news` é uma list que contém listas de tokens
news = [normalize_terms(sentence) for sentence in mac_morpho.sents()]
print(repr(news[0]))

# Estou utilizando os 1000 primeiros pra exemplificar. Processar todos os 51397 demora um tempinho
bm25 = BM25(news[:1000])
query = normalize_terms(nltk.word_tokenize('inflacao'))
for position, index in enumerate(bm25.ranked(query, 5)):
    print('{} - {}'.format(position, ' '.join(news[index])))
