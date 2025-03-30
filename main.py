import random

# ASCII Art for Dice Faces
dice_faces = {
    1: "⚀", 2: "⚁", 3: "⚂",
    4: "⚃", 5: "⚄", 6: "⚅"
}

def roll_dice():
    while True:
        startv_ = input("🎲 WELCOME TO DICE ROLL! Type 0 and press Enter to START: ").strip().lower()
        if startv_ == "0":
            break  # Start game only when '0' is entered

    while True:
        result = random.randint(1, 6)
        print(f"\n🎲 You rolled: {dice_faces[result]} ({result})")

        roll_again = input("Roll again? (y/n): ").strip().lower()
        if roll_again != 'y':
            print("👋 Thanks for playing!")
            break

roll_dice()
