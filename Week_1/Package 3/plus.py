phrase = "This is my test phrase."


def make_snake_case(words: str):
    individual_substrings = words.split()
    print(individual_substrings)
    for substring in individual_substrings:
        print(result)
        result += substring.lower() + "_"
        print (result)

        return result.strip("._")
