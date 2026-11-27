"""Entry for u-deranalabs-invent-a-word-we-need."""
import os

ENTRY = "quaslide (n.) - when a laggy video call freezes you mid-lean-back and all stare at your open mouth. 'I was quasliding, I swear I agreed.'"

out = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
