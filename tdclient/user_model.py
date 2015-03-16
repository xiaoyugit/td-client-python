#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

from tdclient._model import Model

class User(Model):
    """User on Treasure Data Service
    """

    def __init__(self, client, name, org_name, role_names, email):
        super(User, self).__init__(client)
        self._name = name
        self._org_name = org_name
        self._role_names = role_names
        self._email = email

    @property
    def name(self):
        """
        Returns: name of the user
        """
        return self._name

    @property
    def org_name(self):
        """
        Returns: organization name
        """
        return self._org_name

    @property
    def role_names(self):
        """
        TODO: add docstring
        """
        return self._role_names

    @property
    def email(self):
        """
        Returns: e-mail address
        """
        return self._email
