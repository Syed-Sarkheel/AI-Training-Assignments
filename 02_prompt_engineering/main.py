from utils.ollama_helper import ask_ollama

# ---------------- PROMPTS ----------------
zero_prompt = "What is REST API?"

few_prompt = """
Q: What is HTTP?
A: A protocol used for communication on the web.

Q: What is REST API?
"""

role_prompt = "Explain REST API to a beginner developer."

json_prompt = """
Give response only in JSON:

{
  "definition": "",
  "benefits": [],
  "examples": []
}

Topic: REST API
"""

# ---------------- RUN MODEL ----------------
print("Running Zero-shot...")
zero_output = ask_ollama(zero_prompt)

print("Running Few-shot...")
few_output = ask_ollama(few_prompt)

print("Running Role Prompt...")
role_output = ask_ollama(
    role_prompt,
    system="You are a senior backend engineer who explains concepts clearly."
)

print("Running JSON Prompt...")
json_output = ask_ollama(json_prompt)

# ---------------- SAVE FILE ----------------
file_path = "02_prompt_engineering/results.md"

with open(file_path, "w") as f:
    f.write("# Prompt Engineering Results\n\n")
    f.write("This assignment compares multiple prompting strategies and how they change model behavior.\n\n")
    f.write("---\n\n")

    # ZERO SHOT
    f.write("## Zero-Shot Prompting\n\n")
    f.write("### Prompt Used\n\n```text\n")
    f.write(zero_prompt)
    f.write("\n```\n\n")

    f.write("### Model Response\n\n```text\n")
    f.write(zero_output.strip())
    f.write("\n```\n\n")

    f.write("### Notes\n\n")
    f.write("- No examples or context were given.\n")
    f.write("- Useful for quick general questions.\n\n")
    f.write("---\n\n")

    # FEW SHOT
    f.write("## Few-Shot Prompting\n\n")
    f.write("### Prompt Used\n\n```text\n")
    f.write(few_prompt.strip())
    f.write("\n```\n\n")

    f.write("### Model Response\n\n```text\n")
    f.write(few_output.strip())
    f.write("\n```\n\n")

    f.write("### Notes\n\n")
    f.write("- Prior examples guide answer style.\n")
    f.write("- Better consistency than zero-shot.\n\n")
    f.write("---\n\n")

    # ROLE
    f.write("## Role Prompting\n\n")
    f.write("### Prompt Used\n\n```text\n")
    f.write("System: You are a senior backend engineer.\n")
    f.write(role_prompt)
    f.write("\n```\n\n")

    f.write("### Model Response\n\n```text\n")
    f.write(role_output.strip())
    f.write("\n```\n\n")

    f.write("### Notes\n\n")
    f.write("- Role affects tone and explanation depth.\n")
    f.write("- Good for expert guidance or teaching.\n\n")
    f.write("---\n\n")

    # JSON
    f.write("## Structured Output (JSON)\n\n")
    f.write("### Prompt Used\n\n```text\n")
    f.write(json_prompt.strip())
    f.write("\n```\n\n")

    f.write("### Model Response\n\n```json\n")
    f.write(json_output.strip())
    f.write("\n```\n\n")

    f.write("### Notes\n\n")
    f.write("- Easier to parse in applications.\n")
    f.write("- Useful for APIs, automations, dashboards.\n\n")
    f.write("---\n\n")

    # SUMMARY TABLE
    f.write("## Summary Comparison\n\n")
    f.write("| Method | Strength | Best Use |\n")
    f.write("|-------|----------|----------|\n")
    f.write("| Zero-shot | Fast and simple | Basic Q&A |\n")
    f.write("| Few-shot | Pattern following | Repetitive tasks |\n")
    f.write("| Role Prompting | Better tone/context | Teaching / Expertise |\n")
    f.write("| JSON Output | Structured data | Production apps |\n\n")

    f.write("---\n\n")

    f.write("## Final Thoughts\n\n")
    f.write("Prompt engineering improves reliability and usefulness of LLM outputs. "
            "Small prompt changes can strongly influence quality, format, and relevance.\n")

print(f"Saved {file_path}")