import matplotlib.pyplot as plt
import numpy as np

ACAS_grid_1_manual = {            
    'drone0': [
        (0, 0.0, 40), 
        (0, 29.09656181419166, 40), 
        (0, 58.19312362838332, 40), 
        (0, 261.86905632772494, 40),
        (0, 290.965618, 40),
        (0, 320.965618, 40)
    ],
    'drone1': [
         (-133.30894903682029, 0.0, 40), 
        (-119.97889106532426, 29.09622794860579, 40), 
        (-106.64883309382825, 58.19245589721158, 40), 
        (-1.0, 261.86605153745208, 40),
        (-1.0, 323.870440711, 40) 
    ],
}

ACAS_grid_2_manual = {            
    'drone0': [
        (0, 0.0, 40), 
        (0, 29.09656181419166, 40), 
        (0, 58.19312362838332, 40), 
        (0, 261.86905632772494, 40),
        (0, 290.965618, 40)
    ],
    'drone1': [
        (0, 29.09656181419166, 40), 
        (0, 58.19312362838332, 40), 
        (0, 261.86905632772494, 40),
        (0, 290.965618, 40),
        (0, 320.965618, 40) 
    ],
}
#####################################################################
# ACAS_grid_1 = {'drone0': [(0, 2909.6208, 40)], 'drone1': [(-0.083692200891619, 2909.5874138473937, 40)]}
  # {'drone0': [(0.0, 89, 40.0)], 'drone1': [(100.0, 95.7, 40.0)]}

ACAS_grid_1 = {'drone0': [(0, 727.4052, 40)], 'drone1': [(33.30381664475482, 800.1365388080332, 40)]}

ACAS_grid_2 = {'drone0': [(0, 352.50120000000004, 40)], 'drone1': [(4.6192452617039014e-14, 421.11168, 40)]}

ACAS_grid_3 =  {'drone0': [(0, 381.0, 40)], 'drone1': [(-12.417222988993899, 420.02421224908096, 40)]}

ACAS_grid_4 =  {'drone0': [(0, 156.1338, 40)], 'drone1': [(23.559900064214162, 195.31439098894106, 40)]}

ACAS_grid_5 =  {'drone0': [(0, 1269.93396, 40)], 'drone1': [(12.103581926072252, 1257.6522812240385, 40)]}

ACAS_grid_6 =  {'drone0': [(0, 464.2865999999999, 40)], 'drone1': [(-33.32847376731792, 510.69326733326193, 40)]}

ACAS_grid_7 =  {'drone0': [(0, 873.1758000000001, 40)], 'drone1': [(-61.54588754216422, 934.9967774479301, 40)]}

ACAS_grid_8 =  {'drone0': [(0, 484.78440000000006, 40)], 'drone1': [(-23.56865106314268, 509.6539560630997, 40)]}

ACAS_grid_9 =  {'drone0': [(0, 379.0188, 40)], 'drone1': [(3.0794968411359347e-15, 383.56032000000005, 40)]}

ACAS_grid_10 =  {'drone0': [(0, 457.2, 40)], 'drone1': [(-9.238490523407803e-14, 411.47999999999996, 40)]}

ACAS_grid_1_no_scaling =  {'drone0': [(0, 29096.208000000002, 40)], 'drone1': [(1332.152665790196, 32005.46155232133, 40)]}

######################################################################

ACAS_01 = {            
    'drone0': [
        (0, 0.0, 40), 
        (0, 29.09656181419166, 40), 
        (0, 58.19312362838332, 40), 
        (0, 261.86905632772494, 40),
        (0, 290.965618, 40),
        (0, 320.965618, 40)
    ],
    'drone1': [
        (-133.30894903682029, 0.0, 40), 
        (-119.97889106532426, 29.09622794860579, 40), 
        (-106.64883309382825, 58.19245589721158, 40), 
        (-1.0, 261.86605153745208, 40),
        (-1.0, 323.870440711, 40),        
    ],
}

ACAS_01_0 = {
    'drone0': [
        [0.0, 0.0, 40], 
        [0.0, 29.09656181419166, 40], 
        [0.0, 58.19312362838332, 40], 
        [0.0, 261.86905632772493, 40], 
        [0.0, 290.965618, 40], 
        [0.0, 320.965618, 40]
    ], 
    'drone1': [
        [-133.30894903682028, 0.0, 40], 
        [-119.97889106532426, 29.09622794860579, 40], 
        [-106.64883309382824, 58.19245589721158, 40], 
        [-1.0, 261.8660515374521, 40], 
        [-1.0, 323.870440711, 40]
    ]
}
ACAS_01_0_a = {'drone0': [[0.0, 0.0, 40], 
        [0.0, 29.09656181419166, 40]], 'drone1': [[-133.30894903682028, 0.0, 40], 
        [-119.97889106532426, 29.09622794860579, 40]]}
ACAS_01_0_b = {'drone0': [[0.0, 58.19312362838332, 40], 
        [0.0, 261.86905632772493, 40]], 'drone1': [[-106.64883309382824, 58.19245589721158, 40], 
        [-1.0, 261.8660515374521, 40]]}
ACAS_01_0_c = {'drone0': [[0.0, 290.965618, 40], 
        [0.0, 320.965618, 40]], 'drone1': [[-1.0, 323.870440711, 40]]}
ACAS_01_1 = {'drone0': [[0.0, 0.0, 40], [-18.70290941864089, 22.289259491629373, 40], [-37.40581883728178, 44.578518983258746, 40], [-168.326184767768, 200.60333542466435, 40], [-187.02909409518668, 222.89259480757931, 40], [-206.31272238578285, 245.87392810114866, 40]], 'drone1': [[-102.12057962768722, -85.68934070120238, 40], [-110.61185760614786, -54.831940864968885, 40], [-119.1031355846085, -23.974541028735395, 40], [-169.0902977689299, 199.9582460120866, 40], [-208.9459508758687, 247.45636378746948, 40]]}
ACAS_01_1_a = {'drone0': [[0.0, 0.0, 40], [-18.70290941864089, 22.289259491629373, 40]], 'drone1': [[-102.12057962768722, -85.68934070120238, 40], [-110.61185760614786, -54.831940864968885, 40]]}
ACAS_01_1_b = {'drone0': [[-37.40581883728178, 44.578518983258746, 40], [-168.326184767768, 200.60333542466435, 40]], 'drone1': [[-119.1031355846085, -23.974541028735395, 40], [-169.0902977689299, 199.9582460120866, 40]]}
ACAS_01_1_c = {'drone0': [[-187.02909409518668, 222.89259480757931, 40], [-206.31272238578285, 245.87392810114866, 40]], 'drone1': [[-208.9459508758687, 247.45636378746948, 40]]}
ACAS_01_2 = {'drone0': [[0.0, 0.0, 40], [-28.654519660614902, 5.052564935407577, 40], [-57.309039321229804, 10.105129870815153, 40], [-257.89067694553415, 45.473084418668186, 40], [-286.54519646638846, 50.525649329432206, 40], [-316.08942905675474, 55.73509465944012, 40]], 'drone1': [[-23.14885606693754, -131.28368655736995, 40], [-49.488306659190194, -113.10363515868146, 40], [-75.82775725144285, -94.923583759993, 40], [-258.06136598244416, 44.48775488930084, 40], [-319.12376916134036, 55.254704076638575, 40]]}
ACAS_01_3 = {'drone0': [[-0.0, 0.0, 40], [-25.198361693874215, -14.548280907095823, 40], [-50.39672338774843, -29.096561814191645, 40], [-226.78525524486793, -130.9345281638624, 40], [-251.9836168158388, -145.48280899999995, 40], [-277.96437892937195, -160.48280899999992, 40]], 'drone1': [[66.65447451841011, -115.44893641769146, 40], [34.791372974866704, -118.45288155475954, 40], [2.928271431323296, -121.4568266918276, 40], [-226.28265302015862, -131.79905117251045, 40], [-279.9800291905879, -162.80124575928437, 40]]}
ACAS_01_4 = {'drone0': [[-0.0, 0.0, 40], [-9.951610241974015, -27.341824427036943, 40], [-19.90322048394803, -54.68364885407389, 40], [-89.56449217776614, -246.0764198433325, 40], [-99.51610237120182, -273.41824413701147, 40], [-109.77670667097189, -301.6090227605887, 40]], 'drone1': [[125.26943569462473, -45.594345856167564, 40], [102.79178253094307, -68.37670821422658, 40], [80.3141293672614, -91.1590705722856, 40], [-88.62377185818046, -246.4156164074118, 40], [-109.83052193013786, -304.6806833701324, 40]]}
ACAS_01_5 = {'drone0': [[0.0, -0.0, 40], [9.95161024197401, -27.341824427036947, 40], [19.90322048394802, -54.683648854073894, 40], [89.56449217776608, -246.07641984333253, 40], [99.51610237120175, -273.41824413701147, 40], [109.77670667097182, -301.60902276058874, 40]], 'drone1': [[125.26943569462475, 45.59434585616753, 40], [122.69477463738005, 13.693686822207418, 40], [120.12011358013534, -18.206972211752692, 40], [90.50315709975222, -245.73157612076048, 40], [111.7099071717096, -303.9966430834811, 40]]}
ACAS_01_6 = {'drone0': [[0.0, -0.0, 40], [25.1983616938742, -14.548280907095842, 40], [50.3967233877484, -29.096561814191684, 40], [226.7852552448678, -130.93452816386258, 40], [251.98361681583864, -145.48280900000015, 40], [277.96437892937183, -160.48280900000015, 40]], 'drone1': [[66.6544745184102, 115.4489364176914, 40], [85.18751809045757, 89.35665360615369, 40], [103.72056166250496, 63.26437079461597, 40], [227.2826530201585, -130.06700036494172, 40], [280.9800291905878, -161.0691949517157, 40]]}
ACAS_01_7 = {'drone0': [[0.0, 0.0, 40], [28.654519660614906, 5.052564935407563, 40], [57.30903932122981, 10.105129870815126, 40], [257.89067694553415, 45.47308441866807, 40], [286.5451964663885, 50.52564932943208, 40], [316.08942905675474, 55.73509465943998, 40]], 'drone1': [[-23.14885606693748, 131.28368655736995, 40], [7.820075075204812, 123.20864907919547, 40], [38.78900621734711, 115.133611601021, 40], [257.7140696271104, 46.45737039532513, 40], [318.7764728060066, 57.224319582662844, 40]]}
ACAS_01_8 = {'drone0': [[0.0, 0.0, 40], [18.7029094186409, 22.289259491629366, 40], [37.4058188372818, 44.57851898325873, 40], [168.3261847677681, 200.6033354246643, 40], [187.0290940951868, 222.89259480757926, 40], [206.31272238578296, 245.8739281011486, 40]], 'drone1': [[-102.12057962768719, 85.68934070120243, 40], [-73.20646797818983, 99.40994833647406, 40], [-44.29235632869247, 113.13055597174571, 40], [167.55820888269204, 201.2438212314596, 40], [207.41386198963087, 248.7419390068425, 40]]}
ACAS_01_9 = {'drone0': [[0.0, 0.0, 40], [7.126602258388584e-15, 29.09656181419166, 40], [1.425320451677717e-14, 58.19312362838332, 40], [6.413942032549726e-14, 261.86905632772493, 40], [7.12660225491263e-14, 290.965618, 40], [7.861390334401042e-14, 320.965618, 40]], 'drone1': [[-133.30894903682028, 3.265127554712792e-14, 40], [-119.97889106532425, 29.09622794860582, 40], [-106.64883309382823, 58.19245589721161, 40], [-0.9999999999999358, 261.8660515374521, 40], [-0.9999999999999207, 323.870440711, 40]]}

ACAS_01_PLANE = {            
    'drone0': [
        (0, 150, 30), 
        # (0, 350, 30),
        # (0, 550, 30),
        # (0, 750, 30),
        # (0, 950, 30),
        # (0, 1150, 30),
        (0, 950, 30),
    ],
    'drone1': [
        # (-250, 50, 30), 
        # (-150, 150, 30), 
        # (-50, 250, 30),
        (-1, 350, 30), 
        # (-10, 450, 30),
        # (-10, 550, 30),
        # (-10, 650, 30),
        # (-10, 750, 30),
        # (-10, 850, 30),
        (-1, 950, 30),
    ],
    # 'drone1': [
    #     (-133.30894903682029, 0, 30), 
    #     (-106.64883309382825, 58.19245589721158, 30), 
    #     (-10.0, 261.86605153745208, 30),
    #     (-10.0, 361.870440711, 30),        
    #     (-10.0, 411.870440711, 30), 
    #     (-10.0, 461.870440711, 30), 
    #     (-10.0, 511.870440711, 30), 
    #     (-10.0, 561.870440711, 30), 
    #     (-10.0, 611.870440711, 30), 
        
    # ],
}

ACAS_06 = {            
    'drone0': [
        (0, 0.0, 40), 
        (0, 29.09656181419166, 40), 
        (0, 58.19312362838332, 40), 
        (0, 261.86905632772494, 40),
        (0, 290.965618, 40),
        (0, 320.965618, 40)
    ],
    'drone1': [
        (133.30894903682029, 0.0, 40), 
        (119.97889106532426, 29.09622794860579, 40), 
        (106.64883309382825, 58.19245589721158, 40), 
        (1.0, 261.86605153745208, 40),
        (1.0, 323.870440711, 40),        
    ],
}

ACAS_10 = {
    'drone0': [
        (0.0, 0.0, 40),
        (0.0, 174, 40), 
        (20.0, 174, 40),
        # (-20.0, 175.5940014630578, 40),
    ],
    'drone1': [
        (0.0, 350, 40),
        (0.0, 176, 40), 
        (-20.0, 176.0, 40),
        # (20.0, 185.17044623262616, 40),
    ]
}

ACAS_10_plane = {
    'drone0': [
        (0.0, -100.0, 40), 
        (0.0, 600, 40),
    ],
    'drone1': [
        (0.0, 350, 40), 
        (0.0, -300, 40),
    ]
}

# SCENARIO_LIST = [ACAS_01, ACAS_10]

# scenario = ACAS_01_1

# drone0 = np.array(scenario['drone0'])
# drone1 = np.array(scenario['drone1'])

# plt.plot(drone0[:,0], drone0[:,1])
# plt.plot(drone1[:,0], drone1[:,1])
# plt.show()
