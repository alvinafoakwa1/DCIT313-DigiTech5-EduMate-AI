import json
from pathlib import Path
from src.data_loader import load_and_chunk_notes


def baseline_answer(query: str, chunks: list[str]) -> str:
    """Simple keyword-overlap baseline without similarity thresholding or abstention."""
    query_words = {w.lower().strip("?.,!") for w in query.split() if len(w) > 3}
    best_chunk = chunks[0] if chunks else ""
    best_score = -1

    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        overlap = len(query_words.intersection(chunk_words))
        if overlap > best_score:
            best_score = overlap
            best_chunk = chunk

    preview = " ".join(best_chunk.splitlines()[:2])
    return f"[BASELINE ANSWER] Based on notes: {preview}"


def run_evaluation(
    queries_path: str = "evaluation/queries_draft.json",
    notes_path: str = "data/sample_db_notes.txt",
) -> None:
    chunks = load_and_chunk_notes(notes_path)
    queries = json.loads(Path(queries_path).read_text(encoding="utf-8"))

    print(f"Running baseline on {len(queries)} queries...\n")
    for item in queries:
        qid = item.get("id", "?")
        q_text = item.get("query", "")
        expected = item.get("expected_behavior", "")
        output = baseline_answer(q_text, chunks)
        print(f"{qid} ({expected}): {q_text}")
        print(f"  -> {output}\n")


if __name__ == "__main__":
    run_evaluation()