import os
import sys
import re
import shutil
# import WinError


"""
# надаємо стандартний шлях зчитування до змінної, для зручості звертання
BASE_DIR = 'C:/Users/v4erednyk/Desktop/Somfiles/'
all_files = os.listdir(BASE_DIR)  # зчитуємо весь перелік файлів
image_extantion = ('png', 'jpg', 'svg', 'jpeg')
video_extantion = ('AVI', 'MP4', 'MOV', 'MKV')
docs_extantion = ('DOC', 'DOCX', 'TXT', '.pdf', 'XLSX',
                  'PPTX', '.xls', 'xlsx', 'docx')
music_extantion = ('MP3', 'OGG', 'WAV', 'AMR')
zip_extantion = ('zip', 'GZ', 'TAR')
draw_extantion = ('dwg', 'dxf')
known_extantion = set()
anknown_extantion = set()

image_list = []
video_list = []
docs_list = []
music_list = []
zip_list = []
draw_list = []
other_list = []
for file in all_files:  # перебираюємо всі файл і забираємо їх шляхи
    file_path = os.path.join(BASE_DIR, file)
    # починаємо перебирати файли та сортувати їх за

    if file_path.endswith(image_extantion):
        image_list.append(file)
        new_known_extantion = re.search(r"\.(\w+)", file)
        known_extantion.append(new_known_extantion.group())
    elif file_path.endswith(video_extantion):
        video_list.append(file)
    elif file_path.endswith(docs_extantion):
        docs_list.append(file)
    elif file_path.endswith(music_extantion):
        music_list.append(file)
    elif file_path.endswith(zip_extantion):
        zip_list.append(file)
    elif file_path.endswith(draw_extantion):
        draw_list.append(file)
    else:
        other_list.append(file)
        new_anknown_extantion = re.search(r"\.(\w+)", file)
        anknown_extantion.add(new_anknown_extantion.group())

# print(image_list)
# print(video_list)
# print(docs_list)
# print(music_list)
# print(draw_list)
# print(zip_list)
# print(other_list)
# known_extantion =
print(known_extantion)
print(anknown_extantion)
"""


def normalize(file):
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

    return os.rename(old_name, new_name_file)


def workfuncktion(name):
    name_path = os.path.join(BASE_DIR, name)
    if not os.path.exists(name_path):  # створюємо папку, якщо її немає
        os.mkdir(name_path)
    new_file = name_path + '/' + file  # створюємо шлях для нового файлу
    os.replace(file_path, new_file)  # переміщуємо файл


BASE_DIR = 'C:/Users/v4erednyk/Desktop/Somfiles/Test/'


# блок коду задання ввідних даних
# ввідні дані відомих розширень
file_extantion = []
image_extantion = ('png', 'jpg', 'svg', 'jpeg')
video_extantion = ('AVI', 'MP4', 'MOV', 'MKV')
docs_extantion = ('DOC', 'DOCX', 'TXT', 'pdf', 'XLSX',
                  'PPTX', 'xls', 'xlsx', 'docx')
music_extantion = ('MP3', 'OGG', 'WAV', 'AMR')
zip_extantion = ('zip', 'GZ', 'TAR')
draw_extantion = ('dwg', 'dxf')
BASE_FILE_EXTANTION = (image_extantion + video_extantion + docs_extantion +
                       music_extantion + draw_extantion + zip_extantion + draw_extantion)
find_know_extention = []
find_anknown_extantion = []
# ввідні дані для транслітерації
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}  # створюємо словник перекладу.

all_files = os.listdir(BASE_DIR)
for file in all_files:  # перебираюємо всі файл і забираємо їх шляхи
    file_path = os.path.join(BASE_DIR, file)

    print(file)

    workfuncktion("images")
    # if os.path.isdir(file_path):  # якщо передане тека, то шлях змінюється
    #    print(file_path)
