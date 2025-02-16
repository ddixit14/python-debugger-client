# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
from typing import Dict, Type

from .base import Debugger2Transport
from .grpc import Debugger2GrpcTransport
from .grpc_asyncio import Debugger2GrpcAsyncIOTransport
from .rest import Debugger2RestInterceptor, Debugger2RestTransport

# Compile a registry of transports.
_transport_registry = OrderedDict()  # type: Dict[str, Type[Debugger2Transport]]
_transport_registry["grpc"] = Debugger2GrpcTransport
_transport_registry["grpc_asyncio"] = Debugger2GrpcAsyncIOTransport
_transport_registry["rest"] = Debugger2RestTransport

__all__ = (
    "Debugger2Transport",
    "Debugger2GrpcTransport",
    "Debugger2GrpcAsyncIOTransport",
    "Debugger2RestTransport",
    "Debugger2RestInterceptor",
)
