'''
Author: Electra Bree
Username: rbre069

Creating a colored GUI pattern from a text file
'''

from tkinter import *
import random

#-------------------------------------------
# main() function
#-------------------------------------------
def main():
    size = 10
    start_left = size * 2
    start_down = size * 2
    filename = input("Enter a filename: ")	
    pattern_list = read_pattern(filename)
    number_of_rows = len(pattern_list)	
    number_of_columns = len(pattern_list[0])
    canvas_width = size * number_of_columns +size * 4
    canvas_height = number_of_rows * size + size * 4
    window = Tk() 
    window.title("A5 by rbre069") 
    geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
    window.geometry(geometry_string)
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand = True) #Canvas fills the whole window  
    draw_pattern(a_canvas, pattern_list, size, start_left, start_down)	
    window.mainloop()

#-------------------------------------------
# split_digits() function
#-------------------------------------------
def split_digits(line):
    digits_list = []
    digits_list += line
    return digits_list

#-------------------------------------------
# process_file() function
#-------------------------------------------
def process_file(filename):
    file = open(filename, "r")
    lines_list = file.readlines()
    for index in range(0, len(lines_list)):
        if '\n' in lines_list[index]:
            lines_list[index] = lines_list[index][:-1:]
    return lines_list 

#-------------------------------------------
# read_pattern() function
#-------------------------------------------
def read_pattern(filename):
    lines_list = process_file(filename)
    list_of_digits = []
    for element in lines_list:
        digits_list = split_digits(element)
        list_of_digits.append(digits_list)
    return list_of_digits

#-------------------------------------------
# draw_pattern() function
#-------------------------------------------	
def draw_pattern(a_canvas, pattern_list, size, left, top):
    possible_digits = "0123456789"
    colours = ["black", "white", "red", "orange", "yellow", "green", "cyan", "blue", "brown", "teal" ]
    for element in pattern_list:
        x_left = left
        for digit in element:
            if digit in possible_digits:
                colour = colours[int(digit)]
                rect = (x_left, top, x_left + size, top + size)
                a_canvas.create_rectangle(rect, fill = colour)
                x_left += size
        top += size
  

main()
