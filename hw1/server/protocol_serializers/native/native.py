import pickle
from base_serializer import BaseSerializer
from overrides import override


class NativeSerializer(BaseSerializer):
    @override
    def serialize(self, data):
        return pickle.dumps(data)

    @override
    def deserialize(self, data):
        return pickle.loads(data)

