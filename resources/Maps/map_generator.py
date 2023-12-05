from scripts import save

class MapGen:
    def __init__(self, map_name):

        self.map = [["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    [
                        "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Stone:01:Tp", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    [
                        "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                        "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                        "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ]

        save.save(self.map, 'save1', map_name)

        return