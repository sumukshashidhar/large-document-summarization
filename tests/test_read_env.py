import os
import unittest

from src.utils.read_env import read_env

class TestReadEnv(unittest.TestCase):
    def test_read_env(self):
        # create a temporary .env file with test values
        with open('.env', 'w') as f:
            f.write('OPENAI_API_KEY=abc123\nMAX_TOKENS=5000')

        # call the read_env function and check the return values
        values = read_env('.env')
        self.assertEqual(type(values['MAX_TOKENS']), int)
        self.assertEqual(values['MAX_TOKENS'], 5000)
        self.assertEqual(type(values['OPENAI_API_KEY']), str)
        self.assertEqual(values['OPENAI_API_KEY'], 'abc123')

        # delete the temporary .env file
        os.remove('.env')

if __name__ == '__main__':
    unittest.main()
