class Armor:
  def __init__(self, name, max_block):
    '''Instantiate instance properties.
        name: String
        max_block: Integer
    '''
    # TODO: Create instance variables for the values passed in.
    self.name = name
    self.max_block = max_block

if __name__ == "__main__":
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())