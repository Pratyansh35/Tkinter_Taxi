with open("records.text", "w") as f:
        f.write(f"({regvalue.get()}, {namevalue.get()}, {phonevalue.get()}, {emailvalue.get()})")