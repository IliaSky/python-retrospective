SIGNS_AND_THEIR_END_DATES = [
    ('Козирог', (1, 19)),
    ('Водолей', (2, 18)),
    ('Риби', (3, 20)),
    ('Овен', (4, 20)),
    ('Телец', (5, 20)),
    ('Близнаци', (6, 20)),
    ('Рак', (7, 21)),
    ('Лъв', (8, 22)),
    ('Дева', (9, 22)),
    ('Везни', (10, 22)),
    ('Скорпион', (11, 21)),
    ('Стрелец', (12, 21)),
    ('Козирог', (12, 31))
]

def what_is_my_sign(day, month):
    date_of_birth = (month, day)
    for sign, end_date in SIGNS_AND_THEIR_END_DATES:
        if date_of_birth <= end_date:
            return sign
