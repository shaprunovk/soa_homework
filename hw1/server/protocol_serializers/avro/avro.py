import fastavro
from io import BytesIO
from avro.schema import parse
from base_serializer import BaseSerializer
from overrides import override


SCHEMA = {
  "type": "record",
  "name": "Train",
  "fields": [
    {"name": "name", "type": "string"},
    {"name": "materials", "type": {"type": "array", "items": "string"}},
    {"name": "passagire_count", "type": {"type": "map", "values": "int"}},
    {"name": "wagon_count", "type": "int"},
    {"name": "length", "type": "float"}
  ]
}


class AvroSerializer(BaseSerializer):
    @override
    def serialize(self, data):
        bytes_writer = BytesIO()
        fastavro.schemaless_writer(bytes_writer, SCHEMA, data)
        return bytes_writer.getvalue()

    @override
    def deserialize(self, data):
        bytes_writer = BytesIO()
        bytes_writer.write(data)
        bytes_writer.seek(0)
        return fastavro.schemaless_reader(bytes_writer, SCHEMA)

