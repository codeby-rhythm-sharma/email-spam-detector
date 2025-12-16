# Phishing keyword heuristic (basic security enhancement)

PHISHING_KEYWORDS = [
    "verify your account",
    "urgent action required",
    "click here",
    "password reset",
    "suspended account",
    "login immediately"
]

def phishing_keyword_score(text):
    text = text.lower()
    score = 0
    for keyword in PHISHING_KEYWORDS:
        if keyword in text:
            score += 1
    return score
def main():
    email_text = input("Enter email content: ")

    score = phishing_keyword_score(email_text)

    if score >= 2:
        print("⚠️ Possible phishing indicators detected")
    else:
        print("No obvious phishing indicators found")


if __name__ == "__main__":
    main()
