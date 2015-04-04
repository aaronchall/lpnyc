import os
import sys
import unittest
import subprocess
import shlex


def main():
    print('running unittests for {0}'.format(sys.version))
    test_loader = unittest.TestLoader()
    loaded_test_suite = test_loader.discover(
      'tests/unittests', pattern='*.py', top_level_dir=os.getcwd())
    text_test_runner = unittest.TextTestRunner()
    text_test_runner.run(loaded_test_suite)
    if sys.version_info[0] < 3:
        ps = subprocess.Popen(shlex.split('python3 runtests.py'))
        # print(ps.communicate())
        ps.communicate()
    # could do same for 3 (run 2), but probably not desired

if __name__ == '__main__':
    main()
