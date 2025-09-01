from agents import RunContextWrapper


def dynamic_instruction(ctx:RunContextWrapper, agent):
 return f"User {ctx.context.get('name','Guest')}, you are a helpful assistant for hotel information."


async def allow_all(ctx:RunContextWrapper, agent):
 return True