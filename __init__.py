"""Integration WirenBoard devices."""
"""
The "hello world" custom component.
This component implements the bare minimum that a component should implement.
Configuration:
To use the hello_world component you will need to add the following to your
configuration.yaml file.
hello_world:
"""

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "wiren_board"


def setup(hass, config):
    """Set up a skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.set('wiren_board.Hello_World', 'Works!')

    # Return boolean to indicate that initialization was successfully.
    return True
