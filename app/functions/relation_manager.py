
from vector_db.query_engine import query_vector_db

##############################################################################################################
# Relationship
def fix_appointment_with_rm( user_id, date_time):
    """Schedules an appointment with the Relationship Manager."""
    return f"Appointment scheduled with RM for user {user_id} on {date_time}."

def get_rm_details( user_id):
    ret = query_vector_db("what are Safe custodiy deposits ?")
    print(ret)
    """Returns Relationship Manager details for the given user."""
    return f"Fetching Relationship Manager details for user {user_id}."
