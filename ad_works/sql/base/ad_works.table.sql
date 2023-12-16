create table if not exists {{ database }}.{{ table }} 
(
    {{ columns }},
    _snapshot_date timestamp not null,
    _process_id bigint not null,
    _file_name string not null,
    _from_date date not null,
    _to_date date not null default to_date('9999-12-31'),
    _is_current boolean not null
)
USING DELTA
TBLPROPERTIES (
    delta.enableChangeDataFeed = true
)