from agents import FunctionTool, RunContextWrapper

from instruction.dynamic_instruction import allow_all


async def hotel_info_func(ctx:RunContextWrapper, arg):
	hotel_name = arg.lower().strip()
	hotels = ctx.context.get("hotels", [])
	for h in hotels:
		if h["name"].lower() == hotel_name:
			return (
				f"Hotel {h['name']} in {h['location']} costs ${h['price']} per night "
				f"and has a rating of {h['rating']} stars."
			)
	return f"Sorry, I couldn’t find a hotel named '{hotel_name}'."


hotel_info_tool = FunctionTool(
name="get_hotel_info",
description="Retrieve details for a given hotel by name.",
params_json_schema={"type": "string", "description": "Hotel name"},
on_invoke_tool=hotel_info_func,
is_enabled=allow_all
)