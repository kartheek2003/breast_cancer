from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig :
    root_dir : Path
    source_url : str
    local_data_file : Path


@dataclass
class PreProcessing:
    df_pre_dir:Path
    drop_columns : list[str]
    axis : int

@dataclass
class EDAconfig:
    report_path : Path
    df_clean_path : Path
    