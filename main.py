import csv
import re


# TODO 1: выполните пункты 1-3 ДЗ
def convert_contacts():
    contacts = []
    for con in contacts_list:
        data = ' '.join(con[:3]).split(' ')
        contacts.append([data[0], data[1], data[2], con[3], con[4], con[5], con[6]])
    return contacts


def convert_phone_numbers():
    contacts = convert_contacts()
    pattern = r'(\+7|8)\s?\(?(\d{3})\)?\s?[-]?(\d{3})\s?[-]?(\d{2})\s?[-]?(\d{2})\s?\(?(доб\.?)?\s?(\d{2,5})?\)?'
    convert_phone = r'+7(\2)\3-\4-\5 \6\7'
    for number in contacts:
        res = re.sub(pattern, convert_phone, number[5])
        number[5] = res
    return contacts


def contacts_filter():
    new_contacts = convert_phone_numbers()
    for contact in new_contacts:
        last_name = contact[0]
        first_name = contact[1]
        for new_contact in new_contacts:
            new_last_name = new_contact[0]
            new_first_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == '':
                    contact[2] = new_contact[2]
                if contact[3] == '':
                    contact[3] = new_contact[3]
                if contact[4] == '':
                    contact[4] = new_contact[4]
                if contact[5] == '':
                    contact[5] = new_contact[5]
                if contact[6] == '':
                    contact[6] = new_contact[6]
    result_list = list()
    for i in new_contacts:
        if i not in result_list:
            result_list.append(i)
    return result_list


if __name__ == '__main__':
    # читаем адресную книгу в формате CSV в список contacts_list
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(contacts_filter())
