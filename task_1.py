from collections import Counter

def count_ukraine_sentence():
    sentence = "Україна вільна країна"

    # розбиваємо на слова
    words = sentence.lower().split()

    # рахуємо слова
    word_counts = Counter(words)

    print(f"Аналіз речення: '{sentence}'")
    print("-" * 30)

    for word, count in word_counts.items():
        print(f"Слово '{word}' зустрічається {count} раз")

if __name__ == "__main__":
    count_ukraine_sentence()