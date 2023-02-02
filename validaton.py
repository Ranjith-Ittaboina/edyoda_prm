class validation:
  def validate_triangle(self):
    angle_of_side_1 = int(input("enter angle(deg) of first side of the triangle: "))
    angle_of_side_2 = int(input("enter angle(deg) of second side of the triangle:"))
    angle_of_side_3 = int(input("enter angle(deg) of third side of the triangle: "))
    if (angle_of_side_1 + angle_of_side_2 + angle_of_side_3) == 180:
      print("valid triangle")
    else:
      print("invalid triangle")

  def validate_rectangle(self): #Let adjacent sides are perpendicular to eachother.
    length_1 = int(input("enter length of first side of rectangle: "))
    breadth_1 = int(input("enter breadth of second side of rectangle: "))
    length_2 = int(input("enter length of third side of rectangle: "))
    breadth_2 = int(input("enter breadth of fourth side of rectangle: "))
    if (length_1 == length_2) and (breadth_1 == breadth_2) and (length_1 + length_2 >> breadth_1 + breadth_2):
      print("valid rectangle")
    else:
      print("invalid rectangle")


if __name__ == "__main__":

    while True:
        triangle_object = validation()
        triangle_object.validate_triangle()

        rectangle_object = validation()
        rectangle_object.validate_rectangle()
