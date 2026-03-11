contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "the slicing proces was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", "w")
    file.write(content)

a = " I am a string on my own" \
    "on my own"\
    "too"
print(a)