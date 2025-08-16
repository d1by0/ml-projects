# Importing string module to handle punctuation
import string
from collections import Counter
import matplotlib.pyplot as plt


# Step 1: Reading the input text from a file named 'read.txt'
# This file should contain the user's input text (like a paragraph or sentence)
text = open('read.txt', encoding="utf-8").read()

# Step 2: Converting all characters in the text to lowercase
lower_case = text.lower()

# Step 3: Removing all punctuation from the text using translate() and string.punctuation
cleaned_text = lower_case.translate(str.maketrans("", "", string.punctuation))

# Step 4: Splitting the cleaned text into individual words (tokens)
tokenized_words = cleaned_text.split()

# Defining a list of common stop words (words that are not useful for analysis)
# These are words like "the", "is", "in", "on", etc., which don’t carry strong meaning
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized list. Only keeping meaningful words that are not in the stop_words list
final_words = []

for words in tokenized_words:
    if words not in stop_words:
        final_words.append(words)

# This is the list that will be used for sentiment/emotion analysis
### print(final_words)

# **NLP Emotion Algorithm**

# 1. Checking if the word in the final_words list is also present in emotion.txt
# 2. If word is present -> Add the emotion to emotion_list
# 3. Finally count each emotion in the emotion list

emotion_list = []

with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'')
        if ':' in clear_line:
            word, emotion = clear_line.split(":")
            word = word.strip()
            emotion = emotion.strip()

            if word in final_words:
                print(f"Matched: {word} → {emotion}\n")
                emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print("\n",w)

most_common = w.most_common()
top_emotion, top_count = most_common[0]
other_emotions = [emotion for emotion, count in most_common[1:]]
summary = f"\nThe text expresses mostly *{top_emotion}* emotions."
if other_emotions:
    others = ", ".join(other_emotions)
    summary += f"\nThere are also traces of {others}."

print(summary)

plt.figure(figsize=(8, 5))
plt.bar(w.keys(),w.values())
plt.title("Emotion Count")
plt.xlabel("Emotions")
plt.ylabel("Frequency")
plt.xticks(rotation=45, ha='right') 
plt.tight_layout() # Tight layout to prevent label cutoff

# Show summary text inside plot
plt.text(
    0.95, 0.95, summary,
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment='top',
    horizontalalignment='right',
    bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray')
)

plt.savefig('graph.png')

plt.show(block=True)

