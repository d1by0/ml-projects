### Sentiment Analysis Web App Using Streamlit

**What’s This About?** - This project is designed to help you understand how to build and deploy a sentiment analysis web application using Streamlit. It’s a great starting point if you’re new to natural language processing (NLP) and want hands-on experience with detecting emotions in text through a user-friendly interface.

**Why Should You Care?** - Sentiment analysis is widely used in many real-world applications such as customer feedback, social media monitoring, and mental health tools. This project will guide you through implementing a simple yet effective lexicon-based emotion detection system, making it perfect for beginners who want to grasp essential NLP concepts with practical code examples.

**Objective** - This project helps you implement and understand a lexicon-based sentiment analysis app that maps words from user input text to emotions, provides summaries, and visualizes the results.

**What’s Inside?**
- emotion_app.py — The Streamlit app source code managing UI, emotion analysis, and visualization
- emotions.txt — The emotion lexicon mapping words to specific emotion categories
- config.toml — The app’s theme configuration file for styling

**How Does It Work?** - You input text in the web app, which processes your words by cleaning and filtering them, then matches them to emotions defined in the lexicon. The app counts and summarizes the dominant emotions, presents an emoji-enhanced breakdown, and displays a bar chart to visualize emotion frequency.

**How Do You Run This?**
1. Ensure you have Python installed (version 3.6 or higher).
2. Install the required packages via terminal or command prompt: `pip install streamlit matplotlib`
3. Launch the app with the command: `streamlit run emotion_app.py`
4. Enter or paste your text in the app interface’s input box and click “Analyze Emotions” to see the results.

**What Will You Learn?**
- How to build an interactive web interface using Streamlit
- How to preprocess and clean text data for emotion analysis
- How to leverage a word-to-emotion lexicon for basic sentiment detection
- How to summarize and visualize emotion data effectively

**Need Help?** - No worries, I was just like you when I started. Take it slow, read the comments, Google stuff if you’re stuck. You got this!
