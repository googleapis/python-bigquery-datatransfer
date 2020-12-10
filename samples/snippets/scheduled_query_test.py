# Copyright 2020 Google LLC
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

from . import scheduled_query


def test_create_scheduled_query(capsys, project_id, dataset_id, to_delete_configs):
    transfer_config = scheduled_query.create_scheduled_query(
        {
            "project_id": project_id,
            "dataset_id": dataset_id,
        }
    )
    to_delete_configs.append(transfer_config.name)
    out, _ = capsys.readouterr()
    assert transfer_config.name in out


def test_create_scheduled_query_with_service_account(
    capsys, project_id, dataset_id, service_account_name, to_delete_configs
):
    transfer_config = scheduled_query.create_scheduled_query_with_service_account(
        {
            "project_id": project_id,
            "dataset_id": dataset_id,
            "service_account_name": service_account_name,
        }
    )
    to_delete_configs.append(transfer_config.name)
    out, _ = capsys.readouterr()
    assert transfer_config.name in out
