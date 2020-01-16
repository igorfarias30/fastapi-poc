from pydantic import BaseModel
from typing import Optional
from data import StatusOptions


class ItemModel(BaseModel):
    title: str
    description: Optional[str] = ""
    status: Optional[str] = StatusOptions.to_do


class ItemModelResponse(ItemModel):
    id: int