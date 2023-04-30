import json
from base_serializer import BaseSerializer
from overrides import override


class JsonSerializer(BaseSerializer):
    @override
    def serialize(self, data):
        return json.dumps(data)

    @override
    def deserialize(self, data):
        return json.loads(data)

