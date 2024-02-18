# truthTable.py
from tkinter import *


class TruthTable:
    def __init__(self):
        self.window = Tk()
        self.window.title("Truth Table")

        self.entries = []
        self.correct_answers = {
            'AND': [0, 0, 0, 1],
            'OR': [0, 1, 1, 1],
            'XOR': [0, 1, 1, 0],
            'NOT': [1, 0]
        }

        row = 0
        for gate, answers in self.correct_answers.items():
            Label(self.window, text=gate).grid(row=row, column=0, columnspan=2)
            row += 1
            for i in range(len(answers)):
                if gate == 'NOT':
                    Label(self.window, text=f"NOT {'True' if i else 'False'}").grid(
                        row=row, column=0)
                else:
                    Label(
                        self.window, text=f"{'True' if i//2 else 'False'} {gate} {'True' if i%2 else 'False'}").grid(row=row, column=0)
                entry = Entry(self.window)
                entry.grid(row=row, column=1)
                self.entries.append(entry)
                row += 1

        Button(self.window, text="Submit", command=self.calculate_score).grid(
            row=row, column=0, columnspan=2)

    def calculate_score(self):
        score = 0
        for entry, correct_answer in zip(self.entries, [answer for answers in self.correct_answers.values() for answer in answers]):
            try:
                if int(entry.get()) == correct_answer:
                    score += 1
            except ValueError:
                pass
        Label(self.window, text=f"Score: {score / len(self.entries) * 100}%").grid(
            row=len(self.entries) + len(self.correct_answers) + 1, column=0, columnspan=2)

    def run(self):
        self.window.mainloop()


truthTable = TruthTable()
truthTable.run()
