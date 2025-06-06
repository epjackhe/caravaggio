import os
import runpy
import sys
from unittest.mock import Mock

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import ticket_monitor


def fake_response(text):
    response = Mock()
    response.text = text
    response.raise_for_status = Mock()
    return response


def test_sold_out_message(monkeypatch, capsys):
    monkeypatch.setattr('requests.get', lambda *args, **kwargs: fake_response('tickets SOLD OUT here'))
    runpy.run_module('ticket_monitor', run_name='__main__')
    captured = capsys.readouterr()
    assert 'Tickets not available yet.' in captured.out


def test_tickets_available_message(monkeypatch, capsys):
    html = '<html><body>tickets are open now</body></html>'
    monkeypatch.setattr('requests.get', lambda *args, **kwargs: fake_response(html))
    runpy.run_module('ticket_monitor', run_name='__main__')
    captured = capsys.readouterr()
    assert 'Tickets might be available!' in captured.out
