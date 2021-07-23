import sys
import marsrover


def test_ping_ok():
    sys.argv = ['foo', 'kr']
    msg = marsrover.ping()
    assert isinstance(msg, str)

    sys.argv = ['foo', 'en']
    msg = marsrover.ping()

    assert isinstance(msg, str)


def test_ping_jp():
    sys.argv = ['foo', 'jp']
    msg = marsrover.ping()

    assert isinstance(msg, str)


def test_ping_none():
    sys.argv = ['foo']
    msg = marsrover.ping()

    assert isinstance(msg, str)


def test_what_about_there():
    msg = marsrover.what_about_there(language='kr', question='お元気ですか')
    assert isinstance(msg, str)
    print(msg)

