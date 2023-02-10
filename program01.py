#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A real estate owner in California, Lida,  inherits a piece of land. The
land is modeled as a rectangular patch of variable size. The patch of
land is represented with an image (list of lists).

To make some money out of it, she can decide to lease the land to
other people. To do that, she may decide to divide the land into four
other patches. In case she decides to not lease the land, no further
sub-patches are created. On the contrary, in case the land is divided
into four sub-patches, some colored marks (straight lines) on the land
are drawn with a thickness of one pixel to mark the private properties
that are created. There is no prior knowledge of how and where the
lines will be drawn, nor which colors will be used (there is no
regular pattern).  The only knowledge is that the lines are
axis-aligned.

The four lessees that receive the sub-patches of land may take the
same decision that Lida took before them. They may decide to sublease
once again their small patch to others or, else, to keep the land all
for themselves. The decision for each lessee is independent of each
other. For example, lessee #1 may decide to sublease again, while
lessee #2 may keep the land for himself, etc, whereas lessee #3 and #4
may subdivide. If they sublease and divide, they follow the same
policy of dividing in four parts and setting their boundaries with
line drawing but obviously with a different splitting position of
their land. For sure, they will be using a color that is different
from the colors used by Lida yet they will be using the same color
among them, at the same level of splitting.

NOTE: An important note is that the color of the background (bg) of
the land is not given (i.e. we do not know if the bg is black, or
white or blue etc) but we do know that the background land color is
NOT used by any of the lessees ever to mark their boundaries.

The subdivision process could continue until when all the lessees in
all patches stop subdividing their land. This process described here
leads us to the image that is taken as input to a program.

NOTE: You can assume that the smallest possible rectangular patch has
the shortest side of two pixels in length.

Think well about the problem and once you are sure of a solution,
design on the paper (this "design" needs be then described into the
pseudo code part) and then implement a program ex1(input_file,
output_file) which:
  - reads the file indicated by the parameter 'input_file'
    using the 'images' library 
  - preprocesses the image--if needed--and implements a
    *recursive* function to solve the requirements below.
  - counts all the patches of lands that are in the image and returns
    the number of patches. It should return the number of rectangles
    with the color of the background that is present in the
    image. Regarding the simplified case below:

        # +++++++++++++++++++
        # +-1-|-2-|---------+
        # ++++a+++|----5----+
        # +-3-|-4-|---------+
        # ++++++++b++++++++++
        # +-------|--7-|-8--+
        # +---6---|++++c+++++
        # +-------|-10-|-9--+
        # +++++++++++++++++++
      the approach should return 10 as the total number of patches. (The
    numbers in the simplified case above are just added for the sake
    of clarity. The image data does not contain those numbers,
    obviously).
  - finally, given that the real estate registry needs to book-keep
    all the boundaries created, the program shall build an output
    image of the size of 1x(N+1). The image encodes as the first pixel
    the color of the background. Then it should encode "the color
    hierarchy" of all the N colors used to subdivide the patches of
    land. The hierarchy is defined by "visiting" first in depth the
    upper left patch, then upper right patch, then lower left, and
    lower right. The colors should be stored in reverse order with
    respect to the "visit" made. With reference to the previous
    semplified case, assuming a boundary color is described with a
    letter, the output image should contain:
             out_colors = bg b c a


    Another case a bit more complex:

         +++++++++++++++++++++++++++++++++++++
         +-1-|-2-|---------|--------|--------+
         ++++a+++|----5----|---6----|----7---+
         +-3-|-4-|---------|--------|--------+
         ++++++++b+++++++++|++++++++c+++++++++
         +-------|--9-|-10-|--------|--------+
         +--8----|++++d++++|---13---|---14---+
         +-------|-11-|-12-|--------|--------+
         ++++++++++++++++++e++++++++++++++++++
         +-15|-16|---------|--------|-21|-22-+
         ++++f+++|---19----|---20---|+++g+++++
         +-17|-18|---------|--------|-23|--24+
         ++++++++h+++++++++|++++++++l+++++++++
         +-------|-26-|-27-|--------|-31-|-32+
         +--25---|++++m++++|---30---|+++n+++++
         +-------|-29-|-28-|--------|-33-|-34+
         +++++++++++++++++++++++++++++++++++++

         n_rect is: 34
         the color hierarchy is:
         bg e l n g h m f c b d a
 
NOTE: it is forbidden to import/use other libraries or open files
      except the one indicated

NOTE: The test system recognizes recursion ONLY if the recursive
      function/method is defined in the outermost level.  DO NOT
      define the recursive function within another function/method
      otherwise, you will fail all the tests.
"""

import images


def recursive1(database, image_list, position, bg_color, color_list, count = 0):
    try:
        color = database[position]
    except:
        return 1
    color_list.append(color)
    image1_2 = []
    image2_2 = []
    image3_2 = []
    image4_2 = []
    image1 = []
    image2 = []
    image3 = []
    image4 = []
    limit_y_axis = len(image_list)
    limit_x_axis = len(image_list[0])
    flag_y = True
    for xe in range(limit_y_axis):
        try:
            if image_list[xe][0] == color:
                for row1 in range(limit_y_axis):
                    if flag_y:
                        if image3 != []:
                            image4_2.append(image4)
                            #image4_2 = tuple(image4_2)
                            #image3_2 = list(image3_2)
                            image3_2.append(image3)
                            #image3_2 = tuple(image3_2)
                    else:
                        if image2 != []:
                            #image1_2 = list(image1_2)
                            image1_2.append(image1)
                            #image1_2 = tuple(image1_2)
                            #image2_2 = list(image2_2)
                            image2_2.append(image2)
                            #image2_2 = tuple(image2_2)
                    image1 = []
                    image2 = []
                    image3 = []
                    image4 = []
                    flag_x = True
                    if row1 == xe:
                        flag_y = False
                        continue
                    for pixel1 in range(limit_x_axis):
                        if image_list[row1][pixel1] == color:
                            flag_x = False
                            continue
                        elif flag_y and flag_x:
                           image4.append(image_list[row1][pixel1])
                        elif flag_y and not flag_x:
                           image3.append(image_list[row1][pixel1])
                        elif not flag_y and flag_x:
                           image2.append(image_list[row1][pixel1]) 
                        elif not flag_y and not flag_x:
                           image1.append(image_list[row1][pixel1])            
                image1_2 = list(image1_2)
                image1_2.append(image1)
                image1_2 = tuple(image1_2)
                image2_2 = list(image2_2)
                image2_2.append(image2)
                image2_2 = tuple(image2_2)
                break
        except:
                continue
    list1 = [image1_2, image2_2, image4_2, image3_2]
    for element in list1:
        breaker = False
        for row in element:
            for pixel in row:
                if pixel != bg_color:
                    count += recursive1(database, element, position + 1, bg_color, color_list)
                    breaker = True
                    break
            if breaker:
                break
        if not breaker:
            count += 1
    return count


def ex1(input_file, output_file):
    image_list = images.load(input_file)
    bg_color = image_list[0][0]
    database = {}
    temp_database = {}
    count = 0
    position = 0
    color_list = [bg_color]
    for row in image_list:
        for curr_pixel, nxt_pixel in zip(row, row[1:]):
            if nxt_pixel != bg_color:
                if nxt_pixel == curr_pixel:
                    if nxt_pixel not in database:
                        database[nxt_pixel] = 1
                        temp_database[nxt_pixel] = 1
                    else:
                        temp_database[nxt_pixel] += 1
                        if temp_database[nxt_pixel] > database[nxt_pixel]:
                            database[nxt_pixel] = temp_database[nxt_pixel]
                else:
                    temp_database[nxt_pixel] = 1
    database = sorted(database.items(),key = lambda x: x[1], reverse=True)
    database = [i[0] for i in database]
    result = int(recursive1(database, image_list, position, bg_color, color_list, count))
    images.save(color_list,output_file)
    # data = '{' + '"num_black_rects": {}, "color_order": {}'.format(result,color_list) + '}'
    # with open(output_file,'w') as f:
    #     f.writelines(data)
    return result

