from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""

def parse_file(fname, points, transform, screen, color):
      f = open(fname, 'r')
      line = f.readlines()

      index = 0
      while (index < len(line)):

            l = line[index].strip('\n')
            if l == "line":
                  index += 1
                  cords = line[index].strip('\n').split()
                  cords = [int(x) for x in cords]
                  add_edge(points, cords[0], cords[1], cords[2], cords[3], cords[4], cords[5])
            elif l == "ident":
                  ident(transform)
            elif l == "scale":
                  index += 1
                  factor = line[index].strip('\n').split()
                  factor = [int(x) for x in factor]
                  m = make_scale(factor[0], factor[1], factor[2])
                  matrix_mult(m, transform)
            elif l == "move":
                  index += 1
                  unit = line[index].strip('\n').split()
                  unit = [int(x) for x in unit]
                  m = make_translate(unit[0], unit[1], unit[2])
                  matrix_mult(m, transform)
            elif l == "rotate":
                  index += 1
                  param = line[index].strip('\n').split()
                  if param[0] == 'x':
                        m = make_rotX(int(param[1]))
                        matrix_mult(m, transform)
                  elif param[0] == 'y':
                        m = make_rotY(int(param[1]))
                        matrix_mult(m, transform)
                  elif param[0] == 'z':
                        m = make_rotZ(int(param[1]))
                        matrix_mult(m, transform)
            elif l == "apply":
                  matrix_mult(transform, points)
            elif l == "display":
                  clear_screen(screen)
                  for x in range(len(points)):
                        for y in range(len(points[0])):
                              points[x][y] = int(points[x][y])
                  draw_lines(points, screen, color)
                  display(screen)
            elif l == "save":
                  index += 1
                  fname = line[index].strip('\n')
                  clear_screen(screen)
                  for x in range(len(points)):
                        for y in range(len(points[0])):
                              points[x][y] = int(points[x][y])
                  draw_lines(points, screen, color)
                  save_extension(screen, fname)
            index += 1

      f.close()