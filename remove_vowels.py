sentence = "The quick brown dog jumped over the lazy purple dinosaur"
split_sentence = sentence.split()
vowels = list('aeiou')
output = []

for word in split_sentence:
    state_list = list(word.lower())

    for vowel in vowels:
        while True:
            try:
                state_list.remove(vowel)
            except:
                break
    output.append(''.join(state_list).capitalize())

print(output)
