from pywebio import start_server
from pywebio.input import input, TEXT, NUMBER
from pywebio.output import put_text, put_image
from pywebio.session import set_env

star_image_path = 'D:/user/Desktop/HillelPython67/five_stars.jpeg'


def quiz():
    set_env(title="Історична Вікторина")

    questions = [
        {"question": "Як вас звати?", "type": TEXT, "answer": None},
        {"question": "Коли вибухнула Чорнобильська АЕС?", "type": NUMBER, "answer": 1986},
        {"question": "Який рік відкриття Америки Колумбом?", "type": NUMBER, "answer": 1492},
        {"question": "Скільки штатів у США?", "type": NUMBER, "answer": 50},
        {"question": "Назвіть рік початку Другої світової війни?", "type": NUMBER, "answer": 1939},
        {"question": "В якому році розпався СРСР?", "type": NUMBER, "answer": 1991},
    ]

    total_score = 0

    user_name = input("Як вас звати?", type=TEXT)
    put_text(f"Привіт, {user_name}! Почнемо вікторину.")

    for q in questions[1:]:
        answer = input(q["question"], type=q["type"])

        if q["type"] == TEXT:
            if answer.strip().lower() == q["answer"]:
                total_score += 1
        elif q["type"] == NUMBER:
            if answer == q["answer"]:
                total_score += 1

    put_text(f"Ваша загальна кількість балів: {total_score}")
    if total_score == 5:
        put_image(open(star_image_path, 'rb').read())


if __name__ == '__main__':
    start_server(quiz, port=8080)
