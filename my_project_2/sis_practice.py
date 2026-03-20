import sys
import os

def dynamic_setup():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # шлях до зовнішньої теки
    parent_dir = os.path.dirname(current_dir)
    external_folder = os.path.join(parent_dir, "my_other_folder")

    print(f"Шукаємо в: {external_folder}")

    # додаємо в sys.path, якщо такого шляху там ще немає
    if external_folder not in sys.path:
        sys.path.append(external_folder)

    try:
        import secret_module
        print("Підключено")
    except ImportError:
        print("Папку знайдено, але файла secret_module.py там немає.")


if __name__ == "__main__":
    dynamic_setup()