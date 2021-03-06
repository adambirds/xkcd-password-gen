import unittest

from src.xkcd_pass import xkcd_pass

WORDFILE = "src/xkcd_pass/static/eff-long"


class TestGenerateWordlist(unittest.TestCase):
    """
    Test cases for function `generate_wordlist`.
    """

    def shortDescription(self) -> None:
        return None

    def setUp(self) -> None:
        """
        Set up fixtures for this test case.
        """
        self.wordlist_full = xkcd_pass.generate_wordlist(
            wordfile=WORDFILE,
            min_length=5,
            max_length=8,
        )
        self.wordlist_small = xkcd_pass.generate_wordlist(
            wordfile="src/xkcd_pass/static/test_list", valid_chars="[a-z]"
        )

    def test_loadwordfile(self) -> None:
        """
        Test load wordlist is correct.
        """
        self.assertEqual(len(self.wordlist_full), 5670)

    def test_regex(self) -> None:
        """
        Test regex.
        """
        self.assertNotIn("__$$$__", self.wordlist_small)


if __name__ == "__main__":
    test_cases = [
        TestGenerateWordlist,
    ]
    suites = [unittest.TestLoader().loadTestsFromTestCase(test_case) for test_case in test_cases]
    unittest.TextTestRunner(verbosity=2, buffer=True).run(unittest.TestSuite(suites))
