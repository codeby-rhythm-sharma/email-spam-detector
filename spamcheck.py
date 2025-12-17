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

def main():
    sender_email = input("Enter sender email address: ")
    email_text = input("Enter email text: ")

    spam_result = is_spam(email_text)
    domain_score = sender_domain_score(sender_email)

    if "SPAM ALERT" in spam_result or domain_score >= 2:
        print("⚠️ High risk email detected\n")
    else:
        print("✔️ Email appears safe\n")

    print(spam_result)

SUSPICIOUS_DOMAINS = [
    "mail-update.xyz",
    "secure-login.net",
    "account-alerts.co",
    "verify-now.info"
]

def sender_domain_score(sender_email):
    if "@" not in sender_email:
        return 1  # malformed sender address

    domain = sender_email.split("@")[-1].lower()

    if domain in SUSPICIOUS_DOMAINS:
        return 2

    return 0
def main():
    sender_email = input("Enter sender email address: ")
    email_text = input("Enter email text: ")

    spam_result = is_spam(email_text)
    domain_score = sender_domain_score(sender_email)

    if "SPAM ALERT" in spam_result or domain_score >= 2:
        print("⚠️ High risk email detected\n")
    else:
        print("✔️ Email appears safe\n")

    print(spam_result)


if __name__ == "__main__":
    main()
