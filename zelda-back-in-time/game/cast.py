class Cast:
    def __init__(self):
        self._actors = {}
        
    def add_actor(self, group, actor):
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        results = []

        if group in self._actors.keys():
            results = self._actors[group].copy()

        return results
    
    def get_all_actors(self):
        results = []

        for group in self._actors:
            results.extend(self._actors[group])

        return results

    def remove_actor(self, group, actor):
        """Removes an actor from the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to remove.
        """
        if group in self._actors:
            self._actors[group].remove(actor)