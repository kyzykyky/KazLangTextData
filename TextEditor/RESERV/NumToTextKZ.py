units = (
    u'нөл',
    u'бір', u'екі', u'үш',
    u'төрт', u'бес', u'алты',
    u'жеті', u'сегіз', u'тоғыз'
)

endings = (
    u'дік',
    u'інші', u'нші', u'інші',
    u'інші', u'інші', u'ншы',
    u'нші', u'інші', u'ыншы',
)
endings2 = (
    u'ыншы', u'сыншы', u'ыншы',
    u'ыншы', u'інші', u'ыншы',
    u'інші', u'інші', u'ыншы',

    u'інші', u'ыншы'
)

tens = (
    u'он', u'жиырма', u'отыз',
    u'қырық', u'елу', u'алпыс',
    u'жетпіс', u'сексен', u'тоқсан'
)

hundreds = (
    u'бір жуз', u'екі жуз', u'үш жуз',
    u'төрт жуз', u'бес жуз', u'алты жуз',
    u'жеті жуз', u'сегіз жуз', u'тоғыз жуз'
)

orders = (
    u'мың',
    u'миллион',
    u'миллиард',
)

months = (
    u'қаңтар',
    u'ақпан',
    u'наурыз',
    u'сәуір',
    u'мамыр',
    u'маусым',
    u'шілде',
    u'тамыз',
    u'қыркүйек',
    u'қазан',
    u'қараша',
    u'желтоқсан'
)

minus = u'минус'


def thousand(rest):
    prev = 0
    name = []
    data = ((units, 10), (tens, 100), (hundreds, 1000))

    for names, x in data:
        cur = int(((rest - prev) % x) * 10 / x)
        prev = rest % x

        if cur == 0:
            continue
        elif x == 10:
            name_ = names[cur]
            if isinstance(name_, tuple):
                name_ = name_[0]
            name.append(name_)
        else:
            name.append(names[cur-1])
    return name


def num2text(num, main_units=u'', ord_num=True):
    _orders = (main_units,) + orders
    if num == 0:
        return ' '.join((units[0], _orders[0])).strip()  # ноль

    rest = abs(num)
    orda = 0
    name = []
    while rest > 0:
        nme = thousand(rest % 1000)
        if nme or orda == 0:
            name.append(_orders[orda])
        name += nme
        rest = int(rest / 1000)
        orda += 1
    if num < 0:
        name.append(minus)
    name.reverse()
    return ' '.join(name).strip()


def text2num(text):
    num = ''
    for soz in text.split(' '):
        if soz in orders:
            pass
        elif soz in units:
            num += str(units.index(soz))
        elif soz in tens:
            num += str(tens.index(soz)+1)
        elif soz == 'минус':
            num += '-'
    return num


def date2text(date):
    day, month, year = date.split('.')
    text = ''
    if day[0] == '0':
        day_ = num2text(int(day[1])) + str(endings[int(day[1])])
    else:
        if day[1] == '0':
            day_ = num2text(int(day)) + str(endings2[int(day[0])-1])
        else:
            day_ = num2text(int(day)) + str(endings[int(day[1])])

    if month[0] == '0':
        month_ = month[1]
    else:
        month_ = month

        text += num2text(int(year), 'жылғы') + ' '
        text += day_ + ' '
        text += months[int(month_)-1]
    return text


# from NumToTextKZ import num2text

# number = int(input('Введите число: '))
# print(num2text(number), text2num(num2text(number)))
print(date2text('30.11.2020'))

