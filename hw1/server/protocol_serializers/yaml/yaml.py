import yaml
from base_serializer import BaseSerializer
from overrides import override


class YamlSerializer(BaseSerializer):
    @override
    def serialize(self, data):
        return yaml.dump(data)

    @override
    def deserialize(self, data):
        return yaml.load(data, Loader=yaml.Loader)
