class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.undo_queue = []
        self.redo_queue = []

    def add(self, num: int):
        op = []
        op.append('add')
        op.append(num)
        self.undo_queue.append(op)
        self.value = self.value + num
        

    def subtract(self, num: int):
        op = []
        op.append('sub')
        op.append(num)
        self.undo_queue.append(op)
        self.value = self.value - num

    def undo(self):
        if len(self.undo_queue) > 0: 
            op = self.undo_queue[-1]
            # self.undo_queue = self.undo_queue[:-1]
            del self.undo_queue[-1]
            if (op[0] == 'add'): 
                self.value = self.value - op[1]
                self.redo_queue.append(op)
            elif(op[0] == 'sub'): 
                self.value = self.value + op[1]
                self.redo_queue.append(op)
            # op = self.undo_queue[-1]
            print(self.undo_queue)


    def redo(self):
        if len(self.redo_queue) > 0: 
            op = self.redo_queue[-1]
            del self.redo_queue[-1]
            if (op[0] == 'add'): 
                self.value = self.value + op[1]
            elif(op[0] == 'sub'): 
                self.value = self.value - op[1]

    def bulk_undo(self, steps: int):
        print(self.value)
        for i in range(steps):
            self.undo()


    def bulk_redo(self, steps: int):
        for i in range(steps):
            self.redo()
