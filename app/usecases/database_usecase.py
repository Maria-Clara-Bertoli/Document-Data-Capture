from abstractions.database_utilities import drop_database

class DatabaseUsecase:

    """This class is used to delete the SQLite database."""
    
    def calls_database_resources(self):
        """
        Calls resources to delete the SQLite database. 
        """
        drop_database()