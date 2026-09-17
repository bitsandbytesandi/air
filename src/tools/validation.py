from .models import Tool


class ToolArgumentValidator:
    def validate(
        self,
        tool: Tool,
        arguments: dict,
    ) -> None:
        schema = tool.input_schema

        if schema.get("type") != "object":
            raise ValueError(
                f"Unsupported input schema for tool: {tool.id}"
            )

        properties = schema.get("properties", {})
        required = schema.get("required", [])

        for name in required:
            if name not in arguments:
                raise ValueError(
                    f"Missing required argument: {name}"
                )

        for name in arguments:
            if name not in properties:
                raise ValueError(
                    f"Unknown argument: {name}"
                )

        for name, value in arguments.items():
            expected_type = properties[name].get("type")

            if expected_type == "string" and not isinstance(value, str):
                raise ValueError(
                    f"Argument '{name}' must be a string."
                )
