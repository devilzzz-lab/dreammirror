def get_support_reply(message: str) -> str:
    message = message.lower()

    # Greetings
    if any(word in message for word in ["hello", "hi", "hey", "greetings"]):
        return "👋 Hello! I'm DreamMirror Support Bot. How are you feeling today?"

    # Help or guidance
    elif any(word in message for word in ["help", "guide", "assist"]):
        return "🛠️ You can describe your dream, and I'll help analyze and visualize it. You can also share how you're feeling."

    # Gratitude
    elif any(word in message for word in ["thanks", "thank you", "thx"]):
        return "🙏 You're very welcome! 💛"

    # Sad / low mood
    elif any(word in message for word in ["sad", "low", "down", "unhappy", "depressed", "blue"]):
        return "💛 I'm sorry you're feeling down. It might help to describe your dream or talk about what's bothering you."

    # Loneliness / isolation
    elif any(word in message for word in ["lonely", "alone", "isolated", "solitary"]):
        return "🤗 Feeling lonely is tough. Remember, sharing your dreams or thoughts here can lighten your mood."

    # Anxiety / stressed
    elif any(word in message for word in ["anxious", "stress", "stressed", "nervous", "worried"]):
        return "🌿 Take a deep breath. Would you like to describe a dream or share what's causing your stress?"

    # Happiness / excitement / positive
    elif any(word in message for word in ["happy", "good", "great", "excited", "joyful", "content"]):
        return "🎉 That's wonderful! Care to share your happy dream or moment?"

    # Sleep / dreams related
    elif any(word in message for word in ["dream", "nightmare", "sleep", "sleepy"]):
        return "🌙 Tell me about your dream, and I'll help analyze and visualize it."

    # General fallback – encourages sharing feelings
    else:
        return "🤖 I'm here to listen. Can you tell me more about how you're feeling or your dream?"
