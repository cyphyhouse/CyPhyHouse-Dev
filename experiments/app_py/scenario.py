"""
The following scenarios are generated by hand

SIMPLE_CORRIDOR - 6 Drones fly single file down the same corridor
LOOP            - 6 Drones fly the same loop
BUSY_CORRIDOR   - 6 Drones fly single file down the same corridor (3 Drones fly one way, 3 fly in the opposite direction)
"""
SIMPLE_CORRIDOR = {'drone0': [(-70.0, -65.0, 1.0), (-45.0, -66.0, 1.0), (-33.0, -65.0, 0.3)],
                   'drone1': [(-70.0, -65.0, 1.0), (-45.0, -66.0, 1.0), (-35.0, -65.0, 0.3)],
                   'drone2': [(-70.0, -65.0, 1.0), (-45.0, -66.0, 1.0), (-37.0, -65.0, 0.3)],
                   'drone3': [(-70.0, -65.0, 1.0), (-45.0, -66.0, 1.0), (-39.0, -65.0, 0.3)],
                   'drone4': [(-70.0, -65.0, 1.0), (-45.0, -66.0, 1.0), (-41.0, -65.0, 0.3)],
                   'drone5': [(-70.0, -65.0, 1.0), (-45.0, -66.0, 1.0), (-43.0, -65.0, 0.3)]}

LOOP = {'drone0': [(-64.0, -66.0, 1.0), (-64.0, -59.0, 1.0), (-39.5, -59.0, 1.0), (-39.5, -59.0, 1.0), (-39.5, -66.0, 1.0), (-86, -64, 0.3)],
        'drone1': [(-64.0, -66.0, 1.0), (-64.0, -59.0, 1.0), (-39.5, -59.0, 1.0), (-39.5, -59.0, 1.0), (-39.5, -66.0, 1.0), (-86, -66, 0.3)],
        'drone2': [(-64.0, -66.0, 1.0), (-64.0, -59.0, 1.0), (-39.5, -59.0, 1.0), (-39.5, -59.0, 1.0), (-39.5, -66.0, 1.0), (-86, -68, 0.3)],
        'drone3': [(-64.0, -66.0, 1.0), (-64.0, -59.0, 1.0), (-39.5, -59.0, 1.0), (-39.5, -59.0, 1.0), (-39.5, -66.0, 1.0), (-84, -64, 0.3)],
        'drone4': [(-64.0, -66.0, 1.0), (-64.0, -59.0, 1.0), (-39.5, -59.0, 1.0), (-39.5, -59.0, 1.0), (-39.5, -66.0, 1.0), (-84, -66, 0.3)],
        'drone5': [(-64.0, -66.0, 1.0), (-64.0, -59.0, 1.0), (-39.5, -59.0, 1.0), (-39.5, -59.0, 1.0), (-39.5, -66.0, 1.0), (-84, -68, 0.3)]}

BUSY_CORRIDOR = {'drone0': [(-60.0, -65.0, 1.0), (-55.0, -65.0, 1.0), (-50.0, -65.0, 1.0), (-45.0, -65.0, 1.0), (-40.0, -65.0, 1.0), (-35.0, -65.0, 0.3)],
                 'drone1': [(-60.0, -65.0, 1.0), (-55.0, -65.0, 1.0), (-50.0, -65.0, 1.0), (-45.0, -65.0, 1.0), (-40.0, -65.0, 1.0), (-36.0, -66.0, 0.3)],
                 'drone2': [(-60.0, -65.0, 1.0), (-55.0, -65.0, 1.0), (-50.0, -65.0, 1.0), (-45.0, -65.0, 1.0), (-40.0, -65.0, 1.0), (-37.0, -67.0, 0.3)],
                 'drone3': [(-45.0, -67.0, 1.0), (-50.0, -67.0, 1.0), (-55.0, -67.0, 1.0), (-60.0, -67.0, 1.0), (-65.0, -67.0, 1.0), (-80.0, -67.0, 0.3)],
                 'drone4': [(-45.0, -67.0, 1.0), (-50.0, -67.0, 1.0), (-55.0, -67.0, 1.0), (-60.0, -67.0, 1.0), (-65.0, -67.0, 1.0), (-80.0, -68.0, 0.3)],
                 'drone5': [(-45.0, -67.0, 1.0), (-50.0, -67.0, 1.0), (-55.0, -67.0, 1.0), (-60.0, -67.0, 1.0), (-65.0, -67.0, 1.0), (-80.0, -69.0, 0.3)]}

"""
The following scenarios generated through the generateScenario.py file (a set of randomly generated waypoints)

RANDOM_SCENARIO1 - 6 Drones 3 waypoints each
RANDOM_SCENARIO2 - 6 Drones 6 waypoints each
RANDOM_SCENARIO3 - 6 Drones 9 waypoints each
RANDOM_SCENARIO4 - 10 Drones 5 waypoints each
"""
RANDOM_SCENARIO1 = { 'drone0': [(-37.61, -67.08, 0.8), (-43.26, -38.57, 2.49), (-67.98, -50.72, 0.59)],
                    'drone1': [(-40.07, -65.17, 2.14), (-17.36, -44.54, 1.97), (-26.29, -43.94, 0.99)],
                    'drone2': [(-74.86, -58.16, 0.52), (-69.47, -67.48, 2.42), (-53.15, -68.59, 2.04)],
                    'drone3': [(-49.94, -47.47, 2.14), (-64.94, -57.79, 1.89), (-61.41, -35.24, 0.89)],
                    'drone4': [(19.28, -47.31, 2.43), (24.62, -64.83, 1.25), (-12.76, -64.46, 1.11)],
                    'drone5': [(0.91, -67.55, 2.27), (-10.38, -57.05, 2.1), (-8.24, -50.28, 0.88)]}


RANDOM_SCENARIO2 ={ 'drone0': [(-61.7, -45.67, 0.91), (-44.19, -48.37, 1.51), (-54.86, -50.6, 0.77), (-52.15, -55.02, 1.49), (-38.22, -51.96, 2.13), (-51.19, -45.96, 0.91)],
                    'drone1': [(21.88, -46.32, 1.11), (23.46, -68.85, 1.96), (5.58, -66.55, 0.46), (20.82, -63.94, 1.81), (-41.49, -68.06, 0.6), (22.39, -63.94, 2.12)],
                    'drone2': [(-61.86, -30.86, 2.37), (-40.09, -33.2, 1.95), (-23.21, -34.59, 0.99), (-33.24, -31.34, 0.9), (-71.15, -33.02, 0.56), (-34.81, -33.43, 2.04)],
                    'drone3': [(13.38, -52.81, 1.82), (12.96, -52.68, 1.1), (10.52, -41.33, 0.41), (15.96, -41.35, 0.93), (16.76, -55.83, 0.47), (14.22, -57.34, 0.91)],
                    'drone4': [(-10.53, -37.04, 1.47), (-14.9, -38.67, 1.18), (-13.94, -39.08, 1.5), (-31.87, -46.51, 1.43), (-24.5, -42.09, 1.54), (-26.87, -51.45, 2.02)],
                    'drone5': [(-9.17, -57.87, 0.76), (-11.21, -50.24, 1.9), (-11.02, -52.84, 1.42), (-35.15, -58.84, 2.21), (-8.94, -38.62, 1.69), (-25.88, -45.82, 1.27)]}


RANDOM_SCENARIO3 = { 'drone0': [(3.65, -41.35, 1.62), (6.86, -45.81, 0.96), (0.73, -47.43, 1.58), (3.22, -51.06, 1.15), (1.96, -40.35, 1.66), (0.27, -40.47, 1.63), (5.69, -58.01, 1.44), (2.17, -55.8, 2.4), (5.84, -46.63, 1.92)],
                    'drone1': [(12.43, -66.59, 0.65), (-31.62, -64.91, 0.92), (-57.34, -66.62, 1.44), (-38.95, -65.9, 1.83), (-69.98, -66.17, 0.73), (-76.58, -54.07, 1.24), (-75.67, -60.09, 1.25), (-76.24, -55.38, 1.02), (-78.71, -57.92, 1.02)],
                    'drone2': [(-67.67, -64.22, 1.42), (-39.12, -65.54, 0.99), (-30.83, -55.59, 1.0), (-15.69, -48.08, 1.59), (-23.17, -58.04, 0.55), (-35.18, -56.85, 1.48), (-27.16, -42.57, 0.64), (-23.66, -55.17, 1.33), (-18.9, -45.26, 2.39)],
                    'drone3': [(-23.41, -30.02, 1.24), (-25.69, -33.0, 2.36), (-45.85, -34.02, 1.2), (-19.97, -33.81, 2.16), (-24.48, -34.6, 1.19), (-64.86, -30.95, 2.23), (-22.19, -33.64, 1.2), (-67.25, -32.26, 2.12), (-34.08, -34.6, 1.43)],
                    'drone4': [(-25.82, -63.48, 0.84), (11.95, -63.82, 0.47), (-21.28, -64.57, 2.36), (-41.3, -64.25, 0.98), (-51.99, -68.8, 2.48), (-43.75, -67.14, 2.44), (-67.28, -65.27, 2.04), (21.42, -63.81, 2.13), (17.34, -63.13, 1.04)],
                    'drone5': [(-26.84, -51.99, 1.36), (-16.44, -53.29, 1.28), (-30.67, -39.41, 0.7), (-24.95, -56.32, 0.41), (-25.71, -54.91, 1.87), (-15.0, -43.14, 2.19), (-36.43, -49.03, 1.66), (-24.72, -54.68, 2.24), (-8.02, -41.64, 0.5)]}


RANDOM_SCENARIO4 = { 'drone0': [(-56.13, -61.96, 1.33), (-21.88, -67.32, 0.83), (15.61, -68.48, 2.2), (-47.27, -64.59, 2.45), (-8.21, -69.07, 1.7)],
                    'drone1': [(10.55, -64.27, 1.0), (-0.05, -65.41, 0.67), (-22.06, -46.4, 0.7), (-33.57, -39.62, 1.44), (-33.81, -54.55, 1.5)],
                    'drone2': [(18.2, -55.49, 1.11), (18.12, -53.17, 2.11), (23.34, -57.99, 1.59), (24.05, -38.6, 1.7), (20.86, -53.69, 2.08)],
                    'drone3': [(-33.34, -30.87, 0.83), (-76.49, -30.48, 0.41), (-65.9, -34.92, 1.62), (-67.28, -34.71, 2.11), (-65.86, -31.51, 1.09)],
                    'drone4': [(-28.58, -38.07, 2.27), (-28.22, -37.81, 0.6), (-10.69, -40.22, 0.48), (-13.91, -44.92, 1.65), (-26.82, -48.21, 1.52)],
                    'drone5': [(-55.72, -68.53, 1.28), (-44.7, -63.37, 1.72), (-36.21, -64.79, 1.35), (-23.96, -37.82, 1.02), (-11.73, -48.65, 1.57)],
                    'drone6': [(-44.84, -58.91, 1.16), (-43.14, -44.35, 1.34), (-64.07, -57.14, 1.78), (-37.18, -39.63, 0.6), (-47.06, -43.23, 2.18)],
                    'drone7': [(8.08, -68.72, 0.93), (-7.44, -64.92, 2.25), (-61.91, -62.75, 1.76), (-24.44, -65.0, 0.95), (-19.23, -64.31, 2.0)],
                    'drone8': [(-69.66, -30.4, 1.88), (-17.65, -34.38, 0.98), (-72.59, -34.54, 0.61), (-45.22, -33.15, 1.98), (-60.85, -32.36, 1.93)],
                    'drone9': [(-9.74, -57.13, 1.01), (-21.55, -46.81, 2.44), (-19.68, -58.72, 0.52), (-22.74, -54.54, 0.58), (-26.54, -57.44, 1.66)]}

SCENARIO_LIST = [SIMPLE_CORRIDOR, LOOP, BUSY_CORRIDOR, RANDOM_SCENARIO1, RANDOM_SCENARIO2, RANDOM_SCENARIO3]
