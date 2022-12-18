"""

ДЗ 15. Предложение из первых слов предложений

"""


def generate_sentence(text: str) -> str:
    import re
    pattern = r'([A-Z][^\.!?]*[\.!?]*)'
    sentences = re.findall(pattern, text)
    words = []
    for i in sentences:
        first_word = re.findall(r'\w+', i)[0]
        words.append(first_word)
    new_str = ' '.join(words) + '.'
    res = new_str.capitalize()
    return res
