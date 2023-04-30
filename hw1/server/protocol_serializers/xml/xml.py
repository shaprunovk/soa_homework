from base_serializer import BaseSerializer
from overrides import override
from xml_marshaller import xml_marshaller


class XmlSerializer(BaseSerializer):
    @override
    def serialize(self, data):
        return xml_marshaller.dumps(data)

    @override
    def deserialize(self, data):
        return xml_marshaller.loads(data)

