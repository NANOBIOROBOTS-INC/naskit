class Helix:
    
    __slots__ = '__opc', '__clc'
    
    def __init__(self, open_chain, close_chain):
        self.__opc = tuple(open_chain)
        self.__clc = tuple(close_chain)
    
    
    @property
    def opc(self):
        return self.__opc
    
    
    @property
    def clc(self):
        return self.__clc
    
    
    def __iter__(self):
        return zip(self.__opc, self.__clc[::-1])
    
    
    def __len__(self):
        return len(self.__opc)
    
    
    def __getitem__(self, key): 
        return self.opc[key], self.clc[-(key+1)]
    
    
    def __str__(self):
        return (f"-({', '.join([str(i) for i in self.__opc])})\n"
                f" ({', '.join([str(i) for i in self.__clc[::-1]])})-")
    
    
    def __repr__(self):
        return str(self)
    

def _make_loop(nodes):
    c = len([1 for n in nodes if isinstance(n, tuple)])
    if c==1:
        return Hairpin(nodes)
    
    elif c>2:
        return Junction(nodes)
    
    elif isinstance(nodes[1], tuple) or isinstance(nodes[-1], tuple):
        return Bulge(nodes)
    
    else:
        return InternalLoop(nodes)
        
    
class Loop:
    
    __slots__ = '__nodes', 
    
    def __init__(self, nodes, knot_nbs=None):
        self.__nodes = tuple(nodes)
        
        
    @property
    def nodes(self):
        return self.__nodes
    
    
    @property
    def loop(self):
        loop = [self.__nodes[0][0]]
        for i in range(1, len(self.__nodes)):
            n = self.__nodes[i]
            if isinstance(n, int):
                loop.append(n)
            else:
                loop.append(n[0])
                loop.append(n[1])
        loop.append(self.__nodes[0][1])
        return loop
    
    
    @property
    def branches(self):
        return tuple((n for n in self.__nodes if isinstance(n, tuple)))
    
    
    def __len__(self):
        return len(self.__nodes) + len(self.branches)
    
    
    def __iter__(self):
        return self.__nodes
    
    
    def __str__(self):
        tokens = [""]*len(self.__nodes)
        tokens[0] = f"[{self.__nodes[0][0]}, {self.__nodes[0][1]}]"
        
        for i in range(1, len(self.__nodes)):
            tokens[i] = str(self.__nodes[i])
            
        return ", ".join(tokens)
    
    
class Hairpin(Loop):
    
    __slots__ = tuple()
    
    def __init__(self, nodes):
        super().__init__(nodes)
    
    
class InternalLoop(Loop):
    
    __slots__ = tuple()
    
    def __init__(self, nodes):
        super().__init__(nodes)
        
        
class Bulge(Loop):
    
    __slots__ = tuple()
    
    def __init__(self, nodes):
        super().__init__(nodes)
        
        
class Junction(Loop):
    
    __slots__ = tuple()
    
    def __init__(self, nodes):
        super().__init__(nodes)
        
        
        
        
        
    
    
    