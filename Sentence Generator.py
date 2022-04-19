def words(noun, verb, adjective):
    noun1 = input(noun)
    verb1 = input(verb)
    adjective1 = input(adjective)

    sentence = print(noun1 + " is a " + adjective1 + " "+ verb1)

    return sentence

def Main():


        print(words("Please enter a noun", "Please enter a verb", "Please enter an adjective"))


if __name__=="__main__":
    Main()