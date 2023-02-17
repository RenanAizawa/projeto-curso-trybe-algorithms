def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if not word:
        return False
    if high_index == 0:
        return word[low_index] == word[high_index]
    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False
