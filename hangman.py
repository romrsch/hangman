# Категории статуса игры: победа, поражение, продолжение игры

STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self._word = word
        self._guesses = []
    def guess(self, char):
        if self.status == STATUS_LOSE:
            raise ValueError("Не правильно!")
        elif self.status == STATUS_WIN:
            raise ValueError("Правильно!")
        if char in self._word:
            if char in self._guesses:
                # без повторов; засчитывается как ход
                self.remaining_guesses -= 1
            else:
                self._guesses.append(char)
        else:
            # промах

            self.remaining_guesses -= 1
            self._guesses.append(char)            
        # проверка: победа или поражение
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE

        # если только не угадали правильно...
        if all([l in self._guesses for l in self._word]):
            self.status = STATUS_WIN
    def get_masked_word(self):
        m = ["_"] * len(self._word)
        for l in self._guesses:
            for i, letter in enumerate(self._word):
                if letter == l:
                    m[i] = l
        return ''.join(m)
        
    def get_status(self):
        return self.status
