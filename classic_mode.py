import json
import random
import os 
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QStackedWidget)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QProgressBar

from challenge_mode import COLORS, AppStyles

class WelcomeScreen(QWidget):
    def __init__(self, on_classic_mode, on_challenge_mode):
        super().__init__()
        self.on_classic_mode = on_classic_mode
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
        
        classic_button = QPushButton("CLASSIC MODE")
        classic_button.setFixedSize(200, 60)
        classic_button.setStyleSheet(AppStyles.get_main_button_style())
        classic_button.clicked.connect(self.on_classic_mode)
        
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
        
        buttons_layout.addWidget(classic_button)
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
        self.on_back= on_back
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


class QuizScreen(QWidget):
    def __init__(self, on_finish, topic, difficulty, questions):
        super().__init__()
        self.on_finish = on_finish
        self.topic = topic
        self.difficulty = difficulty
        self.questions = questions
        self.current_question_idx = 0
        self.score = 0
        self.option_buttons = []
        self.setFocusPolicy(Qt.StrongFocus)
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
        
        header_layout.addWidget(topic_label)
        header_layout.addWidget(self.progress_label)
        main_layout.addWidget(self.progress_bar)
        main_layout.addSpacing(10)

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
        
        options_layout = QVBoxLayout()
        options_layout.setSpacing(10)
        
        for i in range(4):
            button = QPushButton("")
            button.setStyleSheet(AppStyles.get_option_button_style())
            button.clicked.connect(lambda checked, idx=i: self.check_answer(idx))
            AppStyles.apply_shadow_effect(button)
            options_layout.addWidget(button)
            self.option_buttons.append(button)
        
        card_layout.addLayout(options_layout)
        question_card.setLayout(card_layout)
        
        self.next_button = QPushButton("Next Question")
        self.next_button.setStyleSheet(AppStyles.get_main_button_style())
        self.next_button.clicked.connect(self.next_question)
        self.next_button.setVisible(False)
        
        main_layout.addLayout(header_layout)
        main_layout.addSpacing(20)
        main_layout.addWidget(question_card)
        main_layout.addSpacing(20)
        main_layout.addWidget(self.next_button, 0, Qt.AlignRight)
        
        self.setLayout(main_layout)
    
    def load_question(self):
        question_data = self.questions[self.current_question_idx]
        self.question_label.setText(question_data["question"])
        
        options = question_data["options"].copy()
        random.shuffle(options)
        
        self.correct_option_index = options.index(question_data["correct_answer"])
        
        for i, option in enumerate(options):
            self.option_buttons[i].setText(option)
            self.option_buttons[i].setStyleSheet(AppStyles.get_option_button_style())
            self.option_buttons[i].setEnabled(True)
        
        self.progress_bar.setValue(self.current_question_idx + 1)
        self.progress_label.setText(f"Question {self.current_question_idx + 1}/{len(self.questions)}")
        self.next_button.setVisible(False)
    
    def check_answer(self, selected_idx):
        for button in self.option_buttons:
            button.setEnabled(False)
        
        self.option_buttons[self.correct_option_index].setStyleSheet(AppStyles.get_correct_style())
        
        if selected_idx == self.correct_option_index:
            self.score += 1
        else:
            self.option_buttons[selected_idx].setStyleSheet(AppStyles.get_incorrect_style())
        
        self.next_button.setVisible(True)
    
    def next_question(self):
        self.current_question_idx += 1
        
        if self.current_question_idx < len(self.questions):
            self.load_question()
        else:
            self.on_finish(self.score, len(self.questions))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if self.next_button.isVisible():
                self.next_question()


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


class QuizApp(QMainWindow):
    def __init__(self, on_switch_to_challenge=None):
        super().__init__()
        self.on_switch_to_challenge = on_switch_to_challenge
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
        self.setWindowTitle('General Culture Quiz')
        self.setGeometry(100, 100, 800, 600)
        
        self.setStyleSheet(f"background-color: {COLORS['background']};")
        
        self.stacked_widget = QStackedWidget()
        
        if self.on_switch_to_challenge:
            self.welcome_screen = WelcomeScreen(
                self.show_topic_selection,
                self.on_switch_to_challenge
            )
        else:
            from challenge_mode import WelcomeScreen as OldWelcomeScreen
            self.welcome_screen = OldWelcomeScreen(self.show_topic_selection)
        
        self.topic_selection_screen = TopicSelectionScreen(
            self.on_topic_selected,
            self.show_welcome_screen
        )
        
        self.stacked_widget.addWidget(self.welcome_screen)
        self.stacked_widget.addWidget(self.topic_selection_screen)
        
        self.setCentralWidget(self.stacked_widget)

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
        
        self.quiz_screen = QuizScreen(
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