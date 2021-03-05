from snake.utils.check import verify, not_null, some, every, build_check, SOME_TYPE, items

import unittest


class CheckTest(unittest.TestCase):

    def test_verify(self):
        self.assertEqual(verify("", [not_null]).status, False)
        self.assertEqual(verify("", [not_null("null")]).status, False)
        self.assertEqual(verify("", not_null("null")).status, False)
        self.assertEqual(verify("", not_null).status, False)

        self.assertEqual(verify("val", [not_null]).status, True)
        self.assertEqual(verify("val", [not_null("null")]).status, True)
        self.assertEqual(verify("val", not_null("null")).status, True)
        self.assertEqual(verify("val", not_null).status, True)

    def test_some(self):
        self.assertEqual(some({"a": None}, {"a": [not_null]}).status, False)
        self.assertEqual(some({"a": None}, {"a": not_null}).status, False)
        self.assertEqual(some({"a": None}, {"a": not_null("null")}).status, False)
        self.assertEqual(some({"a": None}, {"a": [not_null("null")]}).status, False)

        self.assertEqual(some({"a": "val"}, {"a": [not_null]}).status, True)
        self.assertEqual(some({"a": "val"}, {"a": not_null}).status, True)
        self.assertEqual(some({"a": "val"}, {"a": not_null("null")}).status, True)
        self.assertEqual(some({"a": "val"}, {"a": [not_null("null")]}).status, True)

        self.assertEqual(some({"a": {"c": None}}, {"a": items({"c": [not_null]})}).status, False)
        self.assertEqual(some({"a": {"c": "val"}}, {"a": items({"c": [not_null]})}).status, True)

    def test_every(self):
        self.assertEqual(every({"a": None}, {"a": [not_null]}).status, False)
        self.assertEqual(every({"a": None}, {"a": not_null}).status, False)
        self.assertEqual(every({"a": None}, {"a": not_null("null")}).status, False)
        self.assertEqual(every({"a": None}, {"a": [not_null("null")]}).status, False)

        self.assertEqual(every({"a": "val"}, {"a": [not_null]}).status, True)
        self.assertEqual(every({"a": "val"}, {"a": not_null}).status, True)
        self.assertEqual(every({"a": "val"}, {"a": not_null("null")}).status, True)
        self.assertEqual(every({"a": "val"}, {"a": [not_null("null")]}).status, True)

        self.assertEqual(every({"a": {"c": None}}, {"a": items({"c": [not_null]})}).status, False)
        self.assertEqual(every({"a": {"c": "val"}}, {"a": items({"c": [not_null]})}).status, True)

    def test_build_check(self):
        some_item_check = build_check(SOME_TYPE, {"a": items({"c": [not_null]})})

        self.assertEqual(some_item_check({"a": {"c": None}}).status, False)
        self.assertEqual(some_item_check({"a": {"c": "val"}}).status, True)


if __name__ == '__main__':
    unittest.main()
