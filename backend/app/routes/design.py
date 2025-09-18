from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_designs():
    return {"designs": ["Floral", "Arabic", "Indian"]}
