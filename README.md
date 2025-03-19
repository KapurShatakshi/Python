# 🎯 **Hangman Game (AI Powered)**
Welcome to the **Hangman Game** – A modern twist on the classic Hangman game built using **Python (Tkinter)** and enhanced with **Pygame** for sound effects and smooth gameplay!  

---

## 🚀 **Project Overview**  
The Hangman Game challenges players to guess a hidden word within a limited number of chances. It's powered by AI to generate dynamic categories and hints, providing a fresh experience every time!  

✅ Built with a user-friendly interface using **Tkinter**  
✅ Smooth sound effects using **Pygame**  
✅ Dynamic word selection using **AI-generated categories**  
✅ Persistent leaderboard to track wins and losses  

---

## 🌟 **Features**  
### 🎭 **AI-Powered Categories and Words**  
- Words are generated dynamically from AI-generated categories.  
- Hints are based on categories like Movies, Fruits, Technologies, and more.  

### 🔊 **Sound Effects**  
- ✅ Correct Guess → Plays a positive sound  
- ❌ Wrong Guess → Plays a negative sound  
- 🏆 Win or Lose → Special sound for win/lose scenario  

### 💡 **Dynamic UI with Animation**  
- Real-time feedback on correct/incorrect guesses  
- Hangman drawing updates with each wrong guess  
- Colorful buttons for an interactive feel  

### 🏆 **Leaderboard**  
- Tracks wins and losses  
- Persistent leaderboard saved locally  

---

## 🖥️ **Demo**  
![Hangman Game](https://media.giphy.com/media/3o7TKsQk9xL4l1Yyis/giphy.gif)  

---

## 📂 **Project Structure**  
```
📦 Hangman-Game
├── 📄 hangman.py         # Main game logic
├── 📄 leaderboard.txt     # Stores win/loss record
├── 🎵 correct.wav         # Sound for correct guesses
├── 🎵 wrong.wav           # Sound for incorrect guesses
├── 🎵 win.wav             # Sound for winning
├── 🎵 lose.wav            # Sound for losing
├── 🖼️ background.png      # Background image
├── 🖼️ win.png             # Image shown on winning
├── 🖼️ lose.png            # Image shown on losing
└── 📄 README.md           # Project documentation
```

---

## 🚀 **How to Run**  
### 1. **Clone the Repository**  
Open your terminal and run:  
```bash
git clone https://github.com/your-username/hangman-game.git
```

### 2. **Navigate to Project Directory**  
```bash
cd hangman-game
```

### 3. **Install Dependencies**  
Ensure Python and Pygame are installed:  
```bash
pip install pygame
```

### 4. **Run the Game**  
```bash
python hangman.py
```

---

## 🎮 **How to Play**  
1. A random word from a random category will be shown as blanks (`_ _ _`).  
2. Click on the letter buttons to guess the word.  
3. Each wrong guess will result in part of the hangman being drawn.  
4. If you guess the word before the hangman is completed → **YOU WIN** 🏆  
5. If the hangman is completed → **YOU LOSE** 💀  

---

## ⚙️ **Game Logic**  
✔️ The AI generates categories and words dynamically.  
✔️ Number of chances = `unique characters in the word + 4`  
✔️ Correct guesses fill the blanks.  
✔️ Wrong guesses update the hangman drawing.  

---

## 🏆 **Leaderboard**  
- Wins and losses are tracked and stored in `leaderboard.txt`.  
- The leaderboard updates in real-time and persists after closing the game.  

---

## 🛠️ **Technologies Used**  
| **Technology** | **Purpose** |
|---------------|-------------|
| Python | Core language |
| Tkinter | GUI development |
| Pygame | Sound effects |
| OS Module | File handling |
| Random | Word and category generation |

---

## 🚀 **Future Improvements**  
✅ Add difficulty levels  
✅ Introduce multiplayer mode  
✅ Enhance AI-based word and category selection  

---

## 💡 **Contributing**  
Contributions are welcome!  
1. Fork the repository  
2. Create a new branch:  
```bash
git checkout -b feature/your-feature-name
```
3. Make your changes and commit:  
```bash
git commit -m "feat: added new category"
```
4. Push to your branch:  
```bash
git push origin feature/your-feature-name
```
5. Create a pull request  

---

## 📜 **License**  
This project is licensed under the **MIT License** – feel free to modify and use it!  

---

## ❤️ **Acknowledgements**  
- Inspired by the classic Hangman Game  
- Special thanks to the Python and open-source community  

---

🎯 **Ready to challenge yourself? Start playing now!** 😎
```

---

This README is clean, professional, and well-organized — ready to be added directly to your GitHub repository! 😎