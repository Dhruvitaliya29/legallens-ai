from fastapi import FastAPI

app = FastAPI(
    title="LegalLens AI",
    description="AI-powered legal document analysis and grounded question answering",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "LegalLens AI",
    }