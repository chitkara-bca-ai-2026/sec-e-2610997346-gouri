print("="*50)
print("           TEXT PROCESSING TOOL             ")
print("="*50)
x=input("Enter a sentence:")
print()

print("--- Processing Results ---")
indexing=int(input("Enter position for indexing:"))
print(f"Character at position{indexing}:'{x[indexing]}'")

start=int(input("Enter start index for slicing    : "))
end=int(input("Enter end index for slicing   : "))
slicing=x[start:end]
print(f"Sliced string[{start}:{end}]         : '{slicing}'")

print(f"UpperCase                    :{x.upper()}")

print(f"LowerCase                    :{x.lower()}")

word_to_replace=input("Enter a word to Replace  : ")
replacement_word=input("Enter Replacement Word   : ")
replaced_word=x.replace(word_to_replace,replacement_word)
print(f"After Replace         :{replaced_word}")

print(f"Lenght of the sentence     :{len(x)}")
print()

print("="*50)
print("Analysis Complete!")
print("="*50)