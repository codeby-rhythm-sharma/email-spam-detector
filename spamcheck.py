def is_spam(text):
    spam_keywords = [
        "win money", "congratulations", "free gift", "urgent",
        "click here", "limited offer", "verify your account",
        "you have been selected", "claim now"
    ]

    text_lower = text.lower()
    hits = [word for word in spam_keywords if word in text_lower]

    if hits:
        return "⚠️ SPAM ALERT\nFound keywords:\n" + "\n".join("- " + w for w in hits)
    return "✔️ Not spam. No suspicious keywords detected."

email = input("Enter email text: ")
print(is_spam(email))
