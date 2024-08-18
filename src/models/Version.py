from dataclasses import dataclass

@dataclass
class Version:
    name: str
    version: str
    version_type: str
    changelog: str