import os
from pathlib import path
import re
import shutil

# створюємо переліки відомих розширень за назвами
image_extantion = ('png', 'jpg', 'svg', 'jpeg')
video_extantion = ('AVI', 'MP4', 'MOV', 'MKV')
docs_extantion = ('DOC', 'DOCX', 'TXT', 'pdf', 'XLSX',
                  'PPTX', 'xls', 'xlsx', 'docx')
music_extantion = ('MP3', 'OGG', 'WAV', 'AMR')
zip_extantion = ('zip', 'GZ', 'TAR')
draw_extantion = ('dwg', 'dxf')
BASE_FILE_EXTANTION = (image_extantion + video_extantion + docs_extantion +
                       music_extantion + draw_extantion + zip_extantion + draw_extantion)

""" ф-ція приймає ім'я файла і перевіряє його, чи відоме розширення """


def know_extention_file(file):
    find_know_extention = []
    find_anknown_extantion = []
    # шукаємо індекс крапки справ аби відділити розширення
    index_symbol = file.rfind('.')
    e_f = (file[index_symbol+1:])  # вивід розширення
    if e_f in BASE_FILE_EXTANTION:
        k_x = True
        find_know_extention.append(e_f)
    else:
        k_x = False
        find_anknown_extantion.append(e_f)
    return k_x  # True|False


""" ф-ція Normolize яка перекладає назву з кирилиці на латиницю і змінює всі символі на "_" """


def normalize(file):
    # ввідні дані для транслітерації
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}  # створюємо словник перекладу.
    index_symbol = file.rfind('.')  # шукаємо символ "крапка" справа
    e_f = (file[index_symbol:])  # зрізаємо аби виділити розширення файла
    name_file = (file[:index_symbol])  # зрізаємо аби виділити назву файла
    # замінюємо всі символи на інший символ
    name_file = re.sub(r"\W", "_", name_file, flags=re.IGNORECASE)
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    # переклад назви відповідно до словнику
    name_file = name_file.translate(TRANS)
    # створення нового шляху з новою назвою файлу.
    new_name_file = os.path.join(BASE_DIR, name_file + e_f)
    old_name = os.path.join(BASE_DIR, file)
    # переназва файлу
    file = os.rename(old_name, new_name_file)
    return file


""" Ф-ція ___ яка створює диерктоурію, якщо її немає і переміщує туди файли з вказаним розиренням"""


def work_f(name):
    name_path = os.path.join(BASE_DIR, name)
    if not os.path.exists(name_path):  # створюємо папку, якщо її немає
        os.mkdir(name_path)
    new_file = name_path + '/' + file  # створюємо шлях для нового файлу
    os.replace(file_path, new_file)  # переміщуємо файл


"""++++"""
BASE_DIR = 'C:/Users/v4erednyk/Desktop/Somfiles'

"""ф-ція сортування"""


def sort(file):
    if file_path.endswith(image_extantion):

        work_f("images")

    elif file_path.endswith(video_extantion):

        work_f("video")

    elif file_path.endswith(docs_extantion):

        work_f("docs")

    elif file_path.endswith(music_extantion):

        work_f("music")
    # elif file_path.endswith(zip_extantion):
    #    zip_list.append(file)??????????????
    elif file_path.endswith(draw_extantion):
        # створюємо новий шлях файлу
        work_f("draws")
    else:
        work_f("aknowns")

    """ викликаємо ф-цію і перевіряємо, 
    чи відоме розширення нам чи ні. 
    Якщо так - то прапорець k_x = True. Також надає 
    2 переліки. Знайдених відомих та невідомих розширень
    """
    know_extention_file(file)
    """ викликаємо ф-цію для транслітерації кирилічних символів
    в латиницю. А також всі символи, крім латиници та цифр на "_"
    """
    normalize(file)


"""ф-ція проходу проходу по каталогу"""


def in_folder(dir_path):
    # створюємо перелік вмісту файлів та директорій всередині
    all_files = os.listdir(dir_path)
    if all_files:  # перевіряємо чи не порожня вона
        for file in all_files:  # перебираюємо всі файли і забираємо їх шляхи
            # створюємо шлях до файлу\директорії
            file_path = os.path.join(dir_path, file)
            if os.path.isdir(file_path):  # якщо директорія то
                normalize(file)  # нормалізуємо назву директорії
                # стоврюємо шлях до директорії
                dir_p = os.path.join(dir_path, file)
                in_folder(dir_p)  # викликаємо ф-цію аби зайтий в директорію
            elif not os.path.isdir(file_path):
                sort(file)  # сортування файлів
    else:  # директорія порожня і її необхідно видалити
        os.path.mrdir()  # видаляэмо директорію
