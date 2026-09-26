from dataclasses import dataclass


@dataclass
class TextChunk:
    text: str
    page_number: int
    section: str | None
    chunk_index: int


class SemanticChunker:
    """
    Create overlapping text chunks while preserving page and section metadata.

    This is the baseline chunking implementation.
    """

    def __init__(
        self,
        chunk_size: int = 1200,
        chunk_overlap: int = 200,
    ):
        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_page(
        self,
        text: str,
        page_number: int,
        section: str | None = None,
        starting_index: int = 0,
    ) -> list[TextChunk]:

        text = text.strip()

        if not text:
            return []

        chunks = []
        start = 0
        chunk_index = starting_index

        while start < len(text):
            end = min(
                start + self.chunk_size,
                len(text),
            )

            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append(
                    TextChunk(
                        text=chunk_text,
                        page_number=page_number,
                        section=section,
                        chunk_index=chunk_index,
                    )
                )

                chunk_index += 1

            if end >= len(text):
                break

            start = end - self.chunk_overlap

        return chunks