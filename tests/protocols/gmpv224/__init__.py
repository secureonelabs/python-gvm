# SPDX-FileCopyrightText: 2020-2024 Greenbone AG
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


from gvm.protocols.gmpv224 import Gmp

from .. import GmpTestCase


class Gmpv224TestCase(GmpTestCase):
    gmp_class = Gmp
