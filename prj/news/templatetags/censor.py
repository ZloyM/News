from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются

@register.filter(name='censor')
def censor(message: str):
    variants = ['мат', 'цензура', 'спорт']  # непристойные выражения

    ln = len(variants)
    censor = ''
    string = ''
    pattern = '*'  # чем заменять непристойные выражения
    for i in message:
        string += i
        string2 = string.lower()
        flag = 0
    for j in variants:
        if not string2 in j:
            flag += 1
        if string2 == j:
            censor += pattern * len(string)
            flag -= 1
            string = ''
        if flag == ln:
            censor += string
            string = ''

    return censor