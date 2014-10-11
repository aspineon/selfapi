import os
import selfapi
import unittest
import tempfile

class DietEndpointTest(unittest.TestCase):

    def setUp(self):
        self.db_fd, selfapi.db = tempfile.mkstemp()
        selfapi.app.config['TESTING'] = True
        self.app = selfapi.app.test_client()


    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(selfapi.db)

if __name__ == '__main__':
    unittest.main()
