import os,sys
from dataclasses import dataclass
from pathlib import  Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    zip_path: Path
    unzip_path: Path
    raw_data: Path