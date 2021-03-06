# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
from datetime import datetime
from getpass import getpass
import googlemaps
from googlemaps import Client

# (API key) : Google maps API key
GOOGLE_MAP_API_KEY = ''

def get_direction( 
            api_key,
            from_address, 
            to_address, 
            travelling_mode
        ):
    """Returns all the direction informations between two points

    Arguments:
        - api_key         : (str) googlemaps API key
        - from_address    : (str) departure location
        - to_address      : (str) arrival location
        - travelling_mode : (str) conveyance

    Returns:
        - client.directions(...) : (list) information 
                                          about the journey
    """
    client = Client(api_key)
    return client.directions(
                from_address, 
                to_address,
                mode = travelling_mode,
                departure_time = datetime.now()
            )

def get_direction_time(direction, travelling_mode):
    """Get the duration of the journey

    Arguments:
        - direction      : (list) information about the journey
        - travelling_mode: (str) conveyance

    Returns:
        - time : (str) duration of the journey
    """
    time = None
    if travelling_mode == 'driving':
        time = \
            direction[0]['legs'][0]['duration_in_traffic']['text']
    else:
        time = \
            direction[0]['legs'][0]['duration']['text']
    return time

def main() :
    api_key = GOOGLE_MAP_API_KEY
    from_address   = ''
    to_address     = ''
    travelling_mode = ''
    message = '\nPlease select your travelling mode: \n'
    message+= '(driving, walking, bicycling): '

    if not api_key:
        api_key = getpass('Enter your API Key: ')
    while not from_address:
        from_address = input('\nBeginning of the journey: ')
    while not to_address:
        to_address = input('\nArrival of the journey: ')
    while travelling_mode not in ['bicycling', 'driving', 'walking']:
        travelling_mode = input(message)

    direction = get_direction(
                    api_key,
                    from_address, 
                    to_address, 
                    travelling_mode
                )
    
    time_to_destination = get_direction_time(direction, travelling_mode)

    print("\nIt will take %s to travel from %s to %s." \
            % (time_to_destination, from_address, to_address))

if __name__ == '__main__':
    main()
