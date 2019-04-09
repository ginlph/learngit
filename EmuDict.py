class EmuDict(object):
    def __init__(self, _dict):
        self._dict = _dict
    def __repr__(self):
        return "EmuDict" + repr(self._dict)
    def __getitem__(self, key):
        return self._dict[key]
    def __setitem__(self, key, value):
        self._dict[key] = value
    def __delitem__(self, key):
        del self._dict[key]
    def __contains__(self, key):
        return key in self._dict
    def __iter__(self):
        return iter(self._dict)
    def __len__(self):
        return len(self._dict)


example_dict = {"name": "LPH", "age": 23}
emudict = EmuDict(example_dict)
emudict["gender"] = "male"
print(emudict)
for i in emudict:
    print(i)

print(len(emudict))

