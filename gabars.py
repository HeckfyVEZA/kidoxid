# [B, H]
def kid_1_2(S):
    B = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
    H = [175, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
    ses = [[0.025, 0.032, 0.039, 0.045, 0.052, 0.059, 0.066, 0.073, 0.079, 0.086, 0.093, 0.100, 0.107, 0.113, 0.120, 0.127, 0.134],[0.030, 0.038, 0.046, 0.054, 0.062, 0.070, 0.078, 0.086, 0.094, 0.102, 0.110, 0.118, 0.126, 0.134, 0.142, 0.150, 0.159],[0.036, 0.046, 0.056, 0.065, 0.075, 0.085, 0.095, 0.105, 0.114, 0.124, 0.134, 0.144, 0.154, 0.163, 0.173, 0.183, 0.193],[0.045, 0.058, 0.070, 0.082, 0.095, 0.107, 0.119, 0.131, 0.144, 0.156, 0.168, 0.181, 0.193, 0.205, 0.218, 0.230, 0.242],[0.052, 0.066, 0.080, 0.094, 0.108, 0.122, 0.136, 0.150, 0.164, 0.178, 0.192, 0.206, 0.220, 0.234, 0.248, 0.262, 0.276],[0.061, 0.077, 0.094, 0.111, 0.127, 0.144, 0.160, 0.177, 0.193, 0.210, 0.226, 0.243, 0.260, 0.276, 0.293, 0.309, 0.326],[0.067, 0.086, 0.104, 0.122, 0.140, 0.159, 0.177, 0.195, 0.214, 0.232, 0.250, 0.269, 0.287, 0.305, 0.323, 0.342, 0.360],[0.077, 0.097, 0.118, 0.139, 0.160, 0.181, 0.201, 0.222, 0.243, 0.264, 0.285, 0.305, 0.326, 0.347, 0.368, 0.389, 0.409],[0.083, 0.105, 0.128, 0.150, 0.173, 0.196, 0.218, 0.241, 0.263, 0.286, 0.308, 0.331, 0.353, 0.376, 0.399, 0.421, 0.444],[0.092, 0.117, 0.142, 0.167, 0.192, 0.217, 0.242, 0.267, 0.293, 0.318, 0.343, 0.368, 0.393, 0.418, 0.443, 0.468, 0.493],[0.098, 0.125, 0.152, 0.179, 0.206, 0.232, 0.259, 0.286, 0.313, 0.340, 0.366, 0.393, 0.420, 0.447, 0.474, 0.500, 0.527],[0.108, 0.137, 0.166, 0.196, 0.225, 0.254, 0.284, 0.313, 0.342, 0.371, 0.401, 0.430, 0.459, 0.489, 0.518, 0.547, 0.577],[0.114, 0.145, 0.176, 0.207, 0.238, 0.269, 0.300, 0.331, 0.362, 0.393, 0.425, 0.456, 0.487, 0.518, 0.549, 0.580, 0.611],[0.123, 0.157, 0.190, 0.224, 0.258, 0.291, 0.325, 0.358, 0.392, 0.425, 0.459, 0.492, 0.526, 0.559, 0.593, 0.627, 0.660],[0.130, 0.165, 0.200, 0.236, 0.271, 0.306, 0.341, 0.377, 0.412, 0.447, 0.483, 0.518, 0.553, 0.589, 0.624, 0.659, 0.694],[0.139, 0.177, 0.215, 0.252, 0.290, 0.328, 0.366, 0.404, 0.441, 0.479, 0.517, 0.555, 0.593, 0.630, 0.668, 0.706, 0.744],[0.145, 0.185, 0.224, 0.264, 0.303, 0.343, 0.383, 0.422, 0.462, 0.501, 0.541, 0.580, 0.620, 0.659, 0.699, 0.738, 0.778],[0.155, 0.197, 0.239, 0.281, 0.323, 0.365, 0.407, 0.449, 0.491, 0.533, 0.575, 0.617, 0.659, 0.701, 0.743, 0.785, 0.827]]
    abyr = [[H[i],B[j],round(((ses[i][j]/S)-1)*100, 1)] for i in range(len(ses)) for j in range(len(ses[i])) if ses[i][j]>=S]
    return [item for item in abyr if item[-1]<10]
def kid_3(S):
    B = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
    H = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
    ses = [[0.017, 0.024, 0.030, 0.037, 0.043, 0.050, 0.057, 0.063, 0.070, 0.076, 0.083, 0.089, 0.096, 0.102, 0.109, 0.116, 0.122, 0.129],[0.021, 0.029, 0.037, 0.045, 0.053, 0.062, 0.070, 0.078, 0.086, 0.094, 0.102, 0.110, 0.118, 0.126, 0.134, 0.142, 0.150, 0.158],[0.028, 0.038, 0.049, 0.060, 0.070, 0.081, 0.091, 0.102, 0.112, 0.123, 0.133, 0.144, 0.154, 0.165, 0.176, 0.186, 0.197, 0.207],[0.031, 0.043, 0.055, 0.067, 0.078, 0.090, 0.102, 0.114, 0.126, 0.137, 0.149, 0.161, 0.173, 0.185, 0.196, 0.208, 0.220, 0.232],[0.038, 0.053, 0.068, 0.082, 0.097, 0.111, 0.126, 0.140, 0.155, 0.169, 0.184, 0.198, 0.213, 0.228, 0.242, 0.257, 0.271, 0.286],[0.045, 0.062, 0.079, 0.096, 0.113, 0.130, 0.147, 0.164, 0.181, 0.198, 0.216, 0.233, 0.250, 0.267, 0.284, 0.301, 0.318, 0.335],[0.049, 0.068, 0.086, 0.105, 0.123, 0.142, 0.160, 0.179, 0.197, 0.216, 0.234, 0.253, 0.272, 0.290, 0.309, 0.327, 0.346, 0.364],[0.056, 0.077, 0.098, 0.119, 0.140, 0.161, 0.182, 0.203, 0.224, 0.245, 0.266, 0.287, 0.308, 0.329, 0.350, 0.371, 0.392, 0.413],[0.059, 0.081, 0.103, 0.126, 0.148, 0.170, 0.193, 0.215, 0.237, 0.260, 0.282, 0.304, 0.326, 0.349, 0.371, 0.393, 0.416, 0.438],[0.066, 0.091, 0.116, 0.141, 0.166, 0.191, 0.216, 0.241, 0.267, 0.292, 0.317, 0.342, 0.367, 0.392, 0.417, 0.442, 0.467, 0.492],[0.073, 0.100, 0.128, 0.155, 0.183, 0.210, 0.238, 0.266, 0.293, 0.321, 0.348, 0.376, 0.403, 0.431, 0.458, 0.486, 0.514, 0.541],[0.077, 0.106, 0.135, 0.164, 0.193, 0.222, 0.251, 0.280, 0.309, 0.338, 0.367, 0.396, 0.425, 0.454, 0.483, 0.512, 0.541, 0.571],[0.083, 0.115, 0.146, 0.178, 0.209, 0.241, 0.273, 0.304, 0.336, 0.367, 0.399, 0.430, 0.462, 0.493, 0.525, 0.557, 0.588, 0.620],[0.087, 0.119, 0.152, 0.185, 0.218, 0.251, 0.283, 0.316, 0.349, 0.382, 0.415, 0.447, 0.480, 0.513, 0.546, 0.579, 0.611, 0.644],[0.094, 0.129, 0.165, 0.201, 0.236, 0.272, 0.307, 0.343, 0.378, 0.414, 0.449, 0.485, 0.520, 0.556, 0.592, 0.627, 0.663, 0.698],[0.100, 0.139, 0.177, 0.215, 0.253, 0.291, 0.329, 0.367, 0.405, 0.443, 0.481, 0.519, 0.557, 0.595, 0.633, 0.671, 0.709, 0.747],[0.104, 0.144, 0.184, 0.223, 0.263, 0.302, 0.342, 0.381, 0.421, 0.460, 0.500, 0.539, 0.579, 0.619, 0.658, 0.698, 0.737, 0.777]]
    abyr = [[H[i],B[j],round(((ses[i][j]/S)-1)*100, 1)] for i in range(len(ses)) for j in range(len(ses[i])) if ses[i][j]>=S]
    return [item for item in abyr if item[-1]<10]
def oksid_canal(S):
    A = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]
    B = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]
    ses = [[0.024, 0.032, 0.041, 0.049, 0.058, 0.066, 0.075, 0.083, 0.092, 0.100, 0.109, 0.117, 0.126, 0.134, 0.143, 0.151, 0.160, 0.168, 0.177, 0.185, 0.194, 0.202],[0.031, 0.042, 0.053, 0.064, 0.075, 0.086, 0.097, 0.108, 0.119, 0.130, 0.141, 0.152, 0.163, 0.174, 0.185, 0.196, 0.207, 0.218, 0.229, 0.240, 0.251, 0.262],[0.038, 0.051, 0.065, 0.078, 0.092, 0.105, 0.119, 0.132, 0.146, 0.159, 0.173, 0.186, 0.200, 0.213, 0.227, 0.240, 0.254, 0.267, 0.281, 0.294, 0.308, 0.321],[0.045, 0.061, 0.077, 0.093, 0.109, 0.125, 0.141, 0.157, 0.173, 0.189, 0.205, 0.221, 0.237, 0.253, 0.269, 0.285, 0.301, 0.317, 0.333, 0.349, 0.365, 0.381],[0.052, 0.070, 0.089, 0.107, 0.126, 0.144, 0.163, 0.181, 0.200, 0.218, 0.237, 0.255, 0.274, 0.292, 0.311, 0.329, 0.348, 0.366, 0.385, 0.403, 0.422, 0.440],[0.056, 0.076, 0.096, 0.116, 0.136, 0.156, 0.176, 0.196, 0.216, 0.236, 0.256, 0.276, 0.296, 0.316, 0.336, 0.356, 0.376, 0.396, 0.416, 0.436, 0.456, 0.476],[0.063, 0.085, 0.108, 0.130, 0.153, 0.175, 0.198, 0.220, 0.243, 0.265, 0.288, 0.310, 0.333, 0.355, 0.378, 0.400, 0.423, 0.445, 0.468, 0.490, 0.513, 0.535],[0.070, 0.095, 0.120, 0.145, 0.170, 0.195, 0.220, 0.245, 0.270, 0.295, 0.320, 0.345, 0.370, 0.395, 0.420, 0.445, 0.470, 0.495, 0.520, 0.545, 0.570, 0.595],[0.077, 0.104, 0.132, 0.159, 0.187, 0.214, 0.242, 0.269, 0.297, 0.324, 0.352, 0.379, 0.407, 0.434, 0.462, 0.489, 0.517, 0.544, 0.572, 0.599, 0.627, 0.654],[0.084, 0.114, 0.144, 0.174, 0.204, 0.234, 0.264, 0.294, 0.324, 0.354, 0.384, 0.414, 0.444, 0.474, 0.504, 0.534, 0.564, 0.594, 0.624, 0.654, 0.684, 0.714],[0.091, 0.123, 0.156, 0.188, 0.221, 0.253, 0.286, 0.318, 0.351, 0.383, 0.416, 0.448, 0.481, 0.513, 0.546, 0.578, 0.611, 0.643, 0.676, 0.708, 0.741, 0.773],[0.098, 0.133, 0.168, 0.203, 0.238, 0.273, 0.308, 0.343, 0.378, 0.413, 0.448, 0.483, 0.518, 0.553, 0.588, 0.623, 0.658, 0.693, 0.728, 0.763, 0.798, 0.833],[0.105, 0.142, 0.180, 0.217, 0.255, 0.292, 0.330, 0.367, 0.405, 0.442, 0.480, 0.517, 0.555, 0.592, 0.630, 0.667, 0.705, 0.742, 0.780, 0.817, 0.855, 0.892],[0.109, 0.148, 0.187, 0.226, 0.265, 0.304, 0.343, 0.382, 0.421, 0.460, 0.499, 0.538, 0.577, 0.616, 0.655, 0.694, 0.733, 0.772, 0.811, 0.850, 0.889, 0.928],[0.116, 0.157, 0.199, 0.240, 0.282, 0.323, 0.365, 0.406, 0.448, 0.489, 0.531, 0.572, 0.614, 0.655, 0.697, 0.738, 0.780, 0.821, 0.863, 0.904, 0.946, 0.987],[0.123, 0.167, 0.211, 0.255, 0.299, 0.343, 0.387, 0.431, 0.475, 0.519, 0.563, 0.607, 0.651, 0.695, 0.739, 0.783, 0.827, 0.871, 0.915, 0.959, 1.003, 1.047],[0.130, 0.176, 0.223, 0.269, 0.316, 0.362, 0.409, 0.455, 0.502, 0.548, 0.595, 0.641, 0.688, 0.734, 0.781, 0.827, 0.874, 0.920, 0.967, 1.013, 1.060, 1.106],[0.137, 0.186, 0.235, 0.284, 0.333, 0.382, 0.431, 0.480, 0.529, 0.578, 0.627, 0.676, 0.725, 0.774, 0.823, 0.872, 0.921, 0.970, 1.019, 1.068, 1.117, 1.166],[0.144, 0.195, 0.247, 0.298, 0.350, 0.401, 0.453, 0.504, 0.556, 0.607, 0.659, 0.710, 0.762, 0.813, 0.865, 0.916, 0.968, 1.019, 1.071, 1.122, 1.174, 1.225],[0.151, 0.205, 0.259, 0.313, 0.367, 0.421, 0.475, 0.529, 0.583, 0.637, 0.691, 0.745, 0.799, 0.853, 0.907, 0.961, 1.015, 1.069, 1.123, 1.177, 1.231, 1.285],[0.158, 0.214, 0.271, 0.327, 0.384, 0.440, 0.497, 0.553, 0.610, 0.666, 0.723, 0.779, 0.836, 0.892, 0.949, 1.005, 1.062, 1.118, 1.175, 1.231, 1.288, 1.344]]
    abyr = [[B[i],A[j],round(((ses[i][j]/S)-1)*100, 1)] for i in range(len(ses)) for j in range(len(ses[i])) if ses[i][j]>=S]
    return [item for item in abyr if item[-1]<10]
def oksid_wall(S):
    A = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]
    B = [230, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1230]
    ses = [[0.018, 0.026, 0.035, 0.043, 0.052, 0.060, 0.069, 0.077, 0.086, 0.094, 0.103, 0.111, 0.120, 0.128, 0.137, 0.145, 0.154, 0.162, 0.171, 0.179, 0.188, 0.196],[0.020, 0.030, 0.039, 0.049, 0.058, 0.068, 0.077, 0.087, 0.096, 0.106, 0.115, 0.125, 0.134, 0.144, 0.153, 0.163, 0.172, 0.182, 0.191, 0.201, 0.210, 0.220],[0.026, 0.038, 0.050, 0.062, 0.074, 0.086, 0.098, 0.110, 0.122, 0.134, 0.146, 0.158, 0.170, 0.182, 0.194, 0.206, 0.218, 0.230, 0.242, 0.254, 0.266, 0.278],[0.031, 0.046, 0.060, 0.075, 0.089, 0.104, 0.118, 0.133, 0.147, 0.162, 0.176, 0.191, 0.205, 0.220, 0.234, 0.249, 0.263, 0.278, 0.292, 0.307, 0.321, 0.336],[0.037, 0.054, 0.071, 0.088, 0.105, 0.122, 0.139, 0.156, 0.173, 0.190, 0.207, 0.224, 0.241, 0.258, 0.275, 0.292, 0.309, 0.326, 0.343, 0.360, 0.377, 0.394],[0.039, 0.058, 0.076, 0.095, 0.113, 0.132, 0.150, 0.169, 0.187, 0.206, 0.224, 0.243, 0.261, 0.280, 0.298, 0.317, 0.335, 0.354, 0.372, 0.391, 0.409, 0.428],[0.045, 0.066, 0.087, 0.108, 0.129, 0.150, 0.171, 0.192, 0.213, 0.234, 0.255, 0.276, 0.297, 0.318, 0.339, 0.360, 0.381, 0.402, 0.423, 0.444, 0.465, 0.486],[0.050, 0.074, 0.097, 0.121, 0.144, 0.168, 0.191, 0.215, 0.238, 0.262, 0.285, 0.309, 0.332, 0.356, 0.379, 0.403, 0.426, 0.450, 0.473, 0.497, 0.520, 0.544],[0.056, 0.082, 0.108, 0.134, 0.160, 0.186, 0.212, 0.238, 0.264, 0.290, 0.316, 0.342, 0.368, 0.394, 0.420, 0.446, 0.472, 0.498, 0.524, 0.550, 0.576, 0.602],[0.061, 0.090, 0.118, 0.147, 0.175, 0.204, 0.232, 0.261, 0.289, 0.318, 0.346, 0.375, 0.403, 0.432, 0.460, 0.489, 0.517, 0.546, 0.574, 0.603, 0.631, 0.660],[0.067, 0.098, 0.129, 0.160, 0.191, 0.222, 0.253, 0.284, 0.315, 0.346, 0.377, 0.408, 0.439, 0.470, 0.501, 0.532, 0.563, 0.594, 0.625, 0.656, 0.687, 0.718],[0.072, 0.106, 0.139, 0.173, 0.206, 0.240, 0.273, 0.307, 0.340, 0.374, 0.407, 0.441, 0.474, 0.508, 0.541, 0.575, 0.608, 0.642, 0.675, 0.709, 0.742, 0.776],[0.078, 0.114, 0.150, 0.186, 0.222, 0.258, 0.294, 0.330, 0.366, 0.402, 0.438, 0.474, 0.510, 0.546, 0.582, 0.618, 0.654, 0.690, 0.726, 0.762, 0.798, 0.834],[0.080, 0.118, 0.155, 0.193, 0.230, 0.268, 0.305, 0.343, 0.380, 0.418, 0.455, 0.493, 0.530, 0.568, 0.605, 0.643, 0.680, 0.718, 0.755, 0.793, 0.830, 0.868],[0.086, 0.126, 0.166, 0.206, 0.246, 0.286, 0.326, 0.366, 0.406, 0.446, 0.486, 0.526, 0.566, 0.606, 0.646, 0.686, 0.726, 0.766, 0.806, 0.846, 0.886, 0.926],[0.091, 0.134, 0.176, 0.219, 0.261, 0.304, 0.346, 0.389, 0.431, 0.474, 0.516, 0.559, 0.601, 0.644, 0.686, 0.729, 0.771, 0.814, 0.856, 0.899, 0.941, 0.984],[0.097, 0.142, 0.187, 0.232, 0.277, 0.322, 0.367, 0.412, 0.457, 0.502, 0.547, 0.592, 0.637, 0.682, 0.727, 0.772, 0.817, 0.862, 0.907, 0.952, 0.997, 1.042],[0.102, 0.150, 0.197, 0.245, 0.292, 0.340, 0.387, 0.435, 0.482, 0.530, 0.577, 0.625, 0.672, 0.720, 0.767, 0.815, 0.862, 0.910, 0.957, 1.005, 1.052, 1.100],[0.108, 0.158, 0.208, 0.258, 0.308, 0.358, 0.408, 0.458, 0.508, 0.558, 0.608, 0.658, 0.708, 0.758, 0.808, 0.858, 0.908, 0.958, 1.008, 1.058, 1.108, 1.158],[0.113, 0.166, 0.218, 0.271, 0.323, 0.376, 0.428, 0.481, 0.533, 0.586, 0.638, 0.691, 0.743, 0.796, 0.848, 0.901, 0.953, 1.006, 1.058, 1.111, 1.163, 1.216],[0.119, 0.174, 0.229, 0.284, 0.339, 0.394, 0.449, 0.504, 0.559, 0.614, 0.669, 0.724, 0.779, 0.834, 0.889, 0.944, 0.999, 1.054, 1.109, 1.164, 1.219, 1.274],[0.122, 0.178, 0.235, 0.291, 0.348, 0.404, 0.461, 0.517, 0.574, 0.630, 0.687, 0.743, 0.800, 0.856, 0.913, 0.969, 1.026, 1.082, 1.139, 1.195, 1.252, 1.308]]
    abyr = [[B[i],A[j],round(((ses[i][j]/S)-1)*100, 1)] for i in range(len(ses)) for j in range(len(ses[i])) if ses[i][j]>=S]
    return [item for item in abyr if item[-1]<10]
def gabars_choose(valve, S, valve_type=None, blya=None, ron=None, isp=None, mrp=None, kan_wall=None):
    if valve == "КИД":
        if valve_type == 3:
            spisok = sorted([f"КИД-{item[1]}*{item[0]}-{blya}-{valve_type}-УХЛ2 | {item[2]}%" for item in kid_3(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            S/=2
            spisok += sorted([f"КИД-{2*(item[1]+30)}*{item[0]}-{blya}-{valve_type}-УХЛ2  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in kid_3(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            spisok += sorted([f"КИД-{item[1]}*{(item[0]+30)*2}-{blya}-{valve_type}-УХЛ2  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in kid_3(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            S/=2
            spisok += sorted([f"КИД-{2*(item[1]+30)}*{(item[0]+30)*2}-{blya}-{valve_type}-УХЛ2  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in kid_3(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            return spisok
        elif valve_type == 2:
            spisok = sorted([f"КИД-{item[1]}*{item[0]}-{blya}-{valve_type}-УХЛ2 | {item[2]}%" for item in kid_1_2(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            S/=2
            spisok += sorted([f"КИД-{2*(item[1]+30)}*{item[0]}-{blya}-{valve_type}-УХЛ2  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in kid_1_2(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            spisok += sorted([f"КИД-{item[1]}*{(item[0]+30)*2}-{blya}-{valve_type}-УХЛ2  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in kid_1_2(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            S/=2
            spisok += sorted([f"КИД-{2*(item[1]+30)}*{(item[0]+30)*2}-{blya}-{valve_type}-УХЛ2  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in kid_1_2(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            return spisok
        else:
            spisok = sorted([f"КИД-{item[1]}*{item[0]}-{blya}-{valve_type}-УХЛ2 | {item[2]}%" for item in kid_1_2(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            S/=2
            spisok += sorted([f"КИД-{2*(item[1]+50)}*{item[0]}-{blya}-{valve_type}-УХЛ2  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in kid_1_2(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            spisok += sorted([f"КИД-{item[1]}*{(item[0]+50)*2}-{blya}-{valve_type}-УХЛ2  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in kid_1_2(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            S/=2
            spisok += sorted([f"КИД-{2*(item[1]+50)}*{(item[0]+50)*2}-{blya}-{valve_type}-УХЛ2  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in kid_1_2(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            return spisok
    else:
        if kan_wall=='канальный':
            sten_kla = '2*ф'
            spisok = sorted([f"ОКСИД-{item[1]}*{item[0]}-{sten_kla}-{isp}-{ron}-{mrp} | {item[2]}%" for item in oksid_canal(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            S/=2
            spisok += sorted([f"ОКСИД-{(item[1]+30)*2}*{item[0]}-{sten_kla}-{isp}-{ron}-{mrp}  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in oksid_canal(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            spisok += sorted([f"ОКСИД-{item[1]}*{(item[0]+30)*2}-{sten_kla}-{isp}-{ron}-{mrp}  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in oksid_canal(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            S/=2
            spisok += sorted([f"ОКСИД-{(item[1]+30)*2}*{(item[0]+30)*2}-{sten_kla}-{isp}-{ron}-{mrp}  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in oksid_canal(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            return spisok
        else:
            sten_kla = '1*ф'
            spisok = sorted([f"ОКСИД-{item[1]}*{item[0]}-{sten_kla}-{isp}-{ron}-{mrp} | {item[2]}%" for item in oksid_wall(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            S/=2
            spisok += sorted([f"ОКСИД-{(item[1]+50)*2}*{item[0]}-{sten_kla}-{isp}-{ron}-{mrp}  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in oksid_wall(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            spisok += sorted([f"ОКСИД-{item[1]}*{(item[0]+50)*2}-{sten_kla}-{isp}-{ron}-{mrp}  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in oksid_wall(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            S/=2
            spisok += sorted([f"ОКСИД-{(item[1]+50)*2}*{(item[0]+50)*2}-{sten_kla}-{isp}-{ron}-{mrp}  (клапан будет изготовлен в кассетном исполнении) | {item[2]}%" for item in oksid_wall(S)], key=lambda x: float(x.split(' | ')[-1][:-1]))
            return spisok