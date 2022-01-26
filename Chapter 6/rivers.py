rivers={
    'Amazon':'Peru, Columbia, Brazil, Bolivia, Venezuela, Ecuador, and Guyana',
    'Rio Negro':'Brazil, Columbia, and Venezuela',
    'Orinoco':'Venezuela, and Columbia'
}
for river, country in rivers.items():
    print("The " + river.title() + " river flows through " + country.title() + ".")

print("\n The items in the key list for rivers are:")
for river in rivers.keys():
    print("- " + river.title())

print("\n The items in the values list for countries are:")
for country in rivers.values():
    print("- " + country.title())