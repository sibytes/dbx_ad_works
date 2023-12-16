create table if not exists {{ database }}.{{ table }} 
(
    {{ columns }},
    _corrupt_record string null,
    _process_id bigint not null,
    _snapshot_date timestamp not null,
    _file_name string,
    _process_id bigint,
    _from_date date not null,
    _to_date date not null,
    _is_current boolean not null
)
USING DELTA
TBLPROPERTIES (
    delta.enableChangeDataFeed = true
)