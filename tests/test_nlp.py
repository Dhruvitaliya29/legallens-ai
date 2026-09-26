from app.nlp.text_cleaner import TextCleaner
from app.nlp.section_detector import SectionDetector
from app.nlp.chunker import SemanticChunker


def test_text_cleaner():
    text = "Hello   world.\n\n\nThis is a test.   "

    cleaned = TextCleaner.clean(text)

    assert cleaned == "Hello world.\n\nThis is a test."


def test_section_detector():
    text = """
    INTRODUCTION

    1. LIABILITY

    The parties agree to the following.

    SECTION 2 PAYMENT

    Payment shall be made within thirty days.
    """

    sections = SectionDetector().detect(text)

    titles = [section["title"] for section in sections]

    assert "INTRODUCTION" in titles
    assert "1. LIABILITY" in titles
    assert "SECTION 2 PAYMENT" in titles


def test_chunker():
    text = "A" * 2500

    chunks = SemanticChunker(
        chunk_size=1000,
        chunk_overlap=100,
    ).chunk_page(
        text=text,
        page_number=3,
        section="Liability",
    )

    assert len(chunks) > 1

    assert chunks[0].page_number == 3
    assert chunks[0].section == "Liability"
    assert chunks[0].chunk_index == 0

    assert all(chunk.text for chunk in chunks)