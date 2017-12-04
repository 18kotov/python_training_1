# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


    
def test_ad_group(app):


    app.open_start_page()
    app.session.login( username="admin", password="secret")
    app.open_groups_page()
    app.create_group( Group(group_name="ddfg", header="4fff", footer="fbhj"))
    app.return_to_groups_page()
    app.session.logout()


def test_ad_empty_group(app):


    app.open_start_page()
    app.session.login( username="admin", password="secret")
    app.open_groups_page()
    app.create_group( Group(group_name="", header="", footer=""))
    app.return_to_groups_page()
    app.session.logout()




