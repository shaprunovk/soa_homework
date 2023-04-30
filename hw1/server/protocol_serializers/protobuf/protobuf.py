import train_pb2
from google.protobuf.json_format import ParseDict
from base_serializer import BaseSerializer
from overrides import override


class ProtobufSerializer(BaseSerializer):
    @override
    def serialize(self, data):
        scheme = train_pb2.Train()
        ParseDict(data, scheme)
        return scheme.SerializeToString()

    @override
    def deserialize(self, data):
        deserialized = train_pb2.Train()
        deserialized.ParseFromString(data)
        return deserialized

