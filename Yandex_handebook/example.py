from string import ascii_lowercase, ascii_uppercase

letters = ascii_lowercase


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def save_to_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)


def code_text(text, step):
    coding_text = ""
    for s in text:
        if s in ascii_lowercase:
            n = (ascii_lowercase.index(s) + step) % len(ascii_lowercase)
            coding_text += ascii_lowercase[n]
        elif s in ascii_uppercase:
            n = (ascii_uppercase.index(s) + step) % len(ascii_uppercase)
            coding_text += ascii_uppercase[n]
        else:
            coding_text += s
    return coding_text


if __name__ == '__main__':

    text = read_file("public.txt")
    step = int(input())
    coded_text = code_text(text, step)
    save_to_file("private.txt", coded_text)
