sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0
total_letters = 0

for character in sentence:
    if character.lower() in "aeiou":
        vowels += 1
        total_letters += 1
    elif character.isalpha():
        consonants += 1
        total_letters += 1
    elif character.isdigit():
        digits += 1
    elif character == " ":
        spaces += 1
    else:
        special_characters += 1

total_words = len(sentence.split())
total_characters = len(sentence)
vowel_percentage = (vowels / total_letters * 100) if total_letters else 0


print("="*50)
print("\nDOCUMENT ANALYSIS REPORT")
print("="*50)
print(f"Sentence          : {sentence}")
print(f"Total characters  : {total_characters}")
print()
print("Character Breakdown")
print(f"Words             : {total_words}")
print(f"Vowels            : {vowels}")
print(f"Consonants        : {consonants}")
print(f"Digits            : {digits}")
print(f"Spaces            : {spaces}")
print(f"Special characters: {special_characters}")
print()
print(f"Total letters     : {total_letters}")
print(f"Vowel percentage  : {vowel_percentage:.1f}%")
print()
print("Summary")
print("="*50)
print("Analysis Complete!")
print("="*50)
