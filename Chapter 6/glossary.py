glossary={
    'dictionary':'A collection of key-value pairs.',
    'key value pairs':'is an unordered collection of data values, used to store data values like a map',
    'variables':'are nothing but reserved memory locations to store values.',
    'tuple':'is one of 4 built-in data types in Python used to store collections of data which is ordered and unchangeable',
    'data types':'Since everything is an object in Python, data types are actually classes and variables are instance of these classes.',
    'del':'command used to remove a key:value pair from the dictionary',
    'key':'value used to access data stored in the dictionary or glossary',
    'conditional test':'a comparison between two values',
    'boolean':'an expression that evaluates to "true" or "false"',
    'value':'an item associated with a key in dictionary or glossary'
}

print("dictionary:")
print("\t",glossary["dictionary"])
print("key value pairs:")
print("\t",glossary["key value pairs"])
print("variables:")
print("\t",glossary["variables"])
print("tuple:")
print("\t",glossary["tuple"])
print("data types:")
print("\t",glossary["data types"])

print("--------------------6-4--------------------")

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
