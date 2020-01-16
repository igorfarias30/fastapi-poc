from models import ItemModel, ItemModelResponse
from typing import List, Dict, Any, Optional
from data import TODO, StatusOptions
from fastapi import APIRouter

todo = TODO()
router = APIRouter()


@router.get("/", response_model=List[ItemModelResponse], tags=["todo"])
def todo_list(status: Optional[StatusOptions]=None):
    """
    View that return a list of todo's
    """
    if status is not None:
        return todo.filter_(status=status)
    return todo.to_list()

@router.get("/{id_item}", response_model=ItemModelResponse)
def todo_list_by_id(id_item: int):
    """
    View that return a item to do by id
    """
    return todo.get_by_id(id_item)

@router.post("/", response_model=ItemModelResponse, status_code=201, tags=["todo"])
def new_todo(insert_item: ItemModel):
    """
    Insert a new To Do in a list
    """
    return todo.insert(insert_item.dict())

