# This script is for unit testing our databases.

# Imports --------------------------------------------------------------------------------

from tests.testing_tools.add_users_to_database import add_new_psychiatrist, add_new_patient

from tests.functional_test_framework import LiveServerTestCase

import unittest


# Test Patient Database -----------------------------------------------------------------


class UnitTestPatientDatabase(LiveServerTestCase):

    def test_add_patient_without_psychiatrist(self):
        add_new_patient()








# Test Psychiatrist Database ------------------------------------------------------------

# Test Patient Mood Database ------------------------------------------------------------
