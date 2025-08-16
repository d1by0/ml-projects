import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
import string

# ---------------------
# Config
# ---------------------
st.set_page_config(
    page_title="Sentilytics - Your emotions are valid",
    page_icon="favicon.png",
    layout="centered"
)

# ---------------------
# App Branding
# ---------------------
st.image("logo.png", width=200)  # Your custom logo
st.title("🧠 Decode Emotions, Drive Deeper Connections.")

# ---------------------
# Load Emotion File
# ---------------------
def load_emotion_map():
    emotion_map = {}
    with open("emotions.txt", "r") as file:
        for line in file:
            clean_line = line.replace("\n", "").replace(",", "").replace("'", "")
            if ":" in clean_line:
                word, emotion = clean_line.split(":")
                emotion_map[word.strip()] = emotion.strip()
    return emotion_map

# ---------------------
# Analyze Emotions
# ---------------------
def analyze_emotions(text, emotion_map):
    text = text.lower()
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation))
    tokenized_words = cleaned_text.split()

    stop_words = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                      "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                      "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
                      "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
                      "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                      "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                      "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
                      "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                      "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                      "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"])

    final_words = [word for word in tokenized_words if word not in stop_words]
    emotion_list = [emotion_map[word] for word in final_words if word in emotion_map]
    return final_words, emotion_list, Counter(emotion_list)

# ---------------------
# Plot Bar Graph
# ---------------------
def plot_emotions(counter, summary):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(counter.keys(), counter.values(), color='skyblue')
    ax.set_title("Emotion Count")
    ax.set_xlabel("Emotions")
    ax.set_ylabel("Frequency")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Add summary text inside the plot
    plt.text(
        0.95, 0.95, summary,
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment='top',
        horizontalalignment='right',
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray')
    )
    return fig

# ---------------------
# Text Input
# ---------------------
user_input = st.text_area("Enter your emotions", height=200, placeholder="Type or paste your text here...")

# ---------------------
# Emotion Detection Trigger
# ---------------------
if st.button("Analyze Emotions"):
    if user_input.strip():
        emotion_map = load_emotion_map()
        final_words, emotion_list, w = analyze_emotions(user_input, emotion_map)

        if w:
            most_common = w.most_common()
            top_emotion, _ = most_common[0]
            other_emotions = [e for e, _ in most_common[1:]]
            summary = f"The text expresses mostly **{top_emotion}** emotions."
            if other_emotions:
                summary += f" Also present: {', '.join(other_emotions)}."

            # Emoji summary
            emotion_emoji_map = {
                "happy": "😊", "sad": "😢", "angry": "😠", "fear": "😨",
                "surprise": "😲", "love": "❤️", "hate": "💔", "disgust": "🤢"
            }

            emoji_summary = ""
            for emotion, count in w.most_common():
                emoji = emotion_emoji_map.get(emotion)
                emoji_summary += f"- **{emotion.capitalize()}** {emoji} ({count})\n"

            st.markdown(f"### 🔍 Emotional Breakdown:\n{emoji_summary}")
            st.markdown(f"### 📌 Summary:\n{summary}")

            # Optional AI-style reflection
            if top_emotion == "sad":
                st.warning("Hey, it’s okay to feel sad. You’re not alone, better days are coming 💙")
            elif top_emotion == "happy":
                st.success("Your words are shining with happiness, spread the joy 🌞")
            elif top_emotion == "angry":
                st.error("There’s some anger in your tone. It’s valid, but don’t let it consume you.")
            elif top_emotion == "love":
                st.success("Keep loving, it makes you human ❤️")
            elif top_emotion == "fear":
                st.warning("You are not alone. Take one step at a time, you’re stronger than you think.")

            # Plotting
            fig = plot_emotions(w, summary)
            st.pyplot(fig)

        else:
            st.info("No recognizable emotions found in the input text.")
    else:
        st.warning("Please enter some text to analyze.")
