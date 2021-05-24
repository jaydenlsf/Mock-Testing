from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_football(self):
        with patch("requests.get") as f:
            f.return_value.text = "1"

            response = self.client.get(url_for("sport"))
            self.assertIn(b"Football", response.data)

    def test_badminton(self):
        with patch("requests.get") as b:
            b.return_value.text = "2"

            response = self.client.get(url_for("sport"))
            self.assertIn(b"Badminton", response.data)

    def test_hockey(self):
        with patch("requests.get") as h:
            h.return_value.text = "3"

            response = self.client.get(url_for("sport"))
            self.assertIn(b"Hockey", response.data)

    def test_boxing(self):
        with patch("requests.get") as box:
            box.return_value.text = ""

            response = self.client.get(url_for("sport"))
            self.assertIn(b"Boxing", response.data)
