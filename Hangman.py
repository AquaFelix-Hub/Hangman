import random

# Wörterliste
words = ["python", "flugzeug", "schule", "programmieren", "spiele", "htl", "computer"]

# Zufälliges Wort auswählen
word = random.choice(words)
guessed = ["_"] * len(word)
tries = 6  # Anzahl Fehlversuche

print("Willkommen bei Hangman!")
print(" ".join(guessed))

while tries > 0 and "_" in guessed:
    guess = input("Rate einen Buchstaben: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Bitte nur einen Buchstaben eingeben.")
        continue

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Richtig!")
    else:
        tries -= 1
        print(f"Falsch! Noch {tries} Versuche übrig.")

    print(" ".join(guessed))

if "_" not in guessed:
    print(f"Glückwunsch! Du hast das Wort '{word}' erraten.")
else:
    print(f"Game Over! Das Wort war '{word}'.")