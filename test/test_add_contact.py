# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):

    app.session.open_start_page()
    app.session.login( username="admin", password="secret")
    app.contact.open_add_new_page()
    app.contact.add_new(Contact("ssdr", "rr", "rrr", "ghjk", "hjj", "rrt", "tttt", "456", "rrtt@rrt.ty"))
    app.contact.go_home_page()
    app.session.logout()




