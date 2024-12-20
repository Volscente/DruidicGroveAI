"""
The module includes Data Preparation class definitions
"""
# Import Standard Libraries

# Import Package Modules

class StackOverflowDataPreparation:
    """
    The class implements a Data Preparation object for the Stack Overflow
    Answer Score Classification use case

    Attributes:
        logger: logging.Logger object used for logging purposes

    Methods:
    """
    def __init__(self,
                 input_tables_config: dict):
        """
        Constructor of the class StackOverflowDataPreparation
        # TODO: Add a BigQueryConnector object

        Args:
            input_tables_config: dict with Input Tables (including raw data) configuration
        """
        # Setup logger
        self.logger = get_logger(__class__.__name__,
                                 Path(os.getenv('DRUIDIC_GROVE_AI_ROOT_PATH')) /
                                 'src' /
                                 'logging_module' /
                                 'log_configuration.yaml')
        pass
    def _load_input_tables(self):
        # TODO_URGENT: Check if we can use BigQueryConnector.read_from_query_config and, if yes, rename it
        # TODO: Switch if the tables already exist, otherwise call BigQueryConnector.
        pass