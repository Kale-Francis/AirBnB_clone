#!/usr/bin/python3
"""
Unit tests for the Console class
"""

from models.state import State
import unittest
from io import StringIO
import sys
from console import Console

class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up the console for testing"""
        self.console = Console()
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        """Restore original stdout"""
        sys.stdout = self.saved_stdout

    def test_create_state(self):
        """Test create command for State"""
        self.console.create('State', 'California')
        output = sys.stdout.getvalue().strip()
        self.assertIn('Created:', output)

    def test_show_state(self):
        """Test show command for State"""
        state = State(name='California')
        state.save()
        self.console.show('State', state.id)
        output = sys.stdout.getvalue().strip()
        self.assertIn('California', output)

    def test_destroy_state(self):
        """Test destroy command for State"""
        state = State(name='California')
        state.save()
        self.console.destroy('State', state.id)
        output = sys.stdout.getvalue().strip()
        self.assertIn(f"Destroyed: {state.id}", output)

    def test_update_state(self):
        """Test update command for State"""
        state = State(name='California')
        state.save()
        self.console.update('State', state.id, 'name', 'Nevada')
        output = sys.stdout.getvalue().strip()
        self.assertIn('Updated:', output)

    def test_all_states(self):
        """Test all command for listing States"""
        self.console.all('State')
        output = sys.stdout.getvalue().strip()
        self.assertIn('State', output)

if __name__ == "__main__":
    unittest.main()
