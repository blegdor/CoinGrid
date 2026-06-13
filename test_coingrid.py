# test_coingrid.py
"""
Tests for CoinGrid module.
"""

import unittest
from coingrid import CoinGrid

class TestCoinGrid(unittest.TestCase):
    """Test cases for CoinGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinGrid()
        self.assertIsInstance(instance, CoinGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
