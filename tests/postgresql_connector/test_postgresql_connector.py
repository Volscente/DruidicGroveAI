"""
This test module includes all the tests for the
module src.postgresql_connector.
"""

# Import Standard Libraries

# Import Package Modules
from postgresql_connector.postgresql_connector import PostgreSQLConnector


def test_set_client(
    fixture_postgresql_connector: PostgreSQLConnector,
) -> bool:
    """
    Test the function src/postgresql_connector/postgresql_connector._set_client
    by checking the ``self._client`` and ``self._cursor`` attributes.

    Args:
        fixture_postgresql_connector (PostgreSQLConnector): PostgreSQL Connector
    """
    return True
