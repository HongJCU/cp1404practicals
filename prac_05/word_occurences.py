"""
Word Occurrences
Estimate: 30 minutes
Actual:   32 minutes
"""

#Adding the function request user to type the text, program will spit and count it
text = input("Text: ")
words = text.split()
print(words)

counts ={}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)

#Get a sorted output by alphabetically by words
sorted_words = sorted(counts.keys())

# Find the longest word and print alligned column
max_width = max(len(w) for w in sorted_words)

for w in sorted_words:
    print(f"{w:{max_width}} : {counts[w]}")
print(sorted_words)

