def main():
    title =input("Title:")
    search_phrase = input("search phrase:")
    print("title is ",title)
    print("search phrase is ",search_phrase)
    while title and search_phrase != " ":
        title = input("Title:")
        search_phrase = input("search phrase:")
        print("title is ", title)
        print("search phrase is ", search_phrase)
    else:
        print("done")

main()