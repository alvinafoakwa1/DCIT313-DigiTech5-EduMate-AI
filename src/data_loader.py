from pathlib import Path

def load_and_chunk_notes(file_path="data/sample_db_notes.txt"):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Notes file not found: {file_path}")
    text = path.read_text(encoding="utf-8").strip()
    chunks = [block.strip() for block in text.split("\n\n") if block.strip()]
    return chunks

if __name__ == "__main__":
    chunks = load_and_chunk_notes()
    print(f"Successfully loaded {len(chunks)} topic chunks from sample notes.")
    for idx, c in enumerate(chunks, 1):
        first_line = c.splitlines()[0]
        print(f"  Chunk {idx}: {first_line}")
