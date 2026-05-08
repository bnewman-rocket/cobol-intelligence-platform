from fastapi import APIRouter
from app.services.analysis_service import analyze

router = APIRouter()

@router.get("/")
def health_check():
    return {"status": "running"}

# @router.post("/analyze/system")
# def analyze_system(programs: list[str]):
#     return analyze(programs)

@router.post("/analyze/system")
def analyze_system(directory: str):
    return analyze(directory)