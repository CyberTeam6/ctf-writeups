story = open('final.txt', 'r')

def uppercase(s):
    upper_chars = ""
    for char in s:
        if char.isupper() == True:
            upper_chars += char
    return upper_chars

print uppercase(story.read())


