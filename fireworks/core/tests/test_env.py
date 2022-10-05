import os
import unittest

from fireworks import FWorker, LaunchPad

class FWorkerTest(unittest.TestCase):

    def test_settings_from_env(self):
        os.environ['FWORKER_NAME'] = 'from_env'

        fw = FWorker()
        self.assertEqual(fw.name, 'from_env')

class LauchPadTest(unittest.TestCase):

    def test_settings_from_env(self):
        os.environ['LAUNCHPAD_HOST'] = 'not-localhost'

        lp = LaunchPad()
        self.assertEqual(lp.host, 'not-localhost')

