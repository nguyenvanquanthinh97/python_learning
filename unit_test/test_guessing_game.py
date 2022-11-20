import unittest
import guessing_game


class TestGame(unittest.TestCase):
    def test_guess_correctly(self):
        guess = answer = 10
        result = guessing_game.check_correct_guessing(guess, answer)
        self.assertEqual(result, 'you are a genius!')

    def test_guess_wrongly(self):
        guess = 1
        answer = 10
        result = guessing_game.check_correct_guessing(guess, answer)
        self.assertFalse(result)

    def test_guess_is_not_number(self):
        guess = 'dfasjlfkdsa'
        answer = 10
        result = guessing_game.check_correct_guessing(guess, answer)
        self.assertEqual(result, 'please enter a number')

    def test_guess_and_answer_is_not_number(self):
        guess = answer = 'hie'
        result = guessing_game.check_correct_guessing(guess, answer)
        self.assertEqual(result, 'please enter a number')


if __name__ == '__main__':
    unittest.main()
