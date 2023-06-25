def find_and_replace(text, word, word2):
    new_text = ''
    for i in range(len(text)):
        if text[i:i+len(word)] == word:
            new_text += text[:i] + word2 + text[i+len(word):]
    return new_text

attempt = find_and_replace('the fox', 'fox', 'dog')
print(attempt)

assert find_and_replace('the fox', 'fox', 'dog') == 'the dog'
assert find_and_replace('fox', 'fox', 'dog') == 'dog'
assert find_and_replace('Firefox', 'fox', 'dog') == 'Firedog'
assert find_and_replace('Foxfox', 'fox', 'dog') == 'Foxdog'
assert find_and_replace('The Fox and the fox', 'fox', 'dog') == 'The Fox and the dog'