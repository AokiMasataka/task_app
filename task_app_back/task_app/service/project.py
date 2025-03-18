from uuid import UUID
from .utils import DatabaseConnector
from ..schemas import Project


def create(project: Project) -> None:
    query = """
    INSERT INTO projects
        (id, title, description, created_at, updated_at)
    VALUES
        (%s, %s, %s, %s, %s)
    """
    values = (
        project.id,
        project.title,
        project.description,
        project.created_at,
        project.updated_at
    )

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)


def get_all() -> list[dict]:
    query = """
    SELECT
        id, title, description, created_at, updated_at
    FROM
        projects
    """

    with DatabaseConnector() as cur:
        cur.execute(query=query)
        rows = cur.fetchall()

    projects = [dict(row) for row in rows]

    return projects

def get(project_id: UUID) -> dict:
    query = """
    SELECT
        id, title, description, created_at, updated_at
    FROM
        projects
    WHERE
        id = %s
    """
    values = (project_id,)

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)
        row = cur.fetchone()

    project = dict(row)
    return project

def update(project: Project) -> None:
    query = """
    UPDATE
        projects
    SET
        title = %s,
        description = %s,
        updated_at = %s
    WHERE
        id = %s
    """
    values = (
        project.title,
        project.description,
        project.updated_at,
        project.id
    )

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)

def delete(project_id: UUID) -> None:
    query = """
    DELETE FROM
        projects
    WHERE
        id = %s
    """
    values = (project_id, )

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)
