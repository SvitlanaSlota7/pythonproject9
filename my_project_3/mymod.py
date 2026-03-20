import os


def count_lines(file_obj):
    file_obj.seek(0)
    return len(file_obj.readlines())

def count_words(file_obj):
    file_obj.seek(0)
    return len(file_obj.read().split())

def count_chars(file_obj):
    file_obj.seek(0)
    return len(file_obj.read())

def test(name):
    """Повний аналіз файлу"""
    if not os.path.exists(name):
        print(f"Помилка: Файл '{name}' не знайдено.")
        return

    with open(name, 'r', encoding='utf-8') as f:
        lines = count_lines(f)
        words = count_words(f)
        chars = count_chars(f)


        print(f"Звіт для файлу: {name}")

        print(f"Рядків:   {lines}")
        print(f"Слів:     {words}")
        print(f"Символів: {chars}")


if __name__ == "__main__":
    test("mymod.py")