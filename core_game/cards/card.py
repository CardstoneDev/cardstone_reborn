import abc
class Card(abc):

    def __init__(self,preprocessors : dict[EventType, EventPreprocessor],
                 responders : dict[EventType, EventResponder]):
        self.preprocessors = preprocessors
        self.responders = responders


    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_image(self) -> str:
        """
        returns the relative path to the image as a string
        """
        pass

    @abc.abstractmethod
    def get_text(self) -> str:
        pass

    def preprocess_event(self, event : Event) -> Event:
        """
        Accept an event. Return 
        """
        type = event.type
        if type in self.responders:
            return self.responder[type].respond(event)
        return (False,event)

    def respond_to_event(self, event : Event) -> list[Event]:
        """
        Accept an event. Return a list of new events
        that this card wishes to create and add to the event q.
        This list may be empty.
        """
        type = event.type
        if type in self.responders:
            return self.responder[type].respond(event)
        return []