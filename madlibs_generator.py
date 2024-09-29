with open("story.txt", 'r') as f:
    story = f.read()

word_dict = {} 
start_of_word = -1
end_of_word = -1

for i, char in enumerate(story):
    if char == '<':
        start_of_word = i + 1
    elif char == '>':
        key_word = story[start_of_word:i]
        word_dict[key_word] = None

vowels = ['a', 'e', 'i', 'o', 'u']
for key in word_dict:
    if key[0:1] in vowels:
        string_val = input('Give me an ' + key + ': ')
    else:
        string_val = input('Give me a ' + key + ': ')
    
    word_dict[key] = string_val

for key in word_dict:
    story = story.replace(f'<{key}>', word_dict[key])

print(story)



