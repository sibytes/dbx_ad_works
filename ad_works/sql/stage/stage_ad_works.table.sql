create table if not exists {{ database }}.{{ table }} 
(
    _corrupt_record string null,
    _process_id bigint not null,
    _snapshot_date timestamp not null,
    _file_path string,
    _file_name string,
    _file_size bigint,
    _file_modification_time timestamp,
    _file_block_start bigint,
    _file_block_length bigint
)
USING DELTA
TBLPROPERTIES (
  delta.appendOnly = true
)