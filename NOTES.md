# Design notes — quaslide

- Chosen word: quaslide. Portmanteau of "quasi" + "slide".
- Meaning: the frozen mid-recline pose a laggy video call leaves you in.
- The usage line ("I was quasliding, I swear I agreed") gives it a voice and a
  relatable moment instead of a dictionary-only definition.
- Entry text is 137 characters, inside the 140 limit.
- main.py stays a plain writer: entry text to $OUTPUT_DIR/entry.txt (default
  /output) so the grader's reproduce step works unchanged.
