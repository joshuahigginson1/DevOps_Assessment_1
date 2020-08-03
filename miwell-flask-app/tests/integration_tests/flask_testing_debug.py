from flask import Flask
from flask_testing import LiveServerTestCase

import config
import urllib3
import unittest
import wsgi
from flaskr import db, login_manager, argon2


class MyTest(LiveServerTestCase):

    def create_app(self):

    return app

    def test_server_is_up_and_running(self):
        response = urllib3.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)