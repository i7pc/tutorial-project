# 5.1 Написати функцію яка підраховує довжину строки без перенесення символів

"""
text = 'AlexKdfe23\t\f\v.\r'

def real_len(text):
    text = text.replace("\n", "")
    text = text.replace("\r", "")
    text = text.replace("\f", "")
    text = text.replace("\t", "")
    text = text.replace("\v", "")
    text = text.replace("\r", "")
    return print(len(text))

real_len(text)
"""

# 5.2 Є список словників. Розібратись правильність виконання.
"""
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key: str, letter_case bool=False):
    m_l = []
    if not letter_case:
        for items in articles_dict:
            if (key in items['title']) or (key in items['author']):
                m_l.append(items)

    else:
        key = key.lower()
        for i in articles_dict:
            if (key in str(i['title']).lower()) or (key in str(i['author']).lower()):
                my_list.append(i)
    return m_l
"""

"""
# 5.3 Нормалізація телефонного номеру.

def sanitize_phone_number(phone):
    phone = phone.strip()
    phone = phone.replace("-", "")
    phone = phone.replace(" ", "")
    phone = phone.replace("(", "")
    phone = phone.replace(")", "")
    phone = phone.replace("+", "")
    return print(phone)


sanitize_phone_number("   +38(067) 407-88 68    ")
"""
# 5.4 Перевірка префікc
"""v

def full_name(first_name, last_name):  # полное имя
    f_name = f'{first_name} {last_name}'
    result = f_name.startswith(first_name)
    return result


def is_check_name(fullname, first_name):
    result = fullname.startswith(first_name)
    return result

print(is_check_name('Vadim Cherednyk', 'Vadim'))

^"""
# 5.5

"""v
def sanitize_phone_number(phone):
    phone = (
        phone.strip()
        .replace("-", "")
        .replace(" ", "")
        .replace("(", "")
        .replace(")", "")
        .replace("+", ""))
    return phone


sanitize_phone_number("   +38(067) 407-88 68    ")

def get_phone_numbers_for_countries(list_phones):

    # створююємо словничок, з ключами і пустими значеннями.
    v_p = {'UA': [], 'JP': [], 'TW': [], 'SG': []}

    for num in list_phones:                         # перебираємо циклом надані номери телефонів
        # викликаємо ф-цію фільтрації і призначаємо очищений номер до змінної
        sort_num = sanitize_phone_number(num)
        if sort_num.startswith('81'):  # перебір умов
            v_p['JP'].append(sort_num)
        elif sort_num.startswith('65'):
            v_p['SG'].append(sort_num)
        elif sort_num.startswith('886'):
            v_p['TW'].append(sort_num)
        elif sort_num.startswith('380'):
            v_p['UA'].append(sort_num)
    return v_p
^"""
# 5.6
"""v
def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    text_f = (
        text.strip()
        .replace(".", "")
        .replace(",", ""))
    list_word = text_f.split(" ")

    x = 0

    for word in list_word:
        if not space_around:
            for spam in spam_words:
                if word.endswith(spam) or word.startswith(spam):
                    x += 1
                else:
                    continue
        else:  # випадок, коли слово окремо, перевіряємо слово.
            x = spam_words.count(word)

    # Перевірка чи знайдене хоч одне слово
    if x > 0:
        return True
    else:
        return False
^"""

"""v
text = "Перше слово і друге слово, потім третє слово. Четверте Молох та лохотрон"
word = "лох"
word1 = "Молох"
spam_word = ["лох", "козел", "виродок"]

x = spam_word.count.endswith(word)

print(x)
^"""

# 5.7

"""v
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

name = "Дмитро Короб"

TRANS = {}

def translate(name):
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    return name.translate(TRANS)
^"""

# 5.8 Створити ф-цію виведення строк із списку з двох словників
"""v

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    num = 0
    students_list = []
    for k, v in students.items():
        num += 1
        grade_student = v
        if grade_student in grades.keys():
            number_grade = grades.get(grade_student)
        x = "{:>4}|{name_student:<10}|{grade:^5}|{n_g:^5}".format(
            num, name_student=k, grade=v, n_g=number_grade)
        students_list.append(x)
    return students_list

^"""
# 5.9 Створити ф-цію виведення таблиці перетворення

"""v
def formatted_numbers(x):
    list_of_number = []
    first_str = f"|{'decimal':^10}|{'hex':^10}|{'binary':^10}|"
    list_of_number.append(first_str)
    for i in range(x):
        el_list = '|{:<10d}|{:^10x}|{:>10b}|'.format(i, i, i)
        list_of_number.append(el_list)
    return list_of_number

for el in formatted_numbers(10):
    print(el)
^"""
# 5.10 Необхідно створити пошукову ф-цію в тексті. Але умова - має повертати словник, а не зменну=словник
"""v
def find_word(text, word):
    answer_dict = {}
    find_word = re.search(word, text)
    if find_word:
        answer_dict['result'] = True
        t_list = find_word.span()
        answer_dict['first_index'] = t_list[0]
        answer_dict['last_index'] = t_list[1]
        answer_dict['search_string'] = find_word.group()
        answer_dict['string'] = text
        return answer_dict
    else:
        return text

def find_word(text, word):
    #answer_dict = {}
    find_word = re.search(word, text)
    return {
        'result': bool(find_word),
        'first_index': find_word.start() if find_word else None, #тут треба вказувати що додавати, якщо не знайдено. Бо ф-ція не працює з типом None
        'last_index': find_word.end() if find_word else None, #тут треба вказувати що додавати, якщо не знайдено. Бо ф-ція не працює з типом None
        'search_string': word,
        'string': text
    }
^"""
# 5.11 Необхідно створити теж саме шо і 5.10 але з ігнорування до регістру пошукового слова і декілька співпадінь.
"""v
def find_word(text, word):
    return re.findall(fr'{word}+', text, re.IGNORECASE) #розібратись із завданням. Розумію, але шо як пишеться перший аргумент
^"""

# 5.12 Замінює "небажані слова" на *

"""v
def replace_spam_words(text, spam_words):
    for word in spam_words:
        text = re.sub(word, len(word)*"*", text, flags=re.IGNORECASE)
    return text
^"""
# 5.13

"""v
def find_all_emails(text):
    result = re.findall(r"[A-Za-z]{1}[\w\.]+@[a-z]+\.[a-z]{2,}", text)
    return result
^"""

# 5.14
"""v
def find_all_phones(text):
    result = re.findall(r"[+]\d{3}.\d{2}.\d{3}-(?:\d{1}\-\d{3}|\d{2}\-\d{2})", text)
    return result
^"""

# 5.15

"""v
def find_all_links(text):
    result = []
    iterator = re.finditer(
        r"[http://|https://]{3,}(?:[www]|)+.[a-zA-Z]+.[a-zA-Z]{2,}", text)
    for match in iterator:
        result.append(match.group())
    return result
^"""
