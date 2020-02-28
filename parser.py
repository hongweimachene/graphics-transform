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
def parse_file( fname, points, transform, screen, color ):
    file = open(fname, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    for i in range(len(lines)):
        if lines[i] == 'line':
            s = map(int, lines[i+1].split(' '))
            points.append([s[0], s[1], s[2], 1])
            points.append([s[3], s[4], s[5], 1])
            print('line')

        elif lines[i] == 'ident':
            ident(transform)

        elif lines[i] == 'scale':
            s = lines[i+1].split(' ')
            matrix_mult(make_scale(int(s[0]), int(s[1]), int(s[2])), transform)
            print('scale')

        elif lines[i] == 'move':
            s = lines[i+1].split(' ')
            m = make_translate(int(s[0]), int(s[1]), int(s[2]))
            matrix_mult(m ,transform)
            print('move')

        elif lines[i] == 'rotate':
            s = lines[i+1].split(' ')
            if s[0] == 'x':
                matrix_mult(make_rotX(int(s[1])), transform)
                print('rotate X')

            elif s[0] == 'y':
                matrix_mult(make_rotY(int(s[1])), transform)
                print('rotate Y')

            elif s[0] == 'z':
                matrix_mult(make_rotZ(int(s[1])), transform)
                print('rotate Z')

        elif lines[i] == 'apply':
            matrix_mult(transform, points)
            for i in range(len(points)):
                points[i] = map(int, points[i])

        elif lines[i] == 'display':
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)

        elif lines[i] == 'save':
            s = lines[i+1]
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, s)
            i = i + 1

        elif lines[i] == 'quit':
            break
