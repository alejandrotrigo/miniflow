class Node(object):
    def __init__(self, inbound_nodes=[]):
        #Node(s) from which this node receives values
        self.inbound_nodes = inbound_nodes
        #Node(s) to which this Node passes values
        self.outbound_nodes = []
        #For each inbound node here, add this Node as an outbound Node do _that_ Node
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)

        self.value = None

    def forward(self):
        """
        Forward propagation .

        Compute the output value based on 'inbound_nodes' and
        store the result in self.value.
        """
        raise Not Implemented

class Input(Node):
    def __init__(self):
        #An input node has no inbound nodes
        #So no need to pass anything to the node instantiator
        Node.__init__(self)
    # NOTE: Input node is the only node where the value
    # may be passed as an argument to forward().
    #
    # All other node implementations should get the value
    # of the previous node from self.inbound_nodes
    #
    # Example:
    # val0 = self.inbound_nodes[0].value
    def forward(self, value=None):
        #Overwrite the value if one is passed in.
        if value is not None:
            self.value = value

class Add(Node):
    def __init__(self, x, y):
        Node.__init__(self, [x,y])

    def forward(self):
        x_value = self.inbound_nodes[0].value
        y_value = self.inbound_nodes[1].value
        self.value = x_value + y_value
