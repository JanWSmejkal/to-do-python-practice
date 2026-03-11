file = open("bear.txt", "r")
content = file.read()
file.close()
print(content)

file = open("essay.txt", "r")
content = file.read()
file.close()
print(content.title())

file = open("essay.txt", "r")
content = file.read()
file.close()
print(len(content))

file = open("essay.txt", "r")
content = file.read()
file.close()
print(f"The file contains {len(content)} characters. ")

"Solution says:"
"file = open('essay.txt', 'r')"
"content = file.read()"
"file.close()"

"nr_chars = len(content)"
"message = f'The file contains {nr_chars} characters.'"
"print(message)"