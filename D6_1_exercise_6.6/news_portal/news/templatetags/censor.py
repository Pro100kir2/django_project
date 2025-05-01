from django import template

register = template.Library()

# Список нежелательных слов
CENSORED_WORDS = ['идиот', 'дурак', 'редиска']

@register.filter(name='censor')
def censor(value):
    if isinstance(value, str):
        for word in CENSORED_WORDS:
            value = value.replace(word, '*' * len(word))
    return value
