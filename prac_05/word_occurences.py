"""
Word Occurrences
Estimate: 30 minutes
Actual:   40 minutes
"""

#Adding the function request user to type the text, program will spit and count it
text = input("Text: ").lower()
words = text.split()

# Counting the words
counts ={}
for word in words:
    counts[word] = counts.get(word, 0) + 1

#Get a sorted output by alphabetically by words
sorted_words = sorted(counts.keys())

# Find the longest word and print alligned column
max_width = max(len(w) for w in sorted_words)
for w in sorted_words:
    print(f"{w:{max_width}} : {counts[w]}")


