
from vector_db.query_engine import query_vector_db
##############################################################################################################
# Banking Information
def get_fd_rd_rates():
    
    ret = query_vector_db("what are Safe custodiy deposits ?")
    print(ret)
    """Returns the latest FD/RD rates."""
    return "Fetching latest Fixed Deposit and Recurring Deposit rates."

def find_nearest_branch_atm( location):
    """Finds the nearest branch or ATM based on user location."""
    return f"Searching for nearest branch/ATM in {location}."
