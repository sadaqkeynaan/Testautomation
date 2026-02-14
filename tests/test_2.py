def test_file_content_exact():
    """Kontrollerar att filens innehåll exakt matchar 'what a great day!'"""
    with open("test_data/day.txt", "r") as f:
        content = f.read().strip()
    print(f"File content: {content}")
    assert content == "What a great day!"

def test_file_content_length():
    """Kontrollerar att längden på texten i filen är korrekt"""
    with open("test_data/day.txt", "r") as f:
        content = f.read().strip()
    print(f"Length of file content: {len(content)}")
    assert len(content) == len("What a great day!")
