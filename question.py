def CheckPosition(x, y):
    for i in range(4):
        if 50 < x < 500 and 400 + 70 * i < y < 470 + 70 * i:
            return i + 1
    return False


class Question:

    def __init__(self, image, right_answer, answers, cost):
        self.image = image
        self.right_answer = right_answer
        self.answers = answers
        self.cost = cost

    def CheckAnswer(self, answer):
        return answer == self.right_answer
