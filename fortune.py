import random

NAME = "Mohammed Abdul Mujeeb"
ADMNO = "21JE0563"
print(f"\nWelcome to {NAME}'s Fortune Teller ({ADMNO})")
mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

#v1.1
#mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

fortunes = {
    "happy": [
        f"Great things await you, {NAME} says! Keep smiling.",
        "Your positivity will light up a room today."
    ],
    "sad": [
        "Every cloud has a silver lining.... better days are coming.",
        "Remember that even rainbows need a little rain."
    ],
    "neutral": [
        "An unexpected opportunity will brighten your day.",
        "Your balance will guide you to new experiences."
    ]

    #v1.1
    # "stressed": [
    #     "Take a deep breath, clarity comes when you pause.",
    #     "A short walk outside will reset your mind."
    # ]
}

if mood in fortunes:
    choose = fortunes[mood][0]

    #v1.1
    # choose = random.choice(fortunes[mood])
    
    print(f"\nYour fortune: {choose}\n")
else:
    print("\nSorry, I don't know that mood. Please try happy, sad or neutral.\n")

    #v1.1
    # print("\nSorry, I don't know that mood. Please try happy, sad, neutral, or stressed.\n")



