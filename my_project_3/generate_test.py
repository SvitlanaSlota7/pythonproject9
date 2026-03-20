test_content = """Привіт поціновувач Python.
Це тестовий файл
Він імітує утиліту wc, підраховуючи рядки, слова та символи за один прохід читання файлу"""

with open("test_file.txt", "w", encoding="utf-8") as f:
    f.write(test_content)

print("Файл 'test_file.txt' створено. Можна тестувати!")