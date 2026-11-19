from typing import List, Literal
from pydantic import BaseModel, Field

class DefectItem(BaseModel):
    defect_class: str = Field(..., description="Detected defect category")
    confidence: float = Field(..., ge=0.0, le=1.0)
    bbox: List[float] = Field(..., min_length=4, max_length=4)

class InspectionResponse(BaseModel):
    job_id: str
    qa_status: Literal["PASS", "FAIL"]
    defects: List[DefectItem]
