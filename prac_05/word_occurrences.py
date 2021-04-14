Text = input("Text:")
Text = Text.split()
word_to_count = {}
for word in Text:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
print("{:{}} = {}".format(0, 1, word_to_count))

