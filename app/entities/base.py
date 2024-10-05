from datetime import datetime

from pydantic import BaseModel


class AuditBaseModel(BaseModel):
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
    created_by: str | None = None
    updated_by: str | None = None
    deleted_by: str | None = None
