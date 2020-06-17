class Kangaroo(object):
    """ represents a kangaroo """
    def __init__(self):
        self.pouch_contents = []
    
    def __str__(self):
        s = '%s {\n' % object.__str__(self)
        for obj in self.pouch_contents:
            s += '\n    %s' % object.__str__(obj)
        s += '\n\n}\n'
        return s

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)


kanga = Kangaroo()
roo = Kangaroo()

kanga.put_in_pouch(roo)
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')

print(kanga)