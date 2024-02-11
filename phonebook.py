import csv

SPRAVOCHNIK_FILE = "spravochnik.csv"

def load_spravochnik():
    """Загружает данные из файла справочника (если файл существует)."""
    try:
        with open(SPRAVOCHNIK_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            spravochnik = list(reader)
        return spravochnik
    except FileNotFoundError:
        return []

def save_spravochnik(spravochnik):
    """Сохраняет данные в файл справочника."""
    with open(SPRAVOCHNIK_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["Фамилия", "Имя", "Отчество", "Организация", "Телефон рабочий", "Телефон личный"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(spravochnik)

def display_entries(entries):
    """Отображает записи справочника."""
    for entry in entries:
        print(entry)

def add_entry(spravochnik, entry):
    """Добавляет новую запись в справочник и сохраняет его."""
    spravochnik.append(entry)
    save_spravochnik(spravochnik)
    print("Запись добавлена успешно.")

def edit_entry(spravochnik, index, new_entry):
    """Редактирует существующую запись в справочнике по индексу и сохраняет изменения."""
    spravochnik[index] = new_entry
    save_spravochnik(spravochnik)
    print("Запись отредактирована успешно.")

def search_entries(spravochnik, search_criteria):
    """Выполняет поиск записей в справочнике по заданным критериям."""
    result = [entry for entry in spravochnik if all(entry[key] == value for key, value in search_criteria.items())]
    return result

def main():
    """Основная функция, представляющая консольный интерфейс справочника."""
    spravochnik = load_spravochnik()

    while True:
        print("\nВыберите действие:")
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("0. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            display_entries(spravochnik)
        elif choice == "2":
            new_entry = {
                "Фамилия": input("Введите фамилию: "),
                "Имя": input("Введите имя: "),
                "Отчество": input("Введите отчество: "),
                "Организация": input("Введите название организации: "),
                "Телефон рабочий": input("Введите телефон рабочий: "),
                "Телефон личный": input("Введите телефон личный: ")
            }
            add_entry(spravochnik, new_entry)
        elif choice == "3":
            index = int(input("Введите индекс записи для редактирования: "))
            if 0 <= index < len(spravochnik):
                new_entry = {
                    "Фамилия": input("Введите новую фамилию: "),
                    "Имя": input("Введите новое имя: "),
                    "Отчество": input("Введите новое отчество: "),
                    "Организация": input("Введите новое название организации: "),
                    "Телефон рабочий": input("Введите новый телефон рабочий: "),
                    "Телефон личный": input("Введите новый телефон личный: ")
                }
                edit_entry(spravochnik, index, new_entry)
            else:
                print("Некорректный индекс.")
        elif choice == "4":
            search_criteria = {
                key: input(f"Введите значение для {key}: ") for key in ["Фамилия", "Имя", "Отчество", "Организация", "Телефон рабочий", "Телефон личный"]
            }
            result = search_entries(spravochnik, search_criteria)
            if result:
                display_entries(result)
            else:
                print("Записей не найдено.")
        elif choice == "0":
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите корректное значение.")

if __name__ == "__main__":
    main()
