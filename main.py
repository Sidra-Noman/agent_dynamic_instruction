from agents import set_tracing_disabled
set_tracing_disabled(True)
from agents import Runner
from my_agent.assistant import assistant

if __name__ == "__main__":
	
	# Store multiple hotels in context
	hotels_data = [
		{"name": "Grand Plaza", "location": "New York", "price": 250, "rating": 4.5},
		{"name": "Ocean View", "location": "Miami", "price": 180, "rating": 4.2},
		{"name": "Mountain Retreat", "location": "Denver", "price": 200, "rating": 4.7},
	]

	res = Runner.run_sync(
		starting_agent=assistant,
		input="Can you tell me about the Grand Plaza hotel?",
		context={"name": "Atma ram", "age": 30, "role": "traveler", "hotels": hotels_data}
	)

	print(res.final_output)