# English to Pig Latin
print("Enter the English message to translate into Pig Latin:")
inputString = input()
VOWELS = ("a", "e", "i", "o", "u")

# Split the string according to the input
stringList = inputString.split(" ")

pigLatin = []
for word in stringList:
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ""
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    # Check that there are still characters
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Remove non-letters from the suffix
    suffixNonLetters = ""
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Check whether the word was originally upper or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower()  # Make the word lowercase for translation.

    # Translate to pig latin
    prefixConsonants = ""
    while len(word) > 0 and word[0] not in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    if prefixConsonants != "":
        word = word + prefixConsonants + "ay"
    else:
        word = word + "yay"

    # Set the word back to uppercase or title case
    if wasUpper:
        word = word.upper()
    elif wasTitle:
        word = word[0].upper() + word[1:]

    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(" ".join(pigLatin))
