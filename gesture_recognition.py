import math


def distance(point1, point2):
    """Calculate distance between two points."""
    return math.sqrt(
        (point1[0] - point2[0]) ** 2 +
        (point1[1] - point2[1]) ** 2
    )


def recognize_gesture(points):
    """
    Recognize basic hand gestures using
    MediaPipe's 21 hand landmarks.
    """

    if len(points) != 21:
        return "UNKNOWN"


    # Landmark indexes:
    #
    # 0  = Wrist
    #
    # Thumb:
    # 1,2,3,4
    #
    # Index:
    # 5,6,7,8
    #
    # Middle:
    # 9,10,11,12
    #
    # Ring:
    # 13,14,15,16
    #
    # Pinky:
    # 17,18,19,20


    # --------------------------------
    # Determine finger states
    # --------------------------------

    index_up = points[8][1] < points[6][1]

    middle_up = points[12][1] < points[10][1]

    ring_up = points[16][1] < points[14][1]

    pinky_up = points[20][1] < points[18][1]


    # --------------------------------
    # Thumb detection
    # --------------------------------

    thumb_up = points[4][0] > points[3][0]


    # --------------------------------
    # OPEN PALM
    # --------------------------------

    if (
        index_up
        and middle_up
        and ring_up
        and pinky_up
    ):
        return "OPEN PALM"


    # --------------------------------
    # FIST
    # --------------------------------

    if (
        not index_up
        and not middle_up
        and not ring_up
        and not pinky_up
    ):
        return "FIST"


    # --------------------------------
    # PEACE
    # --------------------------------

    if (
        index_up
        and middle_up
        and not ring_up
        and not pinky_up
    ):
        return "PEACE"


    # --------------------------------
    # POINTING
    # --------------------------------

    if (
        index_up
        and not middle_up
        and not ring_up
        and not pinky_up
    ):
        return "POINTING"


    # --------------------------------
    # THUMBS UP
    # --------------------------------

    if (
        thumb_up
        and not index_up
        and not middle_up
        and not ring_up
        and not pinky_up
    ):
        return "THUMBS UP"


    return "UNKNOWN"