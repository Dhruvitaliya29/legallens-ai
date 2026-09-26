import os
from pathlib import Path

import pytest

from app.ingestion.pdf_loader import PDFLoader


@pytest.mark.skipif(
    not os.getenv("TEST_PDF_PATH"),
    reason="Set TEST_PDF_PATH to run PDF extraction test.",
)
def test_pdf_loader():
    pdf_path = Path(os.environ["TEST_PDF_PATH"])

    result = PDFLoader().load(pdf_path)

    assert result.filename == pdf_path.name
    assert result.page_count > 0
    assert len(result.pages) == result.page_count

    for page in result.pages:
        assert page.page_number >= 1
        assert "source" in page.metadata
        assert "page" in page.metadata