from ._logging import configure_logging
configure_logging()

from ._table import BatchTable
from ._table import AutoloaderTable
from ._base_table import BaseTable
from ._table_factory import get_table

__version__ = "0.0.1"

__all__ = ["Table", "get_table"]
