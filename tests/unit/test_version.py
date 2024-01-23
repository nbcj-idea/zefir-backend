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

import pyzefir
import zefir_analytics
from fastapi.testclient import TestClient


def test_get_zefir_version(client: TestClient) -> None:
    response = client.get("/pyzefir_version")
    data = response.json()

    assert response.status_code == 200
    assert "pyzefir version" in data
    assert data["pyzefir version"] == pyzefir.__version__


def test_get_zefir_analytics_version(client: TestClient) -> None:
    response = client.get("/zefir_analytics_version")
    data = response.json()

    assert response.status_code == 200
    assert "zefir_analytics version" in data
    assert data["zefir_analytics version"] == zefir_analytics.__version__
