put_user = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "job": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "updatedAt": {
            "type": "string"
        }
    },
    "required": [
        "job",
        "name",
        "updatedAt"
    ]
}
