from pydantic import BaseModel
from typing import Optional, Union, List
from queries.pool import pool

class ProjectIn(BaseModel):
    title: str
    img_url: Optional[str]
    description: str
    github_url: Optional[str]
    live_url: Optional[str]


class ProjectOut(BaseModel):
    id: int
    title: str
    img_url: Optional[str]
    description: str
    github_url: Optional[str]
    live_url: Optional[str]


class Error(BaseModel):
    message: str

class ProjectRepository:
    def get_all(self) -> Union[Error, List[ProjectOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                            title,
                            img_url,
                            description,
                            github_url,
                            live_url
                        FROM projects
                        ORDER BY
                        """
                    )
                    result = []
                    for project in db:
                        project = ProjectOut(
                            id=project[0],
                            title=project[1],
                            img_url=project[2],
                            description=project[3],
                            github_url=project[4],
                            live_url=project[5]
                        )
                        result.append(project)
                    return result
        except Exception as e:
            print(e)
            return {"message": "Something went wrong!"}
