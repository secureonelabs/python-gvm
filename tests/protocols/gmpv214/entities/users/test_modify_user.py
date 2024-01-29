# SPDX-FileCopyrightText: 2018-2024 Greenbone AG
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

from gvm.errors import RequiredArgument
from gvm.protocols.gmpv214 import UserAuthType


class GmpModifyUserTestMixin:
    def test_modify_user(self):
        self.gmp.modify_user(user_id="u1")

        self.connection.send.has_been_called_with('<modify_user user_id="u1"/>')

    def test_modify_user_missing_user_id(self):
        with self.assertRaises(RequiredArgument):
            self.gmp.modify_user(user_id=None)

        with self.assertRaises(RequiredArgument):
            self.gmp.modify_user(user_id="")

    def test_modify_user_with_new_name(self):
        self.gmp.modify_user(user_id="u1", name="foo")

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            "<new_name>foo</new_name>"
            "</modify_user>"
        )

    def test_modify_user_with_new_comment(self):
        self.gmp.modify_user(user_id="u1", comment="foo")

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            "<comment>foo</comment>"
            "</modify_user>"
        )

    def test_modify_user_with_role_ids(self):
        self.gmp.modify_user(user_id="u1", role_ids=[])

        self.connection.send.has_been_called_with('<modify_user user_id="u1"/>')

        self.gmp.modify_user(user_id="u1", role_ids=["r1"])

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1"><role id="r1"/></modify_user>'
        )

        self.gmp.modify_user(user_id="u1", role_ids=["r1", "r2"])

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            '<role id="r1"/>'
            '<role id="r2"/>'
            "</modify_user>"
        )

    def test_modify_user_with_group_ids(self):
        self.gmp.modify_user(user_id="u1", role_ids=[])

        self.connection.send.has_been_called_with('<modify_user user_id="u1"/>')

        self.gmp.modify_user(user_id="u1", group_ids=["r1"])

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            '<groups><group id="r1"/></groups>'
            "</modify_user>"
        )

        self.gmp.modify_user(user_id="u1", group_ids=["r1", "r2"])

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            "<groups>"
            '<group id="r1"/>'
            '<group id="r2"/>'
            "</groups>"
            "</modify_user>"
        )

    def test_modify_user_with_password(self):
        self.gmp.modify_user(user_id="u1", password="foo")

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            "<password>foo</password>"
            "</modify_user>"
        )

    def test_modify_user_with_auth_source(self):
        self.gmp.modify_user(
            user_id="u1", auth_source=UserAuthType.LDAP_CONNECT
        )

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            "<sources><source>ldap_connect</source></sources>"
            "</modify_user>"
        )

    def test_modify_user_with_hosts(self):
        self.gmp.modify_user(user_id="u1", hosts=[])

        self.connection.send.has_been_called_with('<modify_user user_id="u1"/>')

        self.gmp.modify_user(user_id="u1", hosts=["foo"])

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            '<hosts allow="0">foo</hosts>'
            "</modify_user>"
        )

        self.gmp.modify_user(user_id="u1", hosts=["foo", "bar"])

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            '<hosts allow="0">foo,bar</hosts>'
            "</modify_user>"
        )

        self.gmp.modify_user(
            user_id="u1", hosts=["foo", "bar"], hosts_allow=False
        )

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            '<hosts allow="0">foo,bar</hosts>'
            "</modify_user>"
        )

        self.gmp.modify_user(
            user_id="u1", hosts=["foo", "bar"], hosts_allow=True
        )

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            '<hosts allow="1">foo,bar</hosts>'
            "</modify_user>"
        )

    def test_modify_user_with_ifaces(self):
        self.gmp.modify_user(user_id="u1", ifaces=[])

        self.connection.send.has_been_called_with('<modify_user user_id="u1"/>')

        self.gmp.modify_user(user_id="u1", ifaces=["foo"])

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            '<ifaces allow="0">foo</ifaces>'
            "</modify_user>"
        )

        self.gmp.modify_user(user_id="u1", ifaces=["foo", "bar"])

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            '<ifaces allow="0">foo,bar</ifaces>'
            "</modify_user>"
        )

        self.gmp.modify_user(
            user_id="u1", ifaces=["foo", "bar"], ifaces_allow=False
        )

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            '<ifaces allow="0">foo,bar</ifaces>'
            "</modify_user>"
        )

        self.gmp.modify_user(
            user_id="u1", ifaces=["foo", "bar"], ifaces_allow=True
        )

        self.connection.send.has_been_called_with(
            '<modify_user user_id="u1">'
            '<ifaces allow="1">foo,bar</ifaces>'
            "</modify_user>"
        )
