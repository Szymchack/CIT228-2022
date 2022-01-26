rivers={
    'Amazon':['Peru, Columbia, Brazil, Bolivia, Venezuela, Ecuador, and Guyana'],
    'Rio Negro':['Brazil, Columbia, and Venezuela'],
    'Orinoco':['Venezuela, and Columbia']
}

for key, value in rivers.items():
    if type(value)==list:
        print(f"The {\nkey.title()} river flows through:")
        for v in value:
            print("\t",v)
    else:
        print(f"The{key.title()} river flows through {value.title()}")