
import unittest
import mock
try:
    import __builtin__ as builtins
except ImportError:
    import builtins

from xcrawler.files.openers.write_opener import WriteOpener


class TestWriteOpener(unittest.TestCase):

    def setUp(self):
        self.file_opener_write = WriteOpener()

    @mock.patch('xcrawler.tests.files.test_write_opener.builtins.open')
    def test_open_file_write_byte_strings(self, mock_open_function):
        mock_filename = "file.csv"
        mock_file = mock.Mock()
        mock_open_function.return_value = mock_file
        result = self.file_opener_write.open_file_write_byte_strings(mock_filename)
        self.assertEquals(result, mock_file)

    @mock.patch('xcrawler.tests.files.test_write_opener.builtins.open')
    def test_open_file_write_unicode_strings(self, mock_open_function):
        mock_filename = "file.csv"
        mock_file = mock.Mock()
        mock_open_function.return_value = mock_file
        result = self.file_opener_write.open_file_write_unicode_strings(mock_filename)
        self.assertEquals(result, mock_file)
