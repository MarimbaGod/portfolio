from pydantic import BaseModel
from typing import Optional, Union, List
from queries.pool import pool


class Project(BaseModel):
    title: str
    img_url: Optional[str]
    description: str
    github_url: str
    live_url: Optional[str]


class ProjectInDB(Project):
    id: int

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

    def add_project(self, project: Project) -> ProjectInDB:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO project
                            (title,
                            img_url,
                            description,
                            github_url,
                            live_url)
                        VALUES
                            (%s, %s, %s, %s, %s)
                        RETURNING *;
                        """,
                        [
                            project.title,
                            project.img_url,
                            project.description,
                            project.github_url,
                            project.live_url,
                        ],
                    )
                    project_data = result.fetchone()
                    return ProjectInDB(**project_data)
        except Exception as e:
            print(e)
            return {"message": "Couldn't add the project"}
