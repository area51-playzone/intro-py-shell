from unittest import TestCase
import subprocess

class convertTest(TestCase):

    def convert_one_hundred(self):
        command = "convert_num 100"
        output = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (out, err) = output.communicate()
        self.assertEqual(out,'one hundred\n')
