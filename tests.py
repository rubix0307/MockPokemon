# tests.py
import os.path
import unittest
from unittest.mock import patch
from main import main

class MockPokemonService:
    def get_pokemon_info(self, pokemon_name):
        return {
            'abilities': [{'ability':{'name': 'mock_name'}}],
            'height': 'mock_height',
            'weight': 'mock_weight',
        }

class MockPokemonNameTranslator:
    def __init__(self):
        self.client = ''

    def translate(self, text, target_language="en"):
        return text


class TestMainApp(unittest.TestCase):

    @patch('main.PokemonService', MockPokemonService)
    @patch('main.PokemonNameTranslator', MockPokemonNameTranslator)
    def test_main(self):
        main()

        template = open('report_template.html', 'r').read()

        name_exists = 'mock_name' in template
        height_exists = 'mock_height' in template
        weight_exists = 'mock_weight' in template

        self.assertTrue(name_exists)
        self.assertTrue(height_exists)
        self.assertTrue(weight_exists)
