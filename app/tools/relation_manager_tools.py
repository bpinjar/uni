
from typing import Dict, Any, Callable

from functions.relation_manager import fix_appointment_with_rm, get_rm_details

fix_appointment_with_rm_tool = {
    'type': 'function',
    'function': {
        'name': 'fix_appointment_with_rm',
        'description': "Schedules an appointment with the Relationship Manager",
        'parameters': {
            'type': 'object',
            'required': ['user_id', 'date_time'],
            'properties': {
                'user_id': {'type': 'string', 'description': 'Unique identifier of the user'},
                'date_time': {'type': 'string', 'description': 'Requested date and time for the appointment'},
            },
        },
    },
}

get_rm_details_tool = {
    'type': 'function',
    'function': {
        'name': 'get_rm_details',
        'description': "Fetches details of the user's Relationship Manager",
        'parameters': {
            'type': 'object',
            'required': ['user_id'],
            'properties': {
                'user_id': {'type': 'string', 'description': 'Unique identifier of the user'},
            },
        },
    },
}
 
relationship_functions: Dict[str, Callable] = {    
    'fix_appointment_with_rm': fix_appointment_with_rm,
    'get_rm_details': get_rm_details,
}

relationship_tools = [fix_appointment_with_rm_tool, get_rm_details_tool]