# 🧠 General Knowledge Quiz

## 📚 Overview  
**General Knowledge Quiz** is an interactive application developed in **Python with PyQt5**, designed to test users' knowledge in various domains such as History, Geography, and Sports.  

This application was created as part of an academic assignment.

---

## 🎮 Features

### ✅ Main Functionalities
- Quiz theme selection: **History**, **Geography**, or **Sports**
- Difficulty level choice: **Easy**, **Medium**, **Hard**
- Dynamic display of questions and answer options
- Score update after each response
- Final score display with quiz restart option
- Intuitive and fluid interface

### 💡 Game Modes

#### Classic Mode
- 10 multiple-choice questions
- 1 point per correct answer
- Simple and direct scoring

#### Challenge Mode *(additional feature)*
- Possible answers with multiple hint levels:
  - Direct input answer: 5 points
  - 4-option hint: 3 points
  - 2-option hint: 1 point
- Dynamic scoring system for more challenge

---

## 🗃️ Question Management
Questions, answer options, and correct answers are stored in an easily modifiable JSON file:  
`src/quiz_data.json`

---

## 🧰 Technologies Used
- **Python**
- **PyQt5** for graphical interface
- **JSON** for question storage

---

## ▶️ Installation & Launch

```bash
# Clone the repository
git clone (https://github.com/Jorisdagand/HMI_DM.git
cd hmi_dm

# Install dependencies
pip install PyQt5

# Launch the application
python main.py
```

---

## 📁 Project Structure

```
hmi_dm/
├── main.py               # Application entry point
├── classic_mode.py       # Classic mode logic
├── challenge_mode.py     # Challenge mode logic
└── src/
    └── quiz_data.json    # JSON question file
```

---

## 🤝 Contribution
Suggestions and improvements are welcome!  
Feel free to open a *Pull Request* or submit an *issue*.
