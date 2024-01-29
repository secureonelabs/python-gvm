# -*- coding: utf-8 -*-
# Copyright (C) 2021-2022 Greenbone AG
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .test_clone_scanner import GmpCloneScannerTestMixin
from .test_create_scanner import GmpCreateScannerTestMixin
from .test_delete_scanner import GmpDeleteScannerTestMixin
from .test_get_scanner import GmpGetScannerTestMixin
from .test_get_scanners import GmpGetScannersTestMixin
from .test_modify_scanner import GmpModifyScannerTestMixin
from .test_verify_scanner import GmpVerifyScannerTestMixin

__all__ = (
    "GmpCloneScannerTestMixin",
    "GmpCreateScannerTestMixin",
    "GmpDeleteScannerTestMixin",
    "GmpGetScannerTestMixin",
    "GmpGetScannersTestMixin",
    "GmpModifyScannerTestMixin",
    "GmpVerifyScannerTestMixin",
)
