from pathlib import Path

import pymupdf

from app.ingestion.models import DocumentContent, PageContent


class PDFLoader:
    """Extract page-aware text from PDF documents."""

    def load(self, file_path: str | Path) -> DocumentContent:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"PDF not found: {path}")

        if path.suffix.lower() != ".pdf":
            raise ValueError("Input file must be a PDF.")

        document = pymupdf.open(path)

        pages: list[PageContent] = []

        for page_index, page in enumerate(document):
            text = page.get_text("text").strip()

            pages.append(
                PageContent(
                    page_number=page_index + 1,
                    text=text,
                    metadata={
                        "source": path.name,
                        "page": page_index + 1,
                    },
                )
            )

        result = DocumentContent(
            filename=path.name,
            file_path=path,
            page_count=len(document),
            pages=pages,
            metadata={
                "source": path.name,
                "file_type": "application/pdf",
            },
        )

        document.close()

        return result