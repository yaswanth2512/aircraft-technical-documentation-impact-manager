from dataclasses import dataclass, field
from typing import List


@dataclass
class TechnicalManual:
    manual_type: str   # AMM, IPC, TSM
    ata_chapter: str
    revision: int
    effectivity: str
    compliance_status: str
    traceability_log: List[str] = field(default_factory=list)

    def update_revision(self, change_id: str):
        self.revision += 1
        self.traceability_log.append(change_id)
        self.compliance_status = "Pending Validation"

    def __str__(self):
        return (f"{self.manual_type} | ATA {self.ata_chapter} | "
                f"Rev {self.revision} | Effectivity: {self.effectivity} | "
                f"Compliance: {self.compliance_status}")
