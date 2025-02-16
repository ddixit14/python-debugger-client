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
# Generated code. DO NOT EDIT!
#
# Snippet for DeleteBreakpoint
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-debugger-client


# [START clouddebugger_v2_generated_Debugger2_DeleteBreakpoint_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import debugger_v2


async def sample_delete_breakpoint():
    # Create a client
    client = debugger_v2.Debugger2AsyncClient()

    # Initialize request argument(s)
    request = debugger_v2.DeleteBreakpointRequest(
        debuggee_id="debuggee_id_value",
        breakpoint_id="breakpoint_id_value",
        client_version="client_version_value",
    )

    # Make the request
    await client.delete_breakpoint(request=request)


# [END clouddebugger_v2_generated_Debugger2_DeleteBreakpoint_async]
