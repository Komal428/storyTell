
# Test

import unittest
import message

class TestMessage(unittest.TestCase):

    def test_upper(self):
        messageId = message.create_message('HelloWorld')

        id = str(messageId.rsplit('/')[-1])

        expectedMessage = 'HelloWorld'

        actualMessage = message.read_item(id)

        self.assertEqual(actualMessage,expectedMessage)


if __name__ == '__main__':
    unittest.main()
