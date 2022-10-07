from fastapi import APIRouter

router = APIRouter(prefix='/line', tags=['lines'])

@router.get("/fn")
async def line_fn():
    return {"kpi_name": "Line FN", "message":"Hello world"}