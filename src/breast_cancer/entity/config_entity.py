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
    

@dataclass
class DataTransform:
    df_path : Path
    # transformed_df_path : Path
    test_size : float
    random_state : int
    smote_k_neighbours :int
    n_pca_components: int
    scaler_path : Path
    # pca_model_path : Path

@dataclass 
class ModelBuilding:
    cv : int
    random_state : int
    n_iter : int
    n_jobs : int
    model_save_path : str
    report_save_path : str