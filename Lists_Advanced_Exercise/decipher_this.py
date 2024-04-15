list_of_encrypted_words = input().split()
result = ""
for index in range(len(list_of_encrypted_words)):
    digits = ""
    current_decrypted_word = (list_of_encrypted_words[index])
    current_decrypted_word_list = [el for el in current_decrypted_word]
    for letter in current_decrypted_word:
        if current_decrypted_word_list[0].isdigit():
            current_digit = current_decrypted_word_list.pop(0)
            digits += current_digit
    if len(current_decrypted_word_list) > 1:
        second_letter = current_decrypted_word_list.pop(0)
        last_letter = current_decrypted_word_list.pop()
        current_decrypted_word_list.insert(0, last_letter)
        current_decrypted_word_list.append(second_letter)

    first_letter = chr(int(digits))
    current_decrypted_word_list.insert(0, first_letter)

    result += ("".join(current_decrypted_word_list) + " ")

print(result)
