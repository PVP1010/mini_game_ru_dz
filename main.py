import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_word": english_word,
            "word_definition": word_definition
        }

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def translate_to_russian(text):
    try:
        translation = GoogleTranslator(source='en', target='ru').translate(text)
        return translation
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text

def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        if word_dict is None:
            print("Не удалось получить слово. Попробуйте снова.")
            continue

        english_word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и определение на русский язык
        russian_word = translate_to_russian(english_word)
        russian_definition = translate_to_russian(word_definition)

        print(f"Значение слова: {russian_definition}")
        user_input = input("Какое это слово на русском? ")

        if user_input.lower() == russian_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, правильное слово: {russian_word}")

        play_again = input("Хотите сыграть еще раз? y/n ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

word_game()