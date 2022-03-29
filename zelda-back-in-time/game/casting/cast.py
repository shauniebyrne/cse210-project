class Cast:
    """
    The collection of the actors in the code.
    """
    def __init__(self):
        """Creates a new Actor."""
        self._actors = {}
        
    def add_actor(self, group, actor):
        """Adds an actor to the given group.
        
        Args:
            group (string): Name of the group.
            actor (Actor): The actor to add.
        """
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        """Finds the actors we need in the group.
        
        Arg:
            group (string): Name of the group.

        Returns:
            A list (results) of Actor instances.
        """
        results = []

        if group in self._actors.keys():
            results = self._actors[group].copy()

        return results
    
    def get_all_actors(self):
        """Collects all of the actors in the cast.
        
        Returns:
            A list (results) of Actor instances.
        """
        results = []

        for group in self._actors:
            results.extend(self._actors[group])

        return results

    def remove_actor(self, group, actor):
        """Removes an actor from the given group.
        
        Args:
            group (string): Name of the group.
            actor (Actor): The actor to remove.
        """
        if group in self._actors:
            self._actors[group].remove(actor)

    def remove_all_actors(self):
        """Removes all actors
        
        Args:
            None
        """
        self._actors = {}