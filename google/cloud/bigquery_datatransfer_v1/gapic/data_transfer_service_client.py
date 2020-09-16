# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.cloud.bigquery.datatransfer.v1 DataTransferService API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.path_template
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import google.api_core.protobuf_helpers
import grpc

from google.cloud.bigquery_datatransfer_v1.gapic import (
    data_transfer_service_client_config,
)
from google.cloud.bigquery_datatransfer_v1.gapic import enums
from google.cloud.bigquery_datatransfer_v1.gapic.transports import (
    data_transfer_service_grpc_transport,
)
from google.cloud.bigquery_datatransfer_v1.proto import datatransfer_pb2
from google.cloud.bigquery_datatransfer_v1.proto import datatransfer_pb2_grpc
from google.cloud.bigquery_datatransfer_v1.proto import transfer_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import timestamp_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-bigquery-datatransfer",
).version


class DataTransferServiceClient(object):
    """
    The Google BigQuery Data Transfer Service API enables BigQuery users to
    configure the transfer of their data from other Google Products into
    BigQuery. This service contains methods that are end user exposed. It backs
    up the frontend.
    """

    SERVICE_ADDRESS = "bigquerydatatransfer.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.bigquery.datatransfer.v1.DataTransferService"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DataTransferServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def data_source_path(cls, project, data_source):
        """Return a fully-qualified data_source string."""
        return google.api_core.path_template.expand(
            "projects/{project}/dataSources/{data_source}",
            project=project,
            data_source=data_source,
        )

    @classmethod
    def location_path(cls, project, location):
        """Return a fully-qualified location string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}",
            project=project,
            location=location,
        )

    @classmethod
    def location_data_source_path(cls, project, location, data_source):
        """Return a fully-qualified location_data_source string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/dataSources/{data_source}",
            project=project,
            location=location,
            data_source=data_source,
        )

    @classmethod
    def location_run_path(cls, project, location, transfer_config, run):
        """Return a fully-qualified location_run string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/transferConfigs/{transfer_config}/runs/{run}",
            project=project,
            location=location,
            transfer_config=transfer_config,
            run=run,
        )

    @classmethod
    def location_transfer_config_path(cls, project, location, transfer_config):
        """Return a fully-qualified location_transfer_config string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/transferConfigs/{transfer_config}",
            project=project,
            location=location,
            transfer_config=transfer_config,
        )

    @classmethod
    def project_path(cls, project):
        """Return a fully-qualified project string."""
        return google.api_core.path_template.expand(
            "projects/{project}", project=project,
        )

    @classmethod
    def project_data_source_path(cls, project, data_source):
        """Return a fully-qualified project_data_source string."""
        return google.api_core.path_template.expand(
            "projects/{project}/dataSources/{data_source}",
            project=project,
            data_source=data_source,
        )

    @classmethod
    def project_run_path(cls, project, transfer_config, run):
        """Return a fully-qualified project_run string."""
        return google.api_core.path_template.expand(
            "projects/{project}/transferConfigs/{transfer_config}/runs/{run}",
            project=project,
            transfer_config=transfer_config,
            run=run,
        )

    @classmethod
    def project_transfer_config_path(cls, project, transfer_config):
        """Return a fully-qualified project_transfer_config string."""
        return google.api_core.path_template.expand(
            "projects/{project}/transferConfigs/{transfer_config}",
            project=project,
            transfer_config=transfer_config,
        )

    @classmethod
    def run_path(cls, project, transfer_config, run):
        """Return a fully-qualified run string."""
        return google.api_core.path_template.expand(
            "projects/{project}/transferConfigs/{transfer_config}/runs/{run}",
            project=project,
            transfer_config=transfer_config,
            run=run,
        )

    @classmethod
    def transfer_config_path(cls, project, transfer_config):
        """Return a fully-qualified transfer_config string."""
        return google.api_core.path_template.expand(
            "projects/{project}/transferConfigs/{transfer_config}",
            project=project,
            transfer_config=transfer_config,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.DataTransferServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.DataTransferServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.

        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = data_transfer_service_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=data_transfer_service_grpc_transport.DataTransferServiceGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = data_transfer_service_grpc_transport.DataTransferServiceGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials,
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION,
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME],
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def get_data_source(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Retrieves a supported data source and returns its settings,
        which can be used for UI rendering.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> name = client.project_data_source_path('[PROJECT]', '[DATA_SOURCE]')
            >>>
            >>> response = client.get_data_source(name)

        Args:
            name (str): Start time of the range of transfer runs. For example,
                ``"2017-05-25T00:00:00+00:00"``. The start_time must be strictly less
                than the end_time. Creates transfer runs where run_time is in the range
                betwen start_time (inclusive) and end_time (exlusive).
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_datatransfer_v1.types.DataSource` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_data_source" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_data_source"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_data_source,
                default_retry=self._method_configs["GetDataSource"].retry,
                default_timeout=self._method_configs["GetDataSource"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.GetDataSourceRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_data_source"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_data_sources(
        self,
        parent,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists supported data sources and returns their settings,
        which can be used for UI rendering.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_data_sources(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_data_sources(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Signed seconds of the span of time. Must be from -315,576,000,000 to
                +315,576,000,000 inclusive. Note: these bounds are computed from: 60
                sec/min \* 60 min/hr \* 24 hr/day \* 365.25 days/year \* 10000 years
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.bigquery_datatransfer_v1.types.DataSource` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_data_sources" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_data_sources"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_data_sources,
                default_retry=self._method_configs["ListDataSources"].retry,
                default_timeout=self._method_configs["ListDataSources"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.ListDataSourcesRequest(
            parent=parent, page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_data_sources"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="data_sources",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def create_transfer_config(
        self,
        parent,
        transfer_config,
        authorization_code=None,
        version_info=None,
        service_account_name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a new data transfer configuration.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> # TODO: Initialize `transfer_config`:
            >>> transfer_config = {}
            >>>
            >>> response = client.create_transfer_config(parent, transfer_config)

        Args:
            parent (str): Signed fractions of a second at nanosecond resolution of the span of
                time. Durations less than one second are represented with a 0
                ``seconds`` field and a positive or negative ``nanos`` field. For
                durations of one second or more, a non-zero value for the ``nanos``
                field must be of the same sign as the ``seconds`` field. Must be from
                -999,999,999 to +999,999,999 inclusive.
            transfer_config (Union[dict, ~google.cloud.bigquery_datatransfer_v1.types.TransferConfig]): Required. Data transfer configuration to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_datatransfer_v1.types.TransferConfig`
            authorization_code (str): Required. Name of transfer configuration for which transfer runs
                should be retrieved. Format of transfer configuration resource name is:
                ``projects/{project_id}/transferConfigs/{config_id}`` or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``.
            version_info (str): Should this field be parsed lazily? Lazy applies only to
                message-type fields. It means that when the outer message is initially
                parsed, the inner message's contents will not be parsed but instead
                stored in encoded form. The inner message will actually be parsed when
                it is first accessed.

                This is only a hint. Implementations are free to choose whether to use
                eager or lazy parsing regardless of the value of this option. However,
                setting this option true suggests that the protocol author believes that
                using lazy parsing on this field is worth the additional bookkeeping
                overhead typically needed to implement it.

                This option does not affect the public interface of any generated code;
                all method signatures remain the same. Furthermore, thread-safety of the
                interface is not affected by this option; const methods remain safe to
                call from multiple threads concurrently, while non-const methods
                continue to require exclusive access.

                Note that implementations may choose not to check required fields within
                a lazy sub-message. That is, calling IsInitialized() on the outer
                message may return true even if the inner message has missing required
                fields. This is necessary because otherwise the inner message would have
                to be parsed in order to perform the check, defeating the purpose of
                lazy parsing. An implementation which chooses not to check required
                fields must be consistent about it. That is, for any particular
                sub-message, the implementation must either *always* check its required
                fields, or *never* check its required fields, regardless of whether or
                not the message has been parsed.
            service_account_name (str): Optional service account name. If this field is set, transfer config will
                be created with this service account credentials. It requires that
                requesting user calling this API has permissions to act as this service
                account.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_datatransfer_v1.types.TransferConfig` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_transfer_config" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_transfer_config"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_transfer_config,
                default_retry=self._method_configs["CreateTransferConfig"].retry,
                default_timeout=self._method_configs["CreateTransferConfig"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.CreateTransferConfigRequest(
            parent=parent,
            transfer_config=transfer_config,
            authorization_code=authorization_code,
            version_info=version_info,
            service_account_name=service_account_name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_transfer_config"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_transfer_config(
        self,
        transfer_config,
        update_mask,
        authorization_code=None,
        version_info=None,
        service_account_name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates a data transfer configuration.
        All fields must be set, even if they are not updated.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> # TODO: Initialize `transfer_config`:
            >>> transfer_config = {}
            >>>
            >>> # TODO: Initialize `update_mask`:
            >>> update_mask = {}
            >>>
            >>> response = client.update_transfer_config(transfer_config, update_mask)

        Args:
            transfer_config (Union[dict, ~google.cloud.bigquery_datatransfer_v1.types.TransferConfig]): Required. Data transfer configuration to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_datatransfer_v1.types.TransferConfig`
            update_mask (Union[dict, ~google.cloud.bigquery_datatransfer_v1.types.FieldMask]): Required. Required list of fields to be updated in this request.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_datatransfer_v1.types.FieldMask`
            authorization_code (str): Optional. The historical or future-looking state of the resource
                pattern.

                Example:

                ::

                    // The InspectTemplate message originally only supported resource
                    // names with organization, and project was added later.
                    message InspectTemplate {
                      option (google.api.resource) = {
                        type: "dlp.googleapis.com/InspectTemplate"
                        pattern:
                        "organizations/{organization}/inspectTemplates/{inspect_template}"
                        pattern: "projects/{project}/inspectTemplates/{inspect_template}"
                        history: ORIGINALLY_SINGLE_PATTERN
                      };
                    }
            version_info (str): Transfer configuration name in the form:
                ``projects/{project_id}/transferConfigs/{config_id}`` or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``.
            service_account_name (str): Required. Start time of the range of transfer runs. For example,
                ``"2017-05-25T00:00:00+00:00"``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_datatransfer_v1.types.TransferConfig` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_transfer_config" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_transfer_config"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_transfer_config,
                default_retry=self._method_configs["UpdateTransferConfig"].retry,
                default_timeout=self._method_configs["UpdateTransferConfig"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.UpdateTransferConfigRequest(
            transfer_config=transfer_config,
            update_mask=update_mask,
            authorization_code=authorization_code,
            version_info=version_info,
            service_account_name=service_account_name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("transfer_config.name", transfer_config.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_transfer_config"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_transfer_config(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a data transfer configuration,
        including any associated transfer runs and logs.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> name = client.project_transfer_config_path('[PROJECT]', '[TRANSFER_CONFIG]')
            >>>
            >>> client.delete_transfer_config(name)

        Args:
            name (str): The resource name of the transfer config. Transfer config names have
                the form of
                ``projects/{project_id}/locations/{region}/transferConfigs/{config_id}``.
                The name is automatically generated based on the config_id specified in
                CreateTransferConfigRequest along with project_id and region. If
                config_id is not provided, usually a uuid, even though it is not
                guaranteed or required, will be generated for config_id.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_transfer_config" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_transfer_config"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_transfer_config,
                default_retry=self._method_configs["DeleteTransferConfig"].retry,
                default_timeout=self._method_configs["DeleteTransferConfig"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.DeleteTransferConfigRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_transfer_config"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_transfer_config(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns information about a data transfer config.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> name = client.project_transfer_config_path('[PROJECT]', '[TRANSFER_CONFIG]')
            >>>
            >>> response = client.get_transfer_config(name)

        Args:
            name (str): Protocol Buffers - Google's data interchange format Copyright 2008
                Google Inc. All rights reserved.
                https://developers.google.com/protocol-buffers/

                Redistribution and use in source and binary forms, with or without
                modification, are permitted provided that the following conditions are
                met:

                ::

                    * Redistributions of source code must retain the above copyright

                notice, this list of conditions and the following disclaimer. \*
                Redistributions in binary form must reproduce the above copyright
                notice, this list of conditions and the following disclaimer in the
                documentation and/or other materials provided with the distribution. \*
                Neither the name of Google Inc. nor the names of its contributors may be
                used to endorse or promote products derived from this software without
                specific prior written permission.

                THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
                IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
                TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
                PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
                OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
                EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
                PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
                PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
                LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
                NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
                SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_datatransfer_v1.types.TransferConfig` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_transfer_config" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_transfer_config"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_transfer_config,
                default_retry=self._method_configs["GetTransferConfig"].retry,
                default_timeout=self._method_configs["GetTransferConfig"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.GetTransferConfigRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_transfer_config"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_transfer_configs(
        self,
        parent,
        data_source_ids=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns information about all data transfers in the project.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_transfer_configs(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_transfer_configs(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): See ``HttpRule``.
            data_source_ids (list[str]): When specified, only configurations of requested data sources are returned.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.bigquery_datatransfer_v1.types.TransferConfig` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_transfer_configs" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_transfer_configs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_transfer_configs,
                default_retry=self._method_configs["ListTransferConfigs"].retry,
                default_timeout=self._method_configs["ListTransferConfigs"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.ListTransferConfigsRequest(
            parent=parent, data_source_ids=data_source_ids, page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_transfer_configs"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="transfer_configs",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def schedule_transfer_runs(
        self,
        parent,
        start_time,
        end_time,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        If type_name is set, this need not be set. If both this and
        type_name are set, this must be one of TYPE_ENUM, TYPE_MESSAGE or
        TYPE_GROUP.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> parent = client.project_transfer_config_path('[PROJECT]', '[TRANSFER_CONFIG]')
            >>>
            >>> # TODO: Initialize `start_time`:
            >>> start_time = {}
            >>>
            >>> # TODO: Initialize `end_time`:
            >>> end_time = {}
            >>>
            >>> response = client.schedule_transfer_runs(parent, start_time, end_time)

        Args:
            parent (str): The name of the uninterpreted option. Each string represents a
                segment in a dot-separated name. is_extension is true iff a segment
                represents an extension (denoted with parentheses in options specs in
                .proto files). E.g.,{ ["foo", false], ["bar.baz", true], ["qux", false]
                } represents "foo.(bar.baz).qux".
            start_time (Union[dict, ~google.cloud.bigquery_datatransfer_v1.types.Timestamp]): A generic empty message that you can re-use to avoid defining
                duplicated empty messages in your APIs. A typical example is to use it
                as the request or the response type of an API method. For instance:

                ::

                    service Foo {
                      rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);
                    }

                The JSON representation for ``Empty`` is empty JSON object ``{}``.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_datatransfer_v1.types.Timestamp`
            end_time (Union[dict, ~google.cloud.bigquery_datatransfer_v1.types.Timestamp]): The resource has one pattern, but the API owner expects to add more
                later. (This is the inverse of ORIGINALLY_SINGLE_PATTERN, and prevents
                that from being necessary once there are multiple patterns.)

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_datatransfer_v1.types.Timestamp`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_datatransfer_v1.types.ScheduleTransferRunsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "schedule_transfer_runs" not in self._inner_api_calls:
            self._inner_api_calls[
                "schedule_transfer_runs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.schedule_transfer_runs,
                default_retry=self._method_configs["ScheduleTransferRuns"].retry,
                default_timeout=self._method_configs["ScheduleTransferRuns"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.ScheduleTransferRunsRequest(
            parent=parent, start_time=start_time, end_time=end_time,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["schedule_transfer_runs"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def start_manual_transfer_runs(
        self,
        parent=None,
        requested_time_range=None,
        requested_run_time=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Pagination token, which can be used to request a specific page of
        ``ListTransferRunsRequest`` list results. For multiple-page results,
        ``ListTransferRunsResponse`` outputs a ``next_page`` token, which can be
        used as the ``page_token`` value to request the next page of list
        results.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> response = client.start_manual_transfer_runs()

        Args:
            parent (str): A Timestamp represents a point in time independent of any time zone
                or local calendar, encoded as a count of seconds and fractions of
                seconds at nanosecond resolution. The count is relative to an epoch at
                UTC midnight on January 1, 1970, in the proleptic Gregorian calendar
                which extends the Gregorian calendar backwards to year one.

                All minutes are 60 seconds long. Leap seconds are "smeared" so that no
                leap second table is needed for interpretation, using a `24-hour linear
                smear <https://developers.google.com/time/smear>`__.

                The range is from 0001-01-01T00:00:00Z to
                9999-12-31T23:59:59.999999999Z. By restricting to that range, we ensure
                that we can convert to and from `RFC
                3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ date strings.

                # Examples

                Example 1: Compute Timestamp from POSIX ``time()``.

                ::

                    Timestamp timestamp;
                    timestamp.set_seconds(time(NULL));
                    timestamp.set_nanos(0);

                Example 2: Compute Timestamp from POSIX ``gettimeofday()``.

                ::

                    struct timeval tv;
                    gettimeofday(&tv, NULL);

                    Timestamp timestamp;
                    timestamp.set_seconds(tv.tv_sec);
                    timestamp.set_nanos(tv.tv_usec * 1000);

                Example 3: Compute Timestamp from Win32 ``GetSystemTimeAsFileTime()``.

                ::

                    FILETIME ft;
                    GetSystemTimeAsFileTime(&ft);
                    UINT64 ticks = (((UINT64)ft.dwHighDateTime) << 32) | ft.dwLowDateTime;

                    // A Windows tick is 100 nanoseconds. Windows epoch 1601-01-01T00:00:00Z
                    // is 11644473600 seconds before Unix epoch 1970-01-01T00:00:00Z.
                    Timestamp timestamp;
                    timestamp.set_seconds((INT64) ((ticks / 10000000) - 11644473600LL));
                    timestamp.set_nanos((INT32) ((ticks % 10000000) * 100));

                Example 4: Compute Timestamp from Java ``System.currentTimeMillis()``.

                ::

                    long millis = System.currentTimeMillis();

                    Timestamp timestamp = Timestamp.newBuilder().setSeconds(millis / 1000)
                        .setNanos((int) ((millis % 1000) * 1000000)).build();

                Example 5: Compute Timestamp from current time in Python.

                ::

                    timestamp = Timestamp()
                    timestamp.GetCurrentTime()

                # JSON Mapping

                In JSON format, the Timestamp type is encoded as a string in the `RFC
                3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ format. That is, the
                format is "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z" where
                {year} is always expressed using four digits while {month}, {day},
                {hour}, {min}, and {sec} are zero-padded to two digits each. The
                fractional seconds, which can go up to 9 digits (i.e. up to 1 nanosecond
                resolution), are optional. The "Z" suffix indicates the timezone
                ("UTC"); the timezone is required. A proto3 JSON serializer should
                always use UTC (as indicated by "Z") when printing the Timestamp type
                and a proto3 JSON parser should be able to accept both UTC and other
                timezones (as indicated by an offset).

                For example, "2017-01-15T01:30:15.01Z" encodes 15.01 seconds past 01:30
                UTC on January 15, 2017.

                In JavaScript, one can convert a Date object to this format using the
                standard
                `toISOString() <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString>`__
                method. In Python, a standard ``datetime.datetime`` object can be
                converted to this format using
                ```strftime`` <https://docs.python.org/2/library/time.html#time.strftime>`__
                with the time format spec '%Y-%m-%dT%H:%M:%S.%fZ'. Likewise, in Java,
                one can use the Joda Time's
                ```ISODateTimeFormat.dateTime()`` <http://www.joda.org/joda-time/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTime%2D%2D>`__
                to obtain a formatter capable of generating timestamps in this format.
            requested_time_range (Union[dict, ~google.cloud.bigquery_datatransfer_v1.types.TimeRange]): Time range for the transfer runs that should be started.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_datatransfer_v1.types.TimeRange`
            requested_run_time (Union[dict, ~google.cloud.bigquery_datatransfer_v1.types.Timestamp]): Protocol Buffers - Google's data interchange format Copyright 2008
                Google Inc. All rights reserved.
                https://developers.google.com/protocol-buffers/

                Redistribution and use in source and binary forms, with or without
                modification, are permitted provided that the following conditions are
                met:

                ::

                    * Redistributions of source code must retain the above copyright

                notice, this list of conditions and the following disclaimer. \*
                Redistributions in binary form must reproduce the above copyright
                notice, this list of conditions and the following disclaimer in the
                documentation and/or other materials provided with the distribution. \*
                Neither the name of Google Inc. nor the names of its contributors may be
                used to endorse or promote products derived from this software without
                specific prior written permission.

                THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
                IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
                TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
                PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
                OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
                EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
                PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
                PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
                LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
                NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
                SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_datatransfer_v1.types.Timestamp`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_datatransfer_v1.types.StartManualTransferRunsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "start_manual_transfer_runs" not in self._inner_api_calls:
            self._inner_api_calls[
                "start_manual_transfer_runs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.start_manual_transfer_runs,
                default_retry=self._method_configs["StartManualTransferRuns"].retry,
                default_timeout=self._method_configs["StartManualTransferRuns"].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            requested_time_range=requested_time_range,
            requested_run_time=requested_run_time,
        )

        request = datatransfer_pb2.StartManualTransferRunsRequest(
            parent=parent,
            requested_time_range=requested_time_range,
            requested_run_time=requested_run_time,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["start_manual_transfer_runs"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_transfer_run(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns information about the particular transfer run.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> name = client.project_run_path('[PROJECT]', '[TRANSFER_CONFIG]', '[RUN]')
            >>>
            >>> response = client.get_transfer_run(name)

        Args:
            name (str): An annotation that describes a resource definition, see
                ``ResourceDescriptor``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_datatransfer_v1.types.TransferRun` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_transfer_run" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_transfer_run"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_transfer_run,
                default_retry=self._method_configs["GetTransferRun"].retry,
                default_timeout=self._method_configs["GetTransferRun"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.GetTransferRunRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_transfer_run"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_transfer_run(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes the specified transfer run.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> name = client.project_run_path('[PROJECT]', '[TRANSFER_CONFIG]', '[RUN]')
            >>>
            >>> client.delete_transfer_run(name)

        Args:
            name (str): Optional OAuth2 authorization code to use with this transfer
                configuration. This is required if new credentials are needed, as
                indicated by ``CheckValidCreds``. In order to obtain authorization_code,
                please make a request to
                https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?client_id=&scope=<data_source_scopes>&redirect_uri=<redirect_uri>

                -  client_id should be OAuth client_id of BigQuery DTS API for the given
                   data source returned by ListDataSources method.
                -  data_source_scopes are the scopes returned by ListDataSources method.
                -  redirect_uri is an optional parameter. If not specified, then
                   authorization code is posted to the opener of authorization flow
                   window. Otherwise it will be sent to the redirect uri. A special
                   value of urn:ietf:wg:oauth:2.0:oob means that authorization code
                   should be returned in the title bar of the browser, with the page
                   text prompting the user to copy the code and paste it in the
                   application.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_transfer_run" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_transfer_run"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_transfer_run,
                default_retry=self._method_configs["DeleteTransferRun"].retry,
                default_timeout=self._method_configs["DeleteTransferRun"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.DeleteTransferRunRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_transfer_run"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_transfer_runs(
        self,
        parent,
        states=None,
        page_size=None,
        run_attempt=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns information about running and completed jobs.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> parent = client.project_transfer_config_path('[PROJECT]', '[TRANSFER_CONFIG]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_transfer_runs(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_transfer_runs(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Optional version info. If users want to find a very recent access
                token, that is, immediately after approving access, users have to set
                the version_info claim in the token request. To obtain the version_info,
                users must use the "none+gsession" response type. which be return a
                version_info back in the authorization response which be be put in a JWT
                claim in the token request.
            states (list[~google.cloud.bigquery_datatransfer_v1.types.TransferState]): When specified, only transfer runs with requested states are returned.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            run_attempt (~google.cloud.bigquery_datatransfer_v1.types.RunAttempt): Indicates how run attempts are to be pulled.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.bigquery_datatransfer_v1.types.TransferRun` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_transfer_runs" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_transfer_runs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_transfer_runs,
                default_retry=self._method_configs["ListTransferRuns"].retry,
                default_timeout=self._method_configs["ListTransferRuns"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.ListTransferRunsRequest(
            parent=parent, states=states, page_size=page_size, run_attempt=run_attempt,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_transfer_runs"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="transfer_runs",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def list_transfer_logs(
        self,
        parent,
        page_size=None,
        message_types=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns user facing log messages for the data transfer run.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> parent = client.project_run_path('[PROJECT]', '[TRANSFER_CONFIG]', '[RUN]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_transfer_logs(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_transfer_logs(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): ``ListValue`` is a wrapper around a repeated field of values.

                The JSON representation for ``ListValue`` is JSON array.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            message_types (list[~google.cloud.bigquery_datatransfer_v1.types.MessageSeverity]): Message types to return. If not populated - INFO, WARNING and ERROR
                messages are returned.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.bigquery_datatransfer_v1.types.TransferMessage` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_transfer_logs" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_transfer_logs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_transfer_logs,
                default_retry=self._method_configs["ListTransferLogs"].retry,
                default_timeout=self._method_configs["ListTransferLogs"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.ListTransferLogsRequest(
            parent=parent, page_size=page_size, message_types=message_types,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_transfer_logs"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="transfer_messages",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def check_valid_creds(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns true if valid credentials exist for the given data source and
        requesting user.
        Some data sources doesn't support service account, so we need to talk to
        them on behalf of the end user. This API just checks whether we have OAuth
        token for the particular user, which is a pre-requisite before user can
        create a transfer config.

        Example:
            >>> from google.cloud import bigquery_datatransfer_v1
            >>>
            >>> client = bigquery_datatransfer_v1.DataTransferServiceClient()
            >>>
            >>> name = client.project_data_source_path('[PROJECT]', '[DATA_SOURCE]')
            >>>
            >>> response = client.check_valid_creds(name)

        Args:
            name (str): Output only. The next-pagination token. For multiple-page list
                results, this token can be used as the
                ``ListTransferConfigsRequest.page_token`` to request the next page of
                list results.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_datatransfer_v1.types.CheckValidCredsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "check_valid_creds" not in self._inner_api_calls:
            self._inner_api_calls[
                "check_valid_creds"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.check_valid_creds,
                default_retry=self._method_configs["CheckValidCreds"].retry,
                default_timeout=self._method_configs["CheckValidCreds"].timeout,
                client_info=self._client_info,
            )

        request = datatransfer_pb2.CheckValidCredsRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["check_valid_creds"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
