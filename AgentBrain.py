class AgentBrain:
    def __init__(self, variance):
        self.model = keras.Sequential([
            layers.Flatten(input_shape=(200,)),
            layers.Dense(units=round(256), activation='gaussian'),
            layers.Dense(units=3),
        ])


    def updateWeights(self, variance):
        for
