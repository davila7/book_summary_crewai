from crewai import Agent, Task, Crew
import os

# Define your agents
book_summarizer = Agent(
    role="Book Summarizer",
    goal="Summarize the book provided by the user",
    backstory="An expert in summarizing books into concise summaries",
    verbose=True
)

summary_simplifier = Agent(
    role="Summary Simplifier",
    goal="Simplify the summary and format it into markdown",
    backstory="A specialist in simplifying text and formatting it into markdown",
    verbose=True
)

# Define your tasks
summarize_book = Task(
    description="Summarize the book provided by the user",
    expected_output="A concise summary of the book",
    agent=book_summarizer
)

simplify_and_format_summary = Task(
    description="Simplify the summary and format it into markdown",
    expected_output="A simplified and markdown-formatted summary",
    agent=summary_simplifier,
    context=[summarize_book]
)

# Create the crew
crew = Crew(
    agents=[book_summarizer, summary_simplifier],
    tasks=[summarize_book, simplify_and_format_summary],
    verbose=True,
    planning=True
)

# Execute the crew
result = crew.kickoff()

# Save the formatted summary to a file
summary = result.tasks[1].output
os.makedirs('summaries', exist_ok=True)
with open('summaries/summary.md', 'w') as f:
    f.write(summary)
