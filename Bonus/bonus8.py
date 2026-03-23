filenames = ["1.doc", "1.report", "1.presentation"]
# we want to transform the "." to a "-" and add ".txt". to do this, we use a list comprehension
filenames =[filename.replace(".", "-") + ".txt" for filename in filenames]

print(filenames)