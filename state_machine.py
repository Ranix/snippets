
# State machine project, base on the graph:  https://etaluma.atlassian.net/wiki/spaces/ICF/pages/43253884/Device+Servers?preview=/43253884/117342326/image2019-7-15_8-17-55.png


class State(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self):
        print('Processing current state:', str(self))

    def on_event(self, event):
        """
        Handle events that are delegated to this State.
        """
        pass

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__


# States
class InitState(State):
    """
    The state which indicates that there are limited device capabilities.
    """

    def on_event(self, event):
        if event == 'initialized':
            return ReadyState()

        if event == 'not_ready':
            return ErrorState()

        return self


class ReadyState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """

    def on_event(self, event):
        if event == 'start':
            return BusyState()

        if event == 'not_ready':
            return ErrorState()

        return self


class BusyState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """

    def on_event(self, event):
        if event == 'finish':
            return ReadyState()

        if event == 'error':
            return ErrorState()

        return self


class ErrorState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """

    def on_event(self, event):
        if event == 'clear':
            return ReadyState()

        return self


# State Machine
class DeviceServer(object):
    """ 
    A simple state machine that mimics the functionality of a device from a 
    high level.
    """

    def __init__(self):
        """ Initialize the components. """
        # Start with a default state.
        self.state = InitState()

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """
        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)

    def __str__(self):
        return str(self.state)
