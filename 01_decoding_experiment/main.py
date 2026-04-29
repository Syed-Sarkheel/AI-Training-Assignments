import requests

temps = [0.1, 0.5, 1.0]
prompt = "Write a startup idea for students."

def ask(prompt, temp):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "tinyllama",
            "prompt": prompt,
            "temperature": temp,
            "stream": False
        },
        timeout=120
    )
    r.raise_for_status()
    return r.json()["response"]

results = []

for t in temps:
    print(f"Running temperature {t}...")
    try:
        output = ask(prompt, t)
        results.append((t, output.strip()))
        print("Done.")
    except Exception as e:
        results.append((t, f"ERROR: {e}"))
        print("Failed.")

with open("01_decoding_experiment/results.md", "w") as f:
    f.write("# Decoding Experiment Results\n\n")
    f.write("| Temperature | Output |\n")
    f.write("|------------|--------|\n")

    for t, out in results:
        clean = out.replace("\n", " ").replace("|", "/")
        f.write(f"| {t} | {clean[:500]} |\n")

print("Saved results.md")