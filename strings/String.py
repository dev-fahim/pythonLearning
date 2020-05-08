string = "Fahim Al Islam"
x = 12
# Immutable and Mutable


def replacer(variable: str, index: int, word: str):
    return variable[:index] + word + variable[index + 1:]


print(replacer(string, 2, 'k H'))

