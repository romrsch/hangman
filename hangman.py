# Game status categories
# Change the values as you see fit
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
            raise ValueError("Вы исчерпали все попытки!")
        elif self.status == STATUS_WIN:
            raise ValueError("Вы угадали!")
        if char in self._word:
            if char in self._guesses:
                # no repeats; counts as a move
                self.remaining_guesses -= 1
            else:
                self._guesses.append(char)
        else:
            # a miss

            self.remaining_guesses -= 1
            self._guesses.append(char)            
        # test for winning or losing
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE

        # unless they just guessed right...
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
