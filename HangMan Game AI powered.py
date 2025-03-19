import tkinter as tk
import random
import pygame
import os

# Initialize Pygame for sound effects
pygame.mixer.init()
correct_sound = "correct.wav"
wrong_sound = "wrong.wav"
win_sound = "win.wav"
lose_sound = "loose.wav"

# Categories with hints
categories = {
    "Movie": ["bahubali", "inception", "avengers", "joker"],
    "Fruit": ["guava", "banana", "strawberry", "mango"],
    "Smartest Phone Ever": ["iphone", "samsung galaxy", "pixel"],
    "Social Media": ["facebook", "instagram", "tiktok", "whatsapp"],
    "Recent Technology": ["artificial intelligence", "blockchain", "quantum computing"]
}

# Leaderboard file
LEADERBOARD_FILE = "leaderboard.txt"

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return int(f.readline().strip()), int(f.readline().strip())
    return 0, 0  # Default wins/losses

def save_leaderboard(wins, losses):
    with open(LEADERBOARD_FILE, "w") as f:
        f.write(f"{wins}\n{losses}")

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎭 Hangman Game 🎭")
        self.root.geometry("600x700")
        
        # Set Background Image
        self.bg_image = tk.PhotoImage(file="background.png")  # Make sure you have this image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)
        
        self.wins, self.losses = load_leaderboard()
        
        # Select a random category and word
        self.category, words = random.choice(list(categories.items()))
        self.word = random.choice(words).lower()
        self.chances = len(set(self.word)) + 4
        self.guessed_letters = set()
        self.display_word = ["_" if ch != " " else " " for ch in self.word]
        
        # Title Label
        self.title_label = tk.Label(root, text=f"🎯 Guess the {self.category}!", font=("Arial", 22, "bold"), bg="lightblue")
        self.title_label.pack(pady=10)
        
        # Word Display
        self.word_label = tk.Label(root, text=" ".join(self.display_word), font=("Arial", 28), bg="white")
        self.word_label.pack(pady=10)
        
        # Chances Label
        self.chances_label = tk.Label(root, text=f"Chances left: {self.chances}", font=("Arial", 18), bg="lightyellow")
        self.chances_label.pack(pady=10)
        
        # Hangman Drawing Canvas
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack(pady=10)
        
        # Buttons for Letters with Colorful Palette
        self.buttons_frame = tk.Frame(root, bg="white")
        self.buttons_frame.pack()
        self.buttons = {}

        colors = ["red", "green", "blue", "purple", "orange", "brown"]
        for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
            btn = tk.Button(self.buttons_frame, text=letter.upper(), width=4, height=2, 
                            bg=colors[i % len(colors)], fg="white", font=("Arial", 14, "bold"),
                            command=lambda l=letter: self.letter_click(l))
            btn.grid(row=i // 6, column=i % 6, padx=5, pady=5)
            self.buttons[letter] = btn
        
        # Restart Button
        self.restart_button = tk.Button(root, text="🔄 Restart", command=self.restart_game, font=("Arial", 18), bg="lightgreen")
        self.restart_button.pack(pady=15)
        
        # Leaderboard Display
        self.leaderboard_label = tk.Label(root, text=f"🏆 Wins: {self.wins} | 💀 Losses: {self.losses}", font=("Arial", 16), bg="lightgray")
        self.leaderboard_label.pack(pady=10)
    
    def letter_click(self, letter):
        if letter in self.guessed_letters:
            return
        self.guessed_letters.add(letter)

        if letter in self.word:
            if "_" in self.display_word:  # Play only if the game is ongoing
                pygame.mixer.Sound(correct_sound).play()
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.display_word[i] = letter
            self.word_label.config(text=" ".join(self.display_word))
        else:
            if self.chances > 1:  # Play only if it's not the last attempt
                pygame.mixer.Sound(wrong_sound).play()
            self.chances -= 1
            self.chances_label.config(text=f"Chances left: {self.chances}")
            self.update_hangman()

        self.buttons[letter].config(state="disabled")

        if "_" not in self.display_word:  # WIN CONDITION
            self.chances_label.config(text="🎉 You Win! 🎉")
            self.wins += 1
            save_leaderboard(self.wins, self.losses)
            self.disable_buttons()
            pygame.mixer.Sound(win_sound).play()  # Play win sound only
            self.display_end_image("win.png")  # Show win image

        elif self.chances == 0:  # LOSE CONDITION
            self.chances_label.config(text=f"💀 You Lost! Word was '{self.word}' 💀")
            self.losses += 1
            save_leaderboard(self.wins, self.losses)
            self.disable_buttons()
            pygame.mixer.Sound(lose_sound).play()  # Play lose sound only
            self.display_end_image("lose.png")  # Show lose image

    def disable_buttons(self):
        for btn in self.buttons.values():
            btn.config(state="disabled")

    def update_hangman(self):
        parts = [
            (150, 50, 150, 100),  # Head
            (150, 100, 150, 170),  # Body
            (150, 120, 120, 140),  # Left Arm
            (150, 120, 180, 140),  # Right Arm
            (150, 170, 120, 220),  # Left Leg
            (150, 170, 180, 220)   # Right Leg
        ]
        incorrect_attempts = 6 - self.chances
        if incorrect_attempts < len(parts):
            self.canvas.create_line(parts[incorrect_attempts], width=3)

    def display_end_image(self, image_file):
        """Displays a win or lose image at the end of the game."""
        img = tk.PhotoImage(file=image_file)
        img_label = tk.Label(self.root, image=img, bg="white")
        img_label.image = img  # Keep a reference
        img_label.pack(pady=10)

    def restart_game(self):
        self.root.destroy()
        main()

def main():
    root = tk.Tk()
    HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
