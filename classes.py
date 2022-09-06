import shapely.geometry as shap


class SimpleNode:

    def __init__(self, ind):
        self.id = ind
        self.x = None
        self.y = None
        self.height = None
        self.arc_list = []
        self.json_out = {}

    def set_xy(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def set_height(self, height):
        self.height = height

    def add_arcs_id(self, arc):
        self.arc_list.append(arc)

    def print_me_as_json(self):
        self.json_out.update({"id": self.id,
                              "coordinates": {
                                  "x": self.x,
                                  "y": self.y,
                                },
                              "height": self.height,
                              "arcs": self.arc_list})
        return self.json_out


class SimpleArc:

    def __init__(self, node_arc_list_id):
        self.id = node_arc_list_id
        self.start_node_id = None
        self.x_start = None
        self.y_start = None
        self.end_node_id = None
        self.x_end = None
        self.y_end = None
        self.height_start = 0.00
        self.height_end = 0.00
        self.distance = 0
        self.elev_difference = 0.00
        self.json_out = {}
        self.direction = True

    def process_arc(self, node, node_list):
        end_node = self.find_matching_node(node, node_list)
        self.x_start = node.x
        self.y_start = node.y
        self.start_node_id = node.id
        self.x_end = end_node.x
        self.y_end = end_node.y
        self.end_node_id = end_node.id
        self.height_start = node.height
        self.height_end = end_node.height
        self.elev_difference = self.height_start - self.height_end
        self.distance = shap.Point([self.x_start, self.y_start]).distance(shap.Point([end_node.x, end_node.y]))

    def find_matching_node(self, in_node, node_list):
        for node in node_list:
            if self.id in node.arc_list and in_node.id != node.id:
                return node

    def print_me_as_json(self):
        self.json_out.update({"id": self.id,
                              "coordinates": {
                                  "start": {
                                      "node_id": self.start_node_id,
                                      "x": self.x_start,
                                      "y": self.y_start,
                                      "height": self.height_start
                                  },
                                  "end": {
                                      "node_id": self.end_node_id,
                                      "x": self.x_end,
                                      "y": self.y_end,
                                      "height": self.height_end
                                  }
                                },
                              "distance": self.distance,
                              "elev_diff": self.elev_difference,
                              "direction": self.direction})
        return self.json_out
