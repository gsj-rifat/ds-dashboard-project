class BaseComponent:

    def build_component(self, entity_id, model):
        raise NotImplementedError
    
    def outer_div(self, component):
        return component
    

    def component_data(self, entity_id, model):
        raise NotImplemented

    def __call__(self, entity_id, model):
        """

        :type model: object
        """
        component = self.build_component(entity_id, model)

        return self.outer_div(component)