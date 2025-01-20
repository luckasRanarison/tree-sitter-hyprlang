from unittest import TestCase

import tree_sitter, tree_sitter_hyprlang


class TestLanguage(TestCase):
    def test_can_load_grammar(self):
        try:
            tree_sitter.Language(tree_sitter_hyprlang.language())
        except Exception:
            self.fail("Error loading Hyprlang grammar")
