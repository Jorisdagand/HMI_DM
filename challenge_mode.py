import json
import random
import os 
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QStackedWidget, QLineEdit)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QProgressBar

COLORS = {
    "primary": "#6200EA",  
    "secondary": "#03DAC6",  
    "background": "#121212",  
    "card": "#1E1E1E",  
    "text": "#FFFFFF",  
    "correct": "#4CAF50",  
    "incorrect": "#F44336",  
    "history": "#FF9800",  
    "geography": "#2196F3",  
    "sports": "#E91E63", 
    "easy": "#66BB6A",  
    "medium": "#FFA726", 
    "hard": "#EF5350"  
}

class AppStyles:
    @staticmethod
    def get_main_button_style():
        return f"""
            QPushButton {{
                background-color: {COLORS["primary"]};
                color: {COLORS["text"]};
                border: none;
                border-radius: 10px;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #7C4DFF;
            }}
            QPushButton:pressed {{
                background-color: #5502C7;
            }}
        """
    
    @staticmethod
    def get_option_button_style():
        return f"""
            QPushButton {{
                background-color: {COLORS["card"]};
                color: {COLORS["text"]};
                border: 2px solid {COLORS["secondary"]};
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                text-align: left;
            }}
            QPushButton:hover {{
                background-color: #2A2A2A;
                border: 2px solid #04F7E0;
            }}
        """
    
    @staticmethod
    def get_topic_button_style(topic):
        return f"""
            QPushButton {{
                background-color: {COLORS[topic]};
                color: {COLORS["text"]};
                border: none;
                border-radius: 10px;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {COLORS[topic]};
                opacity: 0.8;
            }}
        """
    
    @staticmethod
    def get_difficulty_button_style(difficulty):
        return f"""
            QPushButton {{
                background-color: {COLORS[difficulty]};
                color: {COLORS["text"]};
                border: none;
                border-radius: 10px;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                opacity: 0.8;
            }}
        """
    
    @staticmethod
    def get_card_style():
        return f"""
            QFrame {{
                background-color: {COLORS["card"]};
                border-radius: 15px;
                padding: 20px;
                border: 1px solid #2A2A2A;
            }}
        """
    
    @staticmethod
    def get_correct_style():
        return f"""
            QPushButton {{
                background-color: {COLORS["correct"]};
                color: {COLORS["text"]};
                border: none;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                text-align: left;
            }}
        """
    
    @staticmethod
    def get_incorrect_style():
        return f"""
            QPushButton {{
                background-color: {COLORS["incorrect"]};
                color: {COLORS["text"]};
                border: none;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                text-align: left;
            }}
        """
    
    @staticmethod
    def get_input_style():
        return f"""
            QLineEdit {{
                background-color: {COLORS["card"]};
                color: {COLORS["text"]};
                border: 2px solid {COLORS["secondary"]};
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
            }}
            QLineEdit:focus {{
                border: 2px solid #04F7E0;
            }}
        """
    
    @staticmethod
    def get_hint_button_style():
        return f"""
            QPushButton {{
                background-color: #8E24AA;
                color: {COLORS["text"]};
                border: none;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #9C27B0;
            }}
            QPushButton:pressed {{
                background-color: #7B1FA2;
            }}
        """
        
    @staticmethod
    def get_hint_level_style():
        return f"""
            QRadioButton {{
                color: {COLORS["text"]};
                font-size: 14px;
                spacing: 10px;
            }}
            QRadioButton::indicator {{
                width: 18px;
                height: 18px;
                border-radius: 9px;
                border: 2px solid {COLORS["secondary"]};
            }}
            QRadioButton::indicator:checked {{
                background-color: {COLORS["secondary"]};
                border: 2px solid {COLORS["text"]};
            }}
        """
    
    @staticmethod
    def apply_shadow_effect(widget):
        from PyQt5.QtWidgets import QGraphicsDropShadowEffect
        from PyQt5.QtGui import QColor
        from PyQt5.QtCore import QPoint
    
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(QPoint(0, 5))
        widget.setGraphicsEffect(shadow)


class WelcomeScreen(QWidget):
    def __init__(self, on_normal_mode, on_challenge_mode):
        super().__init__()
        self.on_normal_mode = on_normal_mode
        self.on_challenge_mode = on_challenge_mode
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        title_label = QLabel("GENERAL KNOWLEDGE QUIZ")
        title_label.setFont(QFont("Arial", 36, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(f"color: {COLORS['secondary']};")
        
        subtitle_label = QLabel("Test your knowledge of History, Geography and Sport")
        subtitle_label.setFont(QFont("Arial", 16))
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet(f"color: {COLORS['text']};")
        
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(20)
        
        normal_button = QPushButton("CLASSIC MODE")
        normal_button.setFixedSize(200, 60)
        normal_button.setStyleSheet(AppStyles.get_main_button_style())
        normal_button.clicked.connect(self.on_normal_mode)
        
        challenge_button = QPushButton("CHALLENGE MODE")
        challenge_button.setFixedSize(200, 60)
        challenge_button.setStyleSheet(
            f"""
            QPushButton {{
                background-color: #9C27B0;
                color: {COLORS["text"]};
                border: none;
                border-radius: 10px;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #AA47BC;
            }}
            QPushButton:pressed {{
                background-color: #8E24AA;
            }}
            """
        )
        challenge_button.clicked.connect(self.on_challenge_mode)
        
        buttons_layout.addWidget(normal_button)
        buttons_layout.addWidget(challenge_button)
        
        layout.addStretch()
        layout.addWidget(title_label)
        layout.addSpacing(20)
        layout.addWidget(subtitle_label)
        layout.addSpacing(50)
        layout.addLayout(buttons_layout)
        layout.addStretch()
        
        self.setLayout(layout)


class TopicSelectionScreen(QWidget):
    def __init__(self, on_topic_selected, on_back):
        super().__init__()
        self.on_topic_selected = on_topic_selected
        self.on_back = on_back
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        title_label = QLabel("SELECT A THEME")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(f"color: {COLORS['secondary']};")
        
        topics_layout = QHBoxLayout()
        topics_layout.setSpacing(20)
        
        history_button = QPushButton("History")
        history_button.setFixedSize(150, 150)
        history_button.setStyleSheet(AppStyles.get_topic_button_style("history"))
        history_button.clicked.connect(lambda: self.on_topic_selected("history"))
        
        geography_button = QPushButton("Geography")
        geography_button.setFixedSize(150, 150)
        geography_button.setStyleSheet(AppStyles.get_topic_button_style("geography"))
        geography_button.clicked.connect(lambda: self.on_topic_selected("geography"))
        
        sports_button = QPushButton("Sports")
        sports_button.setFixedSize(150, 150)
        sports_button.setStyleSheet(AppStyles.get_topic_button_style("sports"))
        sports_button.clicked.connect(lambda: self.on_topic_selected("sports"))
        
        topics_layout.addWidget(history_button)
        topics_layout.addWidget(geography_button)
        topics_layout.addWidget(sports_button)

        back_button = QPushButton("Back")
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #555555;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #777777;
            }
        """)
        back_button.clicked.connect(self.on_back)
        
        layout.addWidget(back_button, 0, Qt.AlignLeft)
        layout.addStretch()
        layout.addWidget(title_label)
        layout.addSpacing(50)
        layout.addLayout(topics_layout)
        layout.addStretch()
        
        self.setLayout(layout)


class DifficultySelectionScreen(QWidget):
    def __init__(self, on_difficulty_selected, topic, on_back):
        super().__init__()
        self.on_difficulty_selected = on_difficulty_selected
        self.topic = topic
        self.on_back = on_back
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        topic_display = {"history": "History", "geography": "Geography", "sports": "Sports"}
        title_label = QLabel(f"SELECT DIFFICULTY - {topic_display.get(self.topic, self.topic).upper()}")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(f"color: {COLORS['secondary']};")
        
        difficulty_layout = QHBoxLayout()
        difficulty_layout.setSpacing(20)
        
        easy_button = QPushButton("Easy")
        easy_button.setFixedSize(150, 150)
        easy_button.setStyleSheet(AppStyles.get_difficulty_button_style("easy"))
        easy_button.clicked.connect(lambda: self.on_difficulty_selected("easy"))
        
        medium_button = QPushButton("Medium")
        medium_button.setFixedSize(150, 150)
        medium_button.setStyleSheet(AppStyles.get_difficulty_button_style("medium"))
        medium_button.clicked.connect(lambda: self.on_difficulty_selected("medium"))
        
        hard_button = QPushButton("Hard")
        hard_button.setFixedSize(150, 150)
        hard_button.setStyleSheet(AppStyles.get_difficulty_button_style("hard"))
        hard_button.clicked.connect(lambda: self.on_difficulty_selected("hard"))
        
        difficulty_layout.addWidget(easy_button)
        difficulty_layout.addWidget(medium_button)
        difficulty_layout.addWidget(hard_button)

        back_button = QPushButton("Back")
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #555555;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #777777;
            }
        """)
        back_button.clicked.connect(self.on_back)
        layout.addWidget(back_button, 0, Qt.AlignLeft)
        layout.addStretch()
        layout.addWidget(title_label)
        layout.addSpacing(50)
        layout.addLayout(difficulty_layout)
        layout.addStretch()
        
        self.setLayout(layout)


class ChallengeQuizScreen(QWidget):
    def __init__(self, on_finish, topic, difficulty, questions):
        super().__init__()
        self.on_finish = on_finish
        self.topic = topic
        self.difficulty = difficulty
        self.questions = questions
        self.current_question_idx = 0
        self.score = 0
        self.option_buttons = []
        self.current_mode = "write"  
        self.init_ui()
        self.load_question()
    
    def init_ui(self):
        main_layout = QVBoxLayout()
        
        header_layout = QHBoxLayout()
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, len(self.questions))
        self.progress_bar.setValue(1)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFormat("%v/%m")
        self.progress_bar.setStyleSheet(f"""
            QProgressBar {{
                border: 2px solid {COLORS["secondary"]};
                border-radius: 5px;
                text-align: center;
                background-color: {COLORS["card"]};
                color: {COLORS["text"]};
                height: 20px;
            }}
            QProgressBar::chunk {{
                background-color: {COLORS[self.topic]};
                width: 10px;
                margin: 0.5px;
            }}
        """)
        
        topic_display = {"history": "History", "geography": "Geography", "sports": "Sports"}
        difficulty_display = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}
        
        topic_label = QLabel(f"{topic_display.get(self.topic, self.topic)} - {difficulty_display.get(self.difficulty, self.difficulty)}")
        topic_label.setFont(QFont("Arial", 16, QFont.Bold))
        topic_label.setStyleSheet(f"color: {COLORS[self.topic]};")
        
        self.progress_label = QLabel(f"Question 1/{len(self.questions)}")
        self.progress_label.setFont(QFont("Arial", 16))
        self.progress_label.setStyleSheet(f"color: {COLORS['text']};")
        self.progress_label.setAlignment(Qt.AlignRight)
        
        self.score_label = QLabel(f"Score: 0")
        self.score_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.score_label.setStyleSheet(f"color: {COLORS['secondary']};")
        
        header_layout.addWidget(topic_label)
        header_layout.addStretch()
        header_layout.addWidget(self.score_label)
        header_layout.addStretch()
        header_layout.addWidget(self.progress_label)
        
        main_layout.addWidget(self.progress_bar)
        main_layout.addSpacing(10)
        main_layout.addLayout(header_layout)
        main_layout.addSpacing(20)
        
        # Carte de question
        question_card = QFrame()
        question_card.setStyleSheet(AppStyles.get_card_style())
        AppStyles.apply_shadow_effect(question_card)
        
        card_layout = QVBoxLayout()
        
        self.question_label = QLabel("")
        self.question_label.setFont(QFont("Arial", 18))
        self.question_label.setWordWrap(True)
        self.question_label.setStyleSheet(f"color: {COLORS['text']};")
        
        card_layout.addWidget(self.question_label)
        card_layout.addSpacing(20)
        
        # Mode d'entrée directe
        self.direct_input_widget = QWidget()
        direct_input_layout = QVBoxLayout()
        
        self.answer_input = QLineEdit()
        self.answer_input.setStyleSheet(AppStyles.get_input_style())
        self.answer_input.setPlaceholderText("Type your answer here...")
        
        self.submit_answer_button = QPushButton("Submit Answer (5 points)")
        self.submit_answer_button.setStyleSheet(AppStyles.get_main_button_style())
        self.submit_answer_button.clicked.connect(self.check_direct_answer)
        
        direct_input_layout.addWidget(self.answer_input)
        direct_input_layout.addWidget(self.submit_answer_button)
        
        self.direct_input_widget.setLayout(direct_input_layout)
        
        # Mode 4 options
        self.four_options_widget = QWidget()
        four_options_layout = QVBoxLayout()
        four_options_layout.setSpacing(10)
        
        for i in range(4):
            button = QPushButton("")
            button.setStyleSheet(AppStyles.get_option_button_style())
            button.clicked.connect(lambda checked, idx=i: self.check_option_answer(idx, 3))
            AppStyles.apply_shadow_effect(button)
            four_options_layout.addWidget(button)
            self.option_buttons.append(button)
        
        self.four_options_widget.setLayout(four_options_layout)
        self.four_options_widget.setVisible(False)
        
        # Mode 2 options
        self.two_options_widget = QWidget()
        two_options_layout = QVBoxLayout()
        two_options_layout.setSpacing(10)
        
        self.two_option_buttons = []
        for i in range(2):
            button = QPushButton("")
            button.setStyleSheet(AppStyles.get_option_button_style())
            button.clicked.connect(lambda checked, idx=i: self.check_option_answer(idx, 1))
            AppStyles.apply_shadow_effect(button)
            two_options_layout.addWidget(button)
            self.two_option_buttons.append(button)
        
        self.two_options_widget.setLayout(two_options_layout)
        self.two_options_widget.setVisible(False)
        
        hint_buttons_layout = QHBoxLayout()
        
        self.four_hints_button = QPushButton("Show 4 Options (3 points)")
        self.four_hints_button.setStyleSheet(AppStyles.get_hint_button_style())
        self.four_hints_button.clicked.connect(self.show_four_options)
        
        self.two_hints_button = QPushButton("Show 2 Options (1 point)")
        self.two_hints_button.setStyleSheet(AppStyles.get_hint_button_style())
        self.two_hints_button.clicked.connect(self.show_two_options)
        
        hint_buttons_layout.addWidget(self.four_hints_button)
        hint_buttons_layout.addWidget(self.two_hints_button)
        
        self.feedback_label = QLabel("")
        self.feedback_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.feedback_label.setAlignment(Qt.AlignCenter)
        self.feedback_label.setWordWrap(True)
        self.feedback_label.setStyleSheet(f"color: {COLORS['text']};")
        self.feedback_label.setVisible(False)
        
        self.next_button = QPushButton("Next Question")
        self.next_button.setStyleSheet(AppStyles.get_main_button_style())
        self.next_button.clicked.connect(self.next_question)
        self.next_button.setVisible(False)
        
        card_layout.addWidget(self.direct_input_widget)
        card_layout.addWidget(self.four_options_widget)
        card_layout.addWidget(self.two_options_widget)
        card_layout.addLayout(hint_buttons_layout)
        card_layout.addSpacing(20)
        card_layout.addWidget(self.feedback_label)
        
        question_card.setLayout(card_layout)
        
        main_layout.addWidget(question_card)
        main_layout.addSpacing(20)
        main_layout.addWidget(self.next_button, 0, Qt.AlignRight)
        
        self.setLayout(main_layout)
    
    def load_question(self):
        question_data = self.questions[self.current_question_idx]
        self.question_label.setText(question_data["question"])
        
        self.current_mode = "write"
        self.direct_input_widget.setVisible(True)
        self.direct_input_widget.setEnabled(True)
        self.four_options_widget.setVisible(False)
        self.two_options_widget.setVisible(False)
        self.four_hints_button.setEnabled(True)
        self.two_hints_button.setEnabled(True)
        self.answer_input.clear()
        self.feedback_label.setVisible(False)
        
        self.correct_answer = question_data["correct_answer"]
        
        options = question_data["options"].copy()
        random.shuffle(options)
        self.four_options = options
        self.correct_four_index = options.index(self.correct_answer)
        
        incorrect_options = [opt for opt in options if opt != self.correct_answer]
        self.two_options = [self.correct_answer, random.choice(incorrect_options)]
        random.shuffle(self.two_options)
        self.correct_two_index = self.two_options.index(self.correct_answer)
        
        for i, option in enumerate(self.four_options):
            self.option_buttons[i].setText(option)
            self.option_buttons[i].setStyleSheet(AppStyles.get_option_button_style())
            self.option_buttons[i].setEnabled(True)
        
        for i, option in enumerate(self.two_options):
            self.two_option_buttons[i].setText(option)
            self.two_option_buttons[i].setStyleSheet(AppStyles.get_option_button_style())
            self.two_option_buttons[i].setEnabled(True)
        
        self.progress_bar.setValue(self.current_question_idx + 1)
        self.progress_label.setText(f"Question {self.current_question_idx + 1}/{len(self.questions)}")
        self.next_button.setVisible(False)
    
    def show_four_options(self):
        self.current_mode = "four_options"
        self.direct_input_widget.setVisible(False)
        self.four_options_widget.setVisible(True)
        self.two_options_widget.setVisible(False)
        self.four_hints_button.setEnabled(False)
        self.two_hints_button.setEnabled(False)
    
    def show_two_options(self):
        self.current_mode = "two_options"
        self.direct_input_widget.setVisible(False)
        self.four_options_widget.setVisible(False)
        self.two_options_widget.setVisible(True)
        self.four_hints_button.setEnabled(False)
        self.two_hints_button.setEnabled(False)
    
    def check_direct_answer(self):
        user_answer = self.answer_input.text().strip().lower()
        correct_answer = self.correct_answer.lower()
        
        is_correct = user_answer == correct_answer
        
        if is_correct:
            self.score += 5
            self.feedback_label.setText(f"Correct! +5 points\nThe answer is: {self.correct_answer}")
            self.feedback_label.setStyleSheet(f"color: {COLORS['correct']};")
        else:
            self.feedback_label.setText(f"Incorrect! The correct answer is: {self.correct_answer}")
            self.feedback_label.setStyleSheet(f"color: {COLORS['incorrect']};")
        
        self.feedback_label.setVisible(True)
        self.direct_input_widget.setEnabled(False)
        self.four_hints_button.setEnabled(False)
        self.two_hints_button.setEnabled(False)
        self.next_button.setVisible(True)
        self.score_label.setText(f"Score: {self.score}")
    
    def check_option_answer(self, selected_idx, points):
        if self.current_mode == "four_options":
            correct_idx = self.correct_four_index
            options = self.option_buttons
        else:  # two_options
            correct_idx = self.correct_two_index
            options = self.two_option_buttons
        
        for button in options:
            button.setEnabled(False)
        
        options[correct_idx].setStyleSheet(AppStyles.get_correct_style())
        
        if selected_idx == correct_idx:
            self.score += points
            self.feedback_label.setText(f"Correct! +{points} points")
            self.feedback_label.setStyleSheet(f"color: {COLORS['correct']};")
        else:
            options[selected_idx].setStyleSheet(AppStyles.get_incorrect_style())
            self.feedback_label.setText(f"Incorrect! No points")
            self.feedback_label.setStyleSheet(f"color: {COLORS['incorrect']};")
        
        self.feedback_label.setVisible(True)
        self.next_button.setVisible(True)
        self.score_label.setText(f"Score: {self.score}")
    
    def next_question(self):
        self.current_question_idx += 1
        
        if self.current_question_idx < len(self.questions):
            self.load_question()
        else:
            self.on_finish(self.score, len(self.questions) * 5)  


class ResultScreen(QWidget):
    def __init__(self, on_restart, score, total):
        super().__init__()
        self.on_restart = on_restart
        self.score = score
        self.total = total
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        results_card = QFrame()
        results_card.setStyleSheet(AppStyles.get_card_style())
        AppStyles.apply_shadow_effect(results_card)
        
        card_layout = QVBoxLayout()
        
        title_label = QLabel("QUIZ FINISHED!")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(f"color: {COLORS['secondary']};")
        
        score_label = QLabel(f"Your Score: {self.score}/{self.total}")
        score_label.setFont(QFont("Arial", 36, QFont.Bold))
        score_label.setAlignment(Qt.AlignCenter)
        score_label.setStyleSheet(f"color: {COLORS['text']};")
        
        percentage = (self.score / self.total) * 100
        percentage_label = QLabel(f"{percentage:.1f}%")
        percentage_label.setFont(QFont("Arial", 24))
        percentage_label.setAlignment(Qt.AlignCenter)
        
        if percentage >= 80:
            percentage_label.setStyleSheet(f"color: {COLORS['correct']};")
            message = "Excellent! You're a quiz master!"
        elif percentage >= 60:
            percentage_label.setStyleSheet(f"color: {COLORS['easy']};")
            message = "Good work! Keep learning!"
        else:
            percentage_label.setStyleSheet(f"color: {COLORS['incorrect']};")
            message = "Keep practicing! You'll get better!"
        
        message_label = QLabel(message)
        message_label.setFont(QFont("Arial", 16))
        message_label.setAlignment(Qt.AlignCenter)
        message_label.setStyleSheet(f"color: {COLORS['text']};")
        
        card_layout.addWidget(title_label)
        card_layout.addSpacing(20)
        card_layout.addWidget(score_label)
        card_layout.addWidget(percentage_label)
        card_layout.addSpacing(20)
        card_layout.addWidget(message_label)
        
        results_card.setLayout(card_layout)
        
        play_again_button = QPushButton("Play again")
        play_again_button.setStyleSheet(AppStyles.get_main_button_style())
        play_again_button.clicked.connect(self.on_restart)
        
        layout.addStretch()
        layout.addWidget(results_card)
        layout.addSpacing(30)
        layout.addWidget(play_again_button, 0, Qt.AlignCenter)
        layout.addStretch()
        
        self.setLayout(layout)


class ChallengeQuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.quiz_data = self.load_quiz_data()
        self.init_ui()
        self.show_topic_selection()

    
    def show_welcome_screen(self):
        self.stacked_widget.setCurrentWidget(self.welcome_screen)

    def load_quiz_data(self):
        try:
            file_path = 'src/quiz_data.json'  
            
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
                
        except FileNotFoundError:
            print(f"Error: File {file_path} not found")
            print(f"Current directory: {os.getcwd()}")
            print(f"Directory contents: {os.listdir('.')}")
            
            alternative_paths = ['quiz_data.json', './quiz_data.json', '../quiz_data.json']
            
            for alt_path in alternative_paths:
                try:
                    print(f"Trying alternative path: {alt_path}")
                    with open(alt_path, 'r', encoding='utf-8') as f:
                        return json.load(f)
                except FileNotFoundError:
                    continue
                except json.JSONDecodeError:
                    continue
            
            print("Unable to find a valid quiz_data.json file.")
            
        except json.JSONDecodeError as e:
            print(f"Error: The file {file_path} is not a valid JSON: {str(e)}")
            
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
        
        return {
            "history": {"easy": [], "medium": [], "hard": []},
            "geography": {"easy": [], "medium": [], "hard": []},
            "sports": {"easy": [], "medium": [], "hard": []}
        }
    
    def init_ui(self):
        self.setWindowTitle('Challenge Quiz')
        self.setGeometry(100, 100, 800, 600)
        
        self.setStyleSheet(f"background-color: {COLORS['background']};")
        
        self.stacked_widget = QStackedWidget()
        
        self.welcome_screen = WelcomeScreen(
            lambda: self.redirect_to_classic_mode(),
            self.show_topic_selection
        )
        
        self.topic_selection_screen = TopicSelectionScreen(
            self.on_topic_selected,
            self.show_welcome_screen  
        )        
        self.stacked_widget.addWidget(self.welcome_screen)
        self.stacked_widget.addWidget(self.topic_selection_screen)
        
        self.setCentralWidget(self.stacked_widget)
    
    def redirect_to_classic_mode(self):
        print("Switching to classic mode")
        pass
    
    def show_topic_selection(self):
        self.stacked_widget.setCurrentWidget(self.topic_selection_screen)
    
    def on_topic_selected(self, topic):
        self.difficulty_selection_screen = DifficultySelectionScreen(
            lambda difficulty: self.on_difficulty_selected(topic, difficulty),
            topic,
            self.show_topic_selection
        )
        
        self.stacked_widget.addWidget(self.difficulty_selection_screen)
        self.stacked_widget.setCurrentWidget(self.difficulty_selection_screen)
    
    def on_difficulty_selected(self, topic, difficulty):
        available_questions = self.quiz_data.get(topic, {}).get(difficulty, [])
        
        if not available_questions:
            print(f"No questions available for {topic} - {difficulty}")
            self.show_topic_selection()
            return
        
        num_questions = min(len(available_questions), 10)
        selected_questions = random.sample(available_questions, num_questions)
        
        self.quiz_screen = ChallengeQuizScreen(
            self.show_results,
            topic,
            difficulty,
            selected_questions
        )
        
        self.stacked_widget.addWidget(self.quiz_screen)
        self.stacked_widget.setCurrentWidget(self.quiz_screen)
    
    def show_results(self, score, total):
        self.result_screen = ResultScreen(
            self.restart_quiz,
            score,
            total
        )
        
        self.stacked_widget.addWidget(self.result_screen)
        self.stacked_widget.setCurrentWidget(self.result_screen)
    
    def restart_quiz(self):
        self.stacked_widget.setCurrentWidget(self.topic_selection_screen)