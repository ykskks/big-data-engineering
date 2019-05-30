import numpy as np
import matplotlib.pyplot as plt


def make_ellipse(n_samples, a, b, x1, y1, rot_deg, scale):
    """Generates n samples that follow x=acos(theta) and y=bsin(theta)"""
    theta = np.arange(0, 2*np.pi, 2*np.pi / n_samples)
    X = a * np.cos(theta)
    Y = b * np.sin(theta)
    original_samples = np.matrix(np.vstack([X, Y]))

    #rotate
    rot_mat = np.matrix([[np.cos(rot_deg), -np.sin(rot_deg)], [np.sin(rot_deg), np.cos(rot_deg)]])
    rot_samples = rot_mat * original_samples

    #add noise 
    X = np.array(rot_samples[0]) + x1 + np.random.normal(scale=scale, size=rot_samples[0].shape)
    Y = np.array(rot_samples[1]) + y1 + np.random.normal(scale=scale, size=rot_samples[1].shape)

    return X, Y 


if __name__ == "__main__":
    x1, y1 = make_ellipse(100, 1, 3, 1, 2, 2*np.pi*(1/8), 0.2)
    x2, y2 = make_ellipse(100, 0.4, 5, 0, -6, 0, 0.2)
    x3, y3 = make_ellipse(100, 0.3, 6, -2, -14, 0, 0.2)

    #plt.plot(x1, y1, marker='o', color='b')
    #plt.plot(x2, y2, marker='o', color='b')
    #plt.plot(x3, y3, marker='o', color='b')
    #plt.show()

    #save as csv
    samples = np.hstack([np.vstack([x1, y1]), np.vstack([x2, y2]), np.vstack([x3, y3])]).transpose()
    np.savetxt("my_data.csv", samples, delimiter=",")