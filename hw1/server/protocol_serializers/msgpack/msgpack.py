import msgpack
from base_serializer import BaseSerializer
from overrides import override


class MsgPackSerializer(BaseSerializer):
    @override
    def serialize(self, data):
        return msgpack.dumps(data)

    @override
    def deserialize(self, data):
        return msgpack.loads(data)

