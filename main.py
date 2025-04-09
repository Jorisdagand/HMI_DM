import sys
from PyQt5.QtWidgets import QApplication
from classic_mode import QuizApp  
from challenge_mode import ChallengeQuizApp  

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.start_challenge_mode()
    
    def start_challenge_mode(self):
        self.challenge_app = ChallengeQuizApp()
        self.challenge_app.redirect_to_classic_mode = self.switch_to_classic_mode
        self.challenge_app.show()
    
    def start_classic_mode(self):
        self.classic_app = QuizApp(on_switch_to_challenge=self.switch_to_challenge_mode)
        self.classic_app.show_topic_selection()
        self.classic_app.show()
    
    def switch_to_classic_mode(self):
        self.challenge_app.close()
        self.challenge_app = None
        self.start_classic_mode()
    
    def switch_to_challenge_mode(self):
        self.classic_app.close()
        self.classic_app = None
        self.start_challenge_mode()
    
    def run(self):
        return self.app.exec_()

def main():
    main_app = MainApp()
    sys.exit(main_app.run())

if __name__ == '__main__':
    main()