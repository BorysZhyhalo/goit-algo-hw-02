from queue import Queue
import time

# Створити чергу заявок
request_queue = Queue()
request_id = 0


def generate_request():
    """Створити нову заявку та додати її до черги."""
    global request_id
    request_id += 1

    request = {
        "id": request_id,
        "status": "new"
    }

    request_queue.put(request)
    print(f"Заявка #{request['id']} створена та додана в чергу.")


def process_request():
    """Видалити заявку з черги та обробити її."""
    if not request_queue.empty():
        request = request_queue.get()
        request["status"] = "processed"
        print(f"Заявка #{request['id']} оброблена.")
    else:
        print("Черга порожня.")


def main():
    """
    Головний цикл програми:
    автоматично створює та обробляє заявки,
    поки користувач не завершить програму.
    """
    print("Програма запущена. Введіть 'exit' для завершення.")

    while True:
        command = input("Натисніть Enter для наступного кроку або 'exit': ").strip().lower()

        if command == "exit":
            print("Програму завершено.")
            break

        generate_request()   # Автоматичне створення заявки
        process_request()    # Послідовна обробка заявки
        print("-" * 40)

        time.sleep(1)  # Імітація часу між кроками


if __name__ == "__main__":
    main()