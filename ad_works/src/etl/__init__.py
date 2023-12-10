from ._logging import configure_logging
configure_logging()

from ._table import Table
from ._table_factory import get_table
__version__ = "0.0.1"

__all__ = ["Table", "get_table"]
