from agents import Agent

from instruction.dynamic_instruction import dynamic_instruction
from my_config.gemini_confg import MODEL
from my_tool.assistant_tool import hotel_info_tool

assistant = Agent(
name="HotelAssistant",
instructions=dynamic_instruction,
model=MODEL,
tools=[hotel_info_tool]
)