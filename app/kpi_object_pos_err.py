from fastapi import APIRouter

router = APIRouter(prefix='/object', tags=['objects'])

@router.get('/pos/err')
async def object_pos_err():
    return {"KPI name": "Object Pos Error", "message": "Hello world"}
