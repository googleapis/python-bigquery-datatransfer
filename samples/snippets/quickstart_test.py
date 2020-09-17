# Copyright 2017 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import pytest

import quickstart


PROJECT = os.environ['GOOGLE_CLOUD_PROJECT']


@pytest.fixture
def mock_project_id():
    """Mock out project and replace with project from environment."""

    return PROJECT


def test_quickstart(capsys, mock_project_id):
    quickstart.run_quickstart(mock_project_id)
    out, _ = capsys.readouterr()
    assert 'Supported Data Sources:' in out
