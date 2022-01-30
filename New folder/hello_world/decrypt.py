def lasso_letter( letter, shift_amount ):
    letter_code = ord(letter.lower())
    decoded_letter_code = letter_code + shift_amount
    decoded_letter = chr(decoded_letter_code)
    return decoded_letter

print(lasso_letter('a', 2))
print(lasso_letter('N', 13))