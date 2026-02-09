"""
Scrivi una funzione che fornisca in output il nome del Sistema Operativo utilizzato con eventuali relative informazioni sulla release corrente.
Suggerimento: per risolvere questo esercizio potreste dover utilizzare una libreria! ;)
"""
import unittest
from unittest.mock import patch
from systemInf import system_information

"""
test_GIVEN_os_information_available_WHEN_requested_THEN_return_structured_data
test_GIVEN_mocked_os_name_WHEN_function_called_THEN_return_that_os_name
test_GIVEN_mocked_os_release_WHEN_function_called_THEN_return_that_release
test_GIVEN_unknown_or_partial_os_info_WHEN_function_called_THEN_handle_gracefully
"""

class TestSystemInformation(unittest.TestCase):

    def test_GIVEN_os_information_available_WHEN_requested_THEN_return_structured_data(self):
        #arrange
        #act
        os_information = system_information()
        #assert
        self.assertEqual(type(os_information), dict)
        self.assertIn('system', os_information)
        self.assertIn('machine', os_information)

    @patch("systemInf.platform.system")
    def test_GIVEN_mocked_os_release_WHEN_function_called_THEN_return_that_release(self, mocked_system):
        # Arrange
        mocked_system.return_value = "Windows"

        # Act
        result = system_information()

        # Assert
        self.assertEqual(result["system"], "Windows")


    @patch("systemInf.platform.machine")
    def test_GIVEN_mocked_machine_WHEN_function_called_THEN_return_that_machine(self, mocked_machine):
        # Arrange
        mocked_machine.return_value = "test"

        # Act
        result = system_information()

        # Assert
        self.assertEqual(result["machine"], "test")

    @patch("systemInf.platform.system")
    @patch("systemInf.platform.processor")
    def test_GIVEN_unknown_or_partial_os_info_WHEN_function_called_THEN_handle_gracefully(self, mocked_processor, mocked_system):
        # Arrange
        mocked_system.return_value = "Linux"
        mocked_processor.return_value = None  # simuliamo informazione mancante

        # Act
        result = system_information()

        # Assert
        self.assertEqual(result["system"], "Linux")
        self.assertEqual(result["processor"], None)
