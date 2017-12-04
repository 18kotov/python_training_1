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


    app.session.open_start_page()
    app.session.login( username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(group_name="ddfg", header="4fff", footer="fbhj"))
    app.group.return_to_groups_page()
    app.session.logout()


def test_ad_empty_group(app):


    app.session.open_start_page()
    app.session.login( username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(group_name="", header="", footer=""))
    app.group.return_to_groups_page()
    app.session.logout()




