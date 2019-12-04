Qt Crash Friendly Test
======================

Highlights:
* Minimal example, using a patched [`qtcrash`](https://pypi.org/project/qcrash/).
* Motive: posting new GitHub gists needs authentication.
* If posting fails, IOW, if posting generates an internal excepetion no feedback is given. In my tests, HTTPS certificate validation was failing.

Alternatives:
* Maybe this simpler approach could be used instead?
  http://timlehr.com/python-exception-hooks-with-qt-message-box/
