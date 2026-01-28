from fastapi import Depends

from infra import get_db_session


DBSessionDeps = Depends(get_db_session)