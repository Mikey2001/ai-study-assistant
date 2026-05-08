from agent import Agent

agent = Agent()

user_input = input("Enter your question: ")
response = agent.run(user_input)

print(response)
