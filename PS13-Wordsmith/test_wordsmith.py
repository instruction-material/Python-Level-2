import importlib.util
from pathlib import Path
import random
import sys
import time
import unittest

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("wordsmith", ROOT / "solution" / "main.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


class WordsmithChecks(unittest.TestCase):
    letters = set("aceinrt")
    words = {"cat", "crate", "trace", "rain", "tat"}

    def trace(self, values, moments=None, duration=60):
        now = [0.0]
        values = iter(values)
        moments = iter(moments or [1] * 100)
        output = []

        def read(_prompt):
            item = next(values)
            now[0] = next(moments)
            if item is None:
                raise EOFError
            return item

        result = game.play_round(self.words, self.letters, duration,
                                 read=read, write=output.append, clock=lambda: now[0])
        return result, output

    def test_scoring_and_duplicates(self):
        result, _ = self.trace(["cat", "cat", "crate", ":quit"])
        self.assertEqual(result, {"score": 8, "words": ["cat", "crate"], "reason": "quit"})

    def test_normalization(self):
        result, _ = self.trace([" CAT ", " CrAtE ", ":quit"])
        self.assertEqual(result["score"], 8)

    def test_invalid_and_empty(self):
        result, _ = self.trace(["banana", "notaword", "", ":quit"])
        self.assertEqual(result["score"], 0)

    def test_letter_reuse(self):
        result, _ = self.trace(["tat", ":quit"])
        self.assertEqual(result["score"], 3)

    def test_eof_keeps_previous_score(self):
        result, _ = self.trace(["cat", None])
        self.assertEqual(result["score"], 3)
        self.assertEqual(result["reason"], "input ended")

    def test_exact_deadline_discards_submission(self):
        for moment in [60, 61]:
            with self.subTest(moment=moment):
                result, out = self.trace(["cat"], [moment])
                self.assertEqual(result["score"], 0)
                self.assertEqual(result["reason"], "time")
                self.assertIn("Time is up.", out)

    def test_before_deadline_scores_and_later_answer_does_not(self):
        result, _ = self.trace(["crate", "trace"], [59.9, 60])
        self.assertEqual(result["score"], 5)
        self.assertEqual(result["words"], ["crate"])

    def test_expired_before_prompt_never_reads(self):
        moments = iter([0, 60])
        result = game.play_round(self.words, self.letters, read=lambda _: self.fail("extra prompt"),
                                 write=lambda _: None, clock=lambda: next(moments))
        self.assertEqual(result["score"], 0)

    def test_real_monotonic_deadline(self):
        def slow_read(_prompt):
            time.sleep(0.1)
            return "cat"
        result = game.play_round(self.words, self.letters, duration=0.05,
                                 read=slow_read, write=lambda _: None)
        self.assertEqual(result["reason"], "time")
        self.assertEqual(result["score"], 0)

    def test_normal_scoring_hook_is_used(self):
        original = game.word_score
        game.word_score = lambda word: len(word) * 2
        try:
            result, _ = self.trace(["cat", ":quit"])
            self.assertEqual(result["score"], 6)
        finally:
            game.word_score = original

    def test_dictionary_and_letter_generation(self):
        words = game.load_words(ROOT / "solution" / "valid_words.txt")
        self.assertGreater(len(words), 70000)
        self.assertIn("cat", words)
        self.assertIn("crate", words)
        for seed in range(100):
            letters = game.choose_letters(random.Random(seed))
            self.assertEqual(len(letters), 7)
            self.assertTrue(all("a" <= letter <= "z" for letter in letters))

    def test_invalid_durations(self):
        for duration in [0, -1, float("nan"), float("inf")]:
            with self.subTest(duration=duration):
                with self.assertRaises(ValueError):
                    game.play_round(self.words, self.letters, duration=duration)


if __name__ == "__main__":
    unittest.main(testRunner=unittest.TextTestRunner(stream=sys.stdout, verbosity=2))
