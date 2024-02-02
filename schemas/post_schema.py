post_user = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "id": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "job",
        "name",
        "createdAt"
    ]
}
