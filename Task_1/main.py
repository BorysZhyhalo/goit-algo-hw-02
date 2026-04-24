from queue import Queue

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
        print("Черга порожня. Немає заявок для обробки.")


def show_queue_size():
    """Показати кількість заявок у черзі."""
    print(f"Кількість заявок у черзі: {request_queue.qsize()}")


def main():
    print("Програма обробки заявок запущена.")
    print("Доступні команди:")
    print("create  - створити нову заявку")
    print("process - обробити першу заявку з черги")
    print("status  - показати кількість заявок у черзі")
    print("exit    - завершити програму")
    print("-" * 40)

    while True:
        command = input("Введіть команду: ").strip().lower()

        if command == "create":
            generate_request()

        elif command == "process":
            process_request()

        elif command == "status":
            show_queue_size()

        elif command == "exit":
            print("Програму завершено.")
            break

        else:
            print("Невідома команда. Використайте: create, process, status або exit.")

        print("-" * 40)


if __name__ == "__main__":
    main()