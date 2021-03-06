import os

def main():
    os.chdir("FilesToSort")
    extension_to_category = {}
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            extension_to_category[extension] = category
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print("{} is the {}".format(filename, extension))
        os.rename(filename, ("{} is the {}".format(filename, extension)))
main()