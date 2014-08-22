## Copyright 2014 Cognitect. All Rights Reserved.
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS-IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

from cmarshaler import JsonMarshaler, VerboseJsonMarshaler, MsgPackMarshaler

class Writer(object):
    """The top-level object for writing out Python objects and converting them
    to Transit data.  During initialization, you must specify the protocol used
    for marshalling the data- json or msgpack.  You must also specify the io
    source used for writing (a file descriptor).  You may optionally pass in
    an options dictionary that will be forwarded onto the Marshaler.
    The cache is enabled by default.
    """
    def __init__(self, io, protocol="json", opts={"cache_enabled": True}):
        if protocol == "json":
            self.marshaler = JsonMarshaler(io, opts=opts)
        elif protocol == "json_verbose":
            self.marshaler = VerboseJsonMarshaler(io, opts=opts)
        else:
            self.marshaler = MsgPackMarshaler(io, opts=opts)

    def write(self, obj):
        """Given a Python object, marshal it into Transit data and write it to
        the 'io' source.
        """
        self.marshaler.marshal_top(obj)

    def register(self, obj_type, handler_class):
        """Register custom converters for object types present in your
        application.  This allows you to extend Transit to encode new types.
        You must specify the obj type to be encoded, and the handler class
        that should be used by the Marshaler during write-time.
        """
        self.marshaler.register(obj_type, handler_class)
