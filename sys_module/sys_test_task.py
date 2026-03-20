import sys
import os
import shutil

def run_sys_path_experiment():
    print("Дослідження модуля sys та sys.path")

    # Тест 1. Аналіз початкового стану
    print("\n[ТЕСТ 1] Початковий стан sys.path")
    print(f"Кількість шляхів за замовчуванням: {len(sys.path)}")
    # Перевіримо перші 3 шляхи
    for i, path in enumerate(sys.path[:3]):
        print(f"  {i + 1}. {path}")

    if '' in sys.path or os.getcwd() in sys.path:
        print("Результат: поточна директорія автоматично включена в пошук.")

    print("\n[ТЕСТ 2] Спроба імпорту з невідомої директорії")
    temp_folder = os.path.abspath("external_test_library")
    module_name = "remote_module"

    # Створюю тимчасову папку та файл модуля
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    with open(os.path.join(temp_folder, f"{module_name}.py"), "w", encoding="utf-8") as f:
        f.write("def status(): return 'Модуль знайдено в кастомному шляху!'\n")

    # Намагаюсь імпортувати без додавання в sys.path
    try:
        import remote_module
    except ImportError:
        print("Очікується що Python не бачить модуль 'remote_module'.")

    # 3. Додаємо шлях та імпортуємо
    sys.path.append(temp_folder)
    print(f" Додано {temp_folder} до sys.path.")

    import remote_module
    print(f"Результат: {remote_module.status()}")

    # Тест 3 Вплив на ієрархію пошуку
    print("\n[ТЕСТ 3] Видалення шляху та блокування доступу")

    # Видаляємо шлях
    if temp_folder in sys.path:
        sys.path.remove(temp_folder)
        print(f"ДІЯ: Шлях {temp_folder} видалено.")

    # Очищуємо кеш імпортованих модулів щоб Python не взяв його з пам'яті)
    if module_name in sys.modules:
        del sys.modules[module_name]
        print(f"ДІЯ: Модуль '{module_name}' видалено з кешу sys.modules.")

    try:
        import remote_module
    except ImportError:
        print("Результат дослідження: модуль знову недоступний. sys.path дійсно керує пошуком.")

    # видаляю тимчасову папку тесту

    confirm = input("Видалити тимчасову папку тесту? (y/n): ")
    if confirm.lower() == 'y':
        shutil.rmtree(temp_folder)
        print("Тимчасові файли видалено.")


if __name__ == "__main__":
    run_sys_path_experiment()