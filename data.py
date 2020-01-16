from typing import List, Dict, Any, Optional, Union
from enum import Enum


class StatusOptions(str, Enum):
    to_do = "To Do"
    doing = "Doing"
    done = "Done"


Item = Dict[str, Union[int, str, StatusOptions]]


class TODO:
    """
    A list of todo
    """

    todo: List[Item] = [
        {
            "id": 1, 
            "title": "Make a live", 
            "description": "Make a live Edu channel", 
            "status": StatusOptions.to_do
        },
        {"id": 2, "title": "Streaming", "status": StatusOptions.done},
        {"id": 3, "title": "Create a API with FastAPI", "status": StatusOptions.doing}
    ]
    id_atual = 3

    def to_list(self):
        return self.todo

    def insert(self, item: Dict[str, Any]) -> Item:
        self.id_atual += 1
        item["id"] = self.id_atual
        self.todo.append(item)
        return item

    def get_by_id(self, id_item: int) ->  Item:
        item = filter(lambda x: x["id"] == id_item, self.todo)
        return item

    def filter_(self, status: StatusOptions) -> List[Item]:
        return list(filter(lambda x: x["status"] == status, self.todo))