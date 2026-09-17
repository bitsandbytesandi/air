from .models import Tool


MEMORY_SEARCH_TOOL = Tool(
    id="memory_search",
    name="Memory Search",
    description="Search stored AIR memories using a text query.",
    input_schema={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
            },
        },
        "required": [
            "query",
        ],
    },
)
