import sys
import marsrover


def test_ping():
    sys.argv = ['foo', '10']
    marsrover.ping()

