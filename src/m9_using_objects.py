"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Mashengjun Li.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()
def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    window = rg.RoseWindow(400,400)
    radius = 10
    circle = rg.Circle(rg.Point(200,150),radius)
    circle.fill_color = 'blue'
    r = 20
    circle2 = rg.Circle(rg.Point(250,100),r)
    circle2.outline_color = 'red'
    circle.attach_to(window)
    circle2.attach_to(window)
    window.render()

    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """

    window = rg.RoseWindow(400,400)
    radius = 50
    center = rg.Point(150,150)
    circle = rg.Circle(center,radius)
    circle.outline_thickness = 5
    circle.fill_color = 'blue'
    circle.attach_to(window)
    print(circle.outline_thickness,circle.fill_color,circle.center,center.x,center.y)

    corner1 = rg.Point(200,150)
    corner2 = rg.Point(300,100)
    rec = rg.Rectangle(corner1, corner2)
    rec.outline_thickness = 5
    rec.fill_color = 'blue'
    rec.attach_to(window)
    window.render()
    print(rec.outline_thickness,rec.fill_color,rec.get_center(),corner1.x,corner2.x,corner1.y,corner2.y)
    window.close_on_mouse_click()
# ------------------------------------------------------------------
    # Done: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # Done: 4. Implement and test this function.
    window = rg.RoseWindow(400,400)
    start1 = rg.Point(20,100)
    start2 = rg.Point(20,300)
    end1 = rg.Point(380,100)
    end2 = rg.Point(380,300)

    line1 = rg.Line(start1, end1)
    line2 = rg.Line(start2, end2)

    line2.thickness = 10
    midpoint = line2.get_midpoint()
    rg.Line(line2.get_midpoint(),line1.get_midpoint())
    print(midpoint,midpoint.x,midpoint.y)

    line1.attach_to(window)
    line2.attach_to(window)

    window.render()
    window.close_on_mouse_click()




# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
