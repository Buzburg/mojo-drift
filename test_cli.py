import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

class CLITests(unittest.TestCase):
    def test_step_without_session_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p = subprocess.run([sys.executable, str(Path(__file__).with_name('drift.py').resolve()), 'step', '--action', 'test'], cwd=d, capture_output=True)
            self.assertNotEqual(p.returncode, 0)
