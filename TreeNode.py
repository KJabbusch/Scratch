class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)

  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    while story_node.choices:
      choice = int(input("Enter 1 or 2 to continue the story: "))
      valid_options = [1, 2]
      while choice not in valid_options:
        choice = int(input("Enter 1 or 2 to continue the story: "))
      chosen_index = int(choice) - 1
      chosen_child = story_node.choices[chosen_index]
      print(chosen_child.story_piece)
      story_node = chosen_child

story_root = TreeNode("You are in a forest clearing. There is a path to the left.\nA bear emerges from the trees and roars!\nDo you:\n1) Roar back!\n2) Run to the left...")
choice_a = TreeNode("The bear is startled and runs away.\nDo you:\n1) Shout 'Sorry bear!'\n2) Yell 'Hooray!'\n")
choice_a_1 = TreeNode("The bear returns and tells you it's been a rough week. After making peace with a talking bear, he shows you the way out of the forest.\n\nYOU HAVE ESCAPED THE WILDERNESS.")
choice_a_2 = TreeNode("The bear returns and tells you that bullying is not okay before leaving you alone in the wilderness.\n\nYOU REMAIN LOST.")

choice_b = TreeNode("You come across a clearing full of flowers.\nThe bear follows you and asks 'what gives?'\nDo you:\n1) Gasp 'A talking bear!'\n2) Explain that the bear scared you.\n")
choice_b_1 = TreeNode("The bear is unamused. After smelling the flowers, it turns around and leaves you alone.\n\nYOU REMAIN LOST.")
choice_b_2 = TreeNode("The bear understands and apologizes for startling you. Your new friend shows you a path leading out of the forest.\n\nYOU HAVE ESCAPED THE WILDERNESS.")

story_root.add_child(choice_a)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

story_root.add_child(choice_b)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

story_root.traverse()