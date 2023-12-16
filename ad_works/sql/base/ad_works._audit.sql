create table if not exists {{database}}._audit 
(
    `table` string,
    total_count bigint,
    valid_count bigint,
    invalid_count bigint,
    invalid_ratio double,
    file_path string,
    file_name string,
    file_size bigint,
    file_modification_time timestamp,
    file_block_start bigint,
    file_block_length bigint,
    schema_valid boolean,
    snapshot_date timestamp,
    process_id bigint,
    load_date timestamp
)
USING DELTA
TBLPROPERTIES (
  delta.appendOnly = true
)