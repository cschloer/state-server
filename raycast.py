from point import Point
import sys

def point_inside_shape(point, shape):
    '''
    A function that determines if a point
    is contained within a polygon shape
    using raycasting

    x: x coordinate of the point
    y: y coordinate of the point
    shape: a list of tuples, where each tuple
        represents a point of the shape (x and y). These points
        must be sequential with the start point repeated at the end
    '''
    number_of_intersections = 0
    for index in range(len(shape) - 1):
        segment = [shape[index], shape[index + 1]]
        # Sum up the number of intersections
        if ray_intersects_segment(point, segment):
            number_of_intersections += 1

    # If the number of intersections is odd, the point is inside the shape
    return (
        number_of_intersections % 2 == 1 or
        # Raycasting doesn't work for points that lie on the edge of the shape
        point_on_edge_of_shape(point, shape)
    )

def ray_intersects_segment(point, segment):
    '''
    A function that determines if a ray
    starting at a point will intersect a
    segment

    point: the point
    segment: the two points making up the segment
    '''
    # Determine which point has a lower y coord
    below_point = segment[0]
    above_point = segment[1]
    if (segment[0].y > segment[1].y):
        below_point = segment[1]
        above_point = segment[0]

    if point.y == below_point.y or point.y == above_point.y:
        point = Point(point.x, point.y + sys.float_info.min)

    # If y is out of bounds, return false
    if point.y < below_point.y or point.y > above_point.y:
        return False

    # If x is greater than both points' x values, return false
    elif point.x >= max(below_point.x, above_point.x):
        return False

    else:
        # If x is lower than both points' x values, return true
        if point.x < min(below_point.x, above_point.x):
            return True

        else:
            # Calculate the angles between the segment points and the inputed point
            if below_point.x != above_point.x:
                m_red = (above_point.y - below_point.y) / float(above_point.x - below_point.x)
            else:
                m_red = float("inf")
            if below_point.x != point.x:
                m_blue = (point.y - below_point.y) / float(point.x - below_point.x)
            else:
                m_blue = float("inf")

            # If the angle calculated with the inputed point is greater,
            # its ray intersects with the segment
            if m_blue >= m_red:
                return True
            else:
                return False
    return False

def point_on_edge_of_shape(point, shape):
    '''
    A function that determines if a point
    lies on the edge of a shape

    point: the point
    shape: a list of tuples, where each tuple
        represents a point of the shape (x and y). These points
        must be sequential with the start point repeated at the end
    '''
    for index in range(len(shape) - 1):
        segment = [shape[index], shape[index + 1]]
        # Sum up the number of intersections
        if point_lies_on_segment(point, segment):
            return True
    return False

def point_lies_on_segment(point, segment):
    '''
    A function that determines if a point
    lies on a line segment

    point: the point
    segment: the two points making up the segment
    '''
    endpoint1 = segment[0]
    endpoint2 = segment[1]
    return (
        # A point lies between two other points if they are all on the same
        # and the x values are sequential
        points_collinear(endpoint1, endpoint2, point) and
        (
            points_within(endpoint1.x, point.x, endpoint2.x) if
            endpoint1.x != endpoint2.x else
            points_within(endpoint1.y, point.y, endpoint2.y)
        )
    )

def points_collinear(point1, point2, point3):
    ''' Returns true if all 3 points lie on the same line '''
    return (
        (point2.x - point1.x) * (point3.y - point1.y) ==
        (point3.x - point1.x) * (point2.y - point1.y)
    )

def points_within(val1, val2, val3):
    ''' Returns true if val2 is between val1 and val3 inclusive '''
    return val1 <= val2 <= val3 or val3 <= val2 <= val1
