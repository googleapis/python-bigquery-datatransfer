# -*- coding: utf-8 -*-
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
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources
import warnings

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.bigquery_datatransfer_v1.services.data_transfer_service import pagers
from google.cloud.bigquery_datatransfer_v1.types import datatransfer
from google.cloud.bigquery_datatransfer_v1.types import transfer
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import struct_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore
from .transports.base import DataTransferServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import DataTransferServiceGrpcAsyncIOTransport
from .client import DataTransferServiceClient


class DataTransferServiceAsyncClient:
    """This API allows users to manage their data transfers into
    BigQuery.
    """

    _client: DataTransferServiceClient

    DEFAULT_ENDPOINT = DataTransferServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DataTransferServiceClient.DEFAULT_MTLS_ENDPOINT

    data_source_path = staticmethod(DataTransferServiceClient.data_source_path)
    parse_data_source_path = staticmethod(
        DataTransferServiceClient.parse_data_source_path
    )
    run_path = staticmethod(DataTransferServiceClient.run_path)
    parse_run_path = staticmethod(DataTransferServiceClient.parse_run_path)
    transfer_config_path = staticmethod(DataTransferServiceClient.transfer_config_path)
    parse_transfer_config_path = staticmethod(
        DataTransferServiceClient.parse_transfer_config_path
    )
    common_billing_account_path = staticmethod(
        DataTransferServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DataTransferServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DataTransferServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DataTransferServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DataTransferServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DataTransferServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DataTransferServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        DataTransferServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(DataTransferServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        DataTransferServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DataTransferServiceAsyncClient: The constructed client.
        """
        return DataTransferServiceClient.from_service_account_info.__func__(DataTransferServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DataTransferServiceAsyncClient: The constructed client.
        """
        return DataTransferServiceClient.from_service_account_file.__func__(DataTransferServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return DataTransferServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DataTransferServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DataTransferServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(DataTransferServiceClient).get_transport_class,
        type(DataTransferServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, DataTransferServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the data transfer service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.DataTransferServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = DataTransferServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def get_data_source(
        self,
        request: Union[datatransfer.GetDataSourceRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datatransfer.DataSource:
        r"""Retrieves a supported data source and returns its
        settings.


        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_get_data_source():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.GetDataSourceRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_data_source(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.GetDataSourceRequest, dict]):
                The request object. A request to get data source info.
            name (:class:`str`):
                Required. The field will contain name of the resource
                requested, for example:
                ``projects/{project_id}/dataSources/{data_source_id}``
                or
                ``projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.bigquery_datatransfer_v1.types.DataSource:
                Defines the properties and custom
                parameters for a data source.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.GetDataSourceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_data_source,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_data_sources(
        self,
        request: Union[datatransfer.ListDataSourcesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListDataSourcesAsyncPager:
        r"""Lists supported data sources and returns their
        settings.


        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_list_data_sources():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.ListDataSourcesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_data_sources(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.ListDataSourcesRequest, dict]):
                The request object. Request to list supported data
                sources and their data transfer settings.
            parent (:class:`str`):
                Required. The BigQuery project id for which data sources
                should be returned. Must be in the form:
                ``projects/{project_id}`` or
                \`projects/{project_id}/locations/{location_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.pagers.ListDataSourcesAsyncPager:
                Returns list of supported data
                sources and their metadata.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.ListDataSourcesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_data_sources,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListDataSourcesAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_transfer_config(
        self,
        request: Union[datatransfer.CreateTransferConfigRequest, dict] = None,
        *,
        parent: str = None,
        transfer_config: transfer.TransferConfig = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> transfer.TransferConfig:
        r"""Creates a new data transfer configuration.

        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_create_transfer_config():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                transfer_config = bigquery_datatransfer_v1.TransferConfig()
                transfer_config.destination_dataset_id = "destination_dataset_id_value"

                request = bigquery_datatransfer_v1.CreateTransferConfigRequest(
                    parent="parent_value",
                    transfer_config=transfer_config,
                )

                # Make the request
                response = client.create_transfer_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.CreateTransferConfigRequest, dict]):
                The request object. A request to create a data transfer
                configuration. If new credentials are needed for this
                transfer configuration, an authorization code must be
                provided. If an authorization code is provided, the
                transfer configuration will be associated with the user
                id corresponding to the authorization code. Otherwise,
                the transfer configuration will be associated with the
                calling user.
            parent (:class:`str`):
                Required. The BigQuery project id where the transfer
                configuration should be created. Must be in the format
                projects/{project_id}/locations/{location_id} or
                projects/{project_id}. If specified location and
                location of the destination bigquery dataset do not
                match - the request will fail.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            transfer_config (:class:`google.cloud.bigquery_datatransfer_v1.types.TransferConfig`):
                Required. Data transfer configuration
                to create.

                This corresponds to the ``transfer_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.bigquery_datatransfer_v1.types.TransferConfig:
                Represents a data transfer configuration. A transfer configuration
                   contains all metadata needed to perform a data
                   transfer. For example, destination_dataset_id
                   specifies where data should be stored. When a new
                   transfer configuration is created, the specified
                   destination_dataset_id is created when needed and
                   shared with the appropriate data source service
                   account.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, transfer_config])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.CreateTransferConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if transfer_config is not None:
            request.transfer_config = transfer_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_transfer_config,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_transfer_config(
        self,
        request: Union[datatransfer.UpdateTransferConfigRequest, dict] = None,
        *,
        transfer_config: transfer.TransferConfig = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> transfer.TransferConfig:
        r"""Updates a data transfer configuration.
        All fields must be set, even if they are not updated.


        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_update_transfer_config():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                transfer_config = bigquery_datatransfer_v1.TransferConfig()
                transfer_config.destination_dataset_id = "destination_dataset_id_value"

                request = bigquery_datatransfer_v1.UpdateTransferConfigRequest(
                    transfer_config=transfer_config,
                )

                # Make the request
                response = client.update_transfer_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.UpdateTransferConfigRequest, dict]):
                The request object. A request to update a transfer
                configuration. To update the user id of the transfer
                configuration, an authorization code needs to be
                provided.
            transfer_config (:class:`google.cloud.bigquery_datatransfer_v1.types.TransferConfig`):
                Required. Data transfer configuration
                to create.

                This corresponds to the ``transfer_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Required list of fields to
                be updated in this request.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.bigquery_datatransfer_v1.types.TransferConfig:
                Represents a data transfer configuration. A transfer configuration
                   contains all metadata needed to perform a data
                   transfer. For example, destination_dataset_id
                   specifies where data should be stored. When a new
                   transfer configuration is created, the specified
                   destination_dataset_id is created when needed and
                   shared with the appropriate data source service
                   account.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([transfer_config, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.UpdateTransferConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if transfer_config is not None:
            request.transfer_config = transfer_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_transfer_config,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("transfer_config.name", request.transfer_config.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def delete_transfer_config(
        self,
        request: Union[datatransfer.DeleteTransferConfigRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a data transfer configuration, including any
        associated transfer runs and logs.


        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_delete_transfer_config():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.DeleteTransferConfigRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_transfer_config(request=request)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.DeleteTransferConfigRequest, dict]):
                The request object. A request to delete data transfer
                information. All associated transfer runs and log
                messages will be deleted as well.
            name (:class:`str`):
                Required. The field will contain name of the resource
                requested, for example:
                ``projects/{project_id}/transferConfigs/{config_id}`` or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.DeleteTransferConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_transfer_config,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    async def get_transfer_config(
        self,
        request: Union[datatransfer.GetTransferConfigRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> transfer.TransferConfig:
        r"""Returns information about a data transfer config.

        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_get_transfer_config():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.GetTransferConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_transfer_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.GetTransferConfigRequest, dict]):
                The request object. A request to get data transfer
                information.
            name (:class:`str`):
                Required. The field will contain name of the resource
                requested, for example:
                ``projects/{project_id}/transferConfigs/{config_id}`` or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.bigquery_datatransfer_v1.types.TransferConfig:
                Represents a data transfer configuration. A transfer configuration
                   contains all metadata needed to perform a data
                   transfer. For example, destination_dataset_id
                   specifies where data should be stored. When a new
                   transfer configuration is created, the specified
                   destination_dataset_id is created when needed and
                   shared with the appropriate data source service
                   account.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.GetTransferConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_transfer_config,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_transfer_configs(
        self,
        request: Union[datatransfer.ListTransferConfigsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTransferConfigsAsyncPager:
        r"""Returns information about all transfer configs owned
        by a project in the specified location.


        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_list_transfer_configs():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.ListTransferConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_transfer_configs(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.ListTransferConfigsRequest, dict]):
                The request object. A request to list data transfers
                configured for a BigQuery project.
            parent (:class:`str`):
                Required. The BigQuery project id for which data sources
                should be returned: ``projects/{project_id}`` or
                ``projects/{project_id}/locations/{location_id}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.pagers.ListTransferConfigsAsyncPager:
                The returned list of pipelines in the
                project.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.ListTransferConfigsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_transfer_configs,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListTransferConfigsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def schedule_transfer_runs(
        self,
        request: Union[datatransfer.ScheduleTransferRunsRequest, dict] = None,
        *,
        parent: str = None,
        start_time: timestamp_pb2.Timestamp = None,
        end_time: timestamp_pb2.Timestamp = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datatransfer.ScheduleTransferRunsResponse:
        r"""Creates transfer runs for a time range [start_time, end_time].
        For each date - or whatever granularity the data source supports
        - in the range, one transfer run is created. Note that runs are
        created per UTC time in the time range. DEPRECATED: use
        StartManualTransferRuns instead.


        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_schedule_transfer_runs():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.ScheduleTransferRunsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.schedule_transfer_runs(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.ScheduleTransferRunsRequest, dict]):
                The request object. A request to schedule transfer runs
                for a time range.
            parent (:class:`str`):
                Required. Transfer configuration name in the form:
                ``projects/{project_id}/transferConfigs/{config_id}`` or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            start_time (:class:`google.protobuf.timestamp_pb2.Timestamp`):
                Required. Start time of the range of transfer runs. For
                example, ``"2017-05-25T00:00:00+00:00"``.

                This corresponds to the ``start_time`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            end_time (:class:`google.protobuf.timestamp_pb2.Timestamp`):
                Required. End time of the range of transfer runs. For
                example, ``"2017-05-30T00:00:00+00:00"``.

                This corresponds to the ``end_time`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.bigquery_datatransfer_v1.types.ScheduleTransferRunsResponse:
                A response to schedule transfer runs
                for a time range.

        """
        warnings.warn(
            "DataTransferServiceAsyncClient.schedule_transfer_runs is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, start_time, end_time])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.ScheduleTransferRunsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if start_time is not None:
            request.start_time = start_time
        if end_time is not None:
            request.end_time = end_time

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.schedule_transfer_runs,
            default_timeout=30.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def start_manual_transfer_runs(
        self,
        request: Union[datatransfer.StartManualTransferRunsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datatransfer.StartManualTransferRunsResponse:
        r"""Start manual transfer runs to be executed now with schedule_time
        equal to current time. The transfer runs can be created for a
        time range where the run_time is between start_time (inclusive)
        and end_time (exclusive), or for a specific run_time.


        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_start_manual_transfer_runs():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.StartManualTransferRunsRequest(
                )

                # Make the request
                response = client.start_manual_transfer_runs(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.StartManualTransferRunsRequest, dict]):
                The request object. A request to start manual transfer
                runs.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.bigquery_datatransfer_v1.types.StartManualTransferRunsResponse:
                A response to start manual transfer
                runs.

        """
        # Create or coerce a protobuf request object.
        request = datatransfer.StartManualTransferRunsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.start_manual_transfer_runs,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_transfer_run(
        self,
        request: Union[datatransfer.GetTransferRunRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> transfer.TransferRun:
        r"""Returns information about the particular transfer
        run.


        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_get_transfer_run():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.GetTransferRunRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_transfer_run(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.GetTransferRunRequest, dict]):
                The request object. A request to get data transfer run
                information.
            name (:class:`str`):
                Required. The field will contain name of the resource
                requested, for example:
                ``projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}``
                or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.bigquery_datatransfer_v1.types.TransferRun:
                Represents a data transfer run.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.GetTransferRunRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_transfer_run,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def delete_transfer_run(
        self,
        request: Union[datatransfer.DeleteTransferRunRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes the specified transfer run.

        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_delete_transfer_run():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.DeleteTransferRunRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_transfer_run(request=request)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.DeleteTransferRunRequest, dict]):
                The request object. A request to delete data transfer
                run information.
            name (:class:`str`):
                Required. The field will contain name of the resource
                requested, for example:
                ``projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}``
                or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.DeleteTransferRunRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_transfer_run,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    async def list_transfer_runs(
        self,
        request: Union[datatransfer.ListTransferRunsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTransferRunsAsyncPager:
        r"""Returns information about running and completed
        transfer runs.


        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_list_transfer_runs():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.ListTransferRunsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_transfer_runs(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.ListTransferRunsRequest, dict]):
                The request object. A request to list data transfer
                runs.
            parent (:class:`str`):
                Required. Name of transfer configuration for which
                transfer runs should be retrieved. Format of transfer
                configuration resource name is:
                ``projects/{project_id}/transferConfigs/{config_id}`` or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.pagers.ListTransferRunsAsyncPager:
                The returned list of pipelines in the
                project.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.ListTransferRunsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_transfer_runs,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListTransferRunsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_transfer_logs(
        self,
        request: Union[datatransfer.ListTransferLogsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTransferLogsAsyncPager:
        r"""Returns log messages for the transfer run.

        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_list_transfer_logs():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.ListTransferLogsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_transfer_logs(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.ListTransferLogsRequest, dict]):
                The request object. A request to get user facing log
                messages associated with data transfer run.
            parent (:class:`str`):
                Required. Transfer run name in the form:
                ``projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}``
                or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.pagers.ListTransferLogsAsyncPager:
                The returned list transfer run
                messages.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.ListTransferLogsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_transfer_logs,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListTransferLogsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def check_valid_creds(
        self,
        request: Union[datatransfer.CheckValidCredsRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> datatransfer.CheckValidCredsResponse:
        r"""Returns true if valid credentials exist for the given
        data source and requesting user.


        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_check_valid_creds():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.CheckValidCredsRequest(
                    name="name_value",
                )

                # Make the request
                response = client.check_valid_creds(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.CheckValidCredsRequest, dict]):
                The request object. A request to determine whether the
                user has valid credentials. This method is used to limit
                the number of OAuth popups in the user interface. The
                user id is inferred from the API call context.
                If the data source has the Google+ authorization type,
                this method returns false, as it cannot be determined
                whether the credentials are already valid merely based
                on the user id.
            name (:class:`str`):
                Required. The data source in the form:
                ``projects/{project_id}/dataSources/{data_source_id}``
                or
                ``projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.bigquery_datatransfer_v1.types.CheckValidCredsResponse:
                A response indicating whether the
                credentials exist and are valid.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = datatransfer.CheckValidCredsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.check_valid_creds,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=20.0,
            ),
            default_timeout=20.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def enroll_data_sources(
        self,
        request: Union[datatransfer.EnrollDataSourcesRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Enroll data sources in a user project. This allows
        users to create transfer configurations for these data
        sources. They will also appear in the ListDataSources
        RPC and as such, will appear in the BigQuery UI
        'https://bigquery.cloud.google.com' (and the documents
        can be found at
        https://cloud.google.com/bigquery/bigquery-web-ui and
        https://cloud.google.com/bigquery/docs/working-with-transfers).


        .. code-block::

            from google.cloud import bigquery_datatransfer_v1

            def sample_enroll_data_sources():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.EnrollDataSourcesRequest(
                )

                # Make the request
                client.enroll_data_sources(request=request)

        Args:
            request (Union[google.cloud.bigquery_datatransfer_v1.types.EnrollDataSourcesRequest, dict]):
                The request object. A request to enroll a set of data
                sources so they are visible in the BigQuery UI's
                `Transfer` tab.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        request = datatransfer.EnrollDataSourcesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.enroll_data_sources,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-bigquery-datatransfer",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("DataTransferServiceAsyncClient",)
