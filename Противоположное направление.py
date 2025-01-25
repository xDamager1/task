def reverse_words(input_string):
    words = input_string.split()

    words.reverse()

    if words:
        words[0] = words[0].capitalize()
        words[1:] = [word.lower() for word in words[1:]]

    return ' '.join(words)


input_string = input("Введите строку: ")
output_string = reverse_words(input_string)
print(output_string)
