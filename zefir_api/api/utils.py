# NCBR_backend
# Copyright (C) 2023-2024 Narodowe Centrum Badań Jądrowych
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from pathlib import Path
from typing import Final

_api_version: Final[str] = "1"
_api_prefix: Final[str] = f"/api/v{_api_version}"

RESOURCES_PATH = os.getenv("RESOURCES_PATH", os.path.join(".", "simple-data-case"))


def get_api_prefix() -> str:
    return _api_prefix


def get_api_version() -> str:
    return _api_version


def get_resources(x: str | Path) -> Path:
    return Path(os.path.join(RESOURCES_PATH, x))
