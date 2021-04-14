Text = input("Text:")
Text = Text.split()
    #["this", "is", "a", "collection", "of", "words", "of", "nice", "words", "this", "is", "a", "fun", "thing", "it", "is"]
print("Text: this is a collection of words of nice words this is a fun thing it is")
word_to_count = {}
for word in Text:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
print(word_to_count)

