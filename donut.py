from colorthief import ColorThief
import matplotlib.pyplot as plt
import numpy as np

def identifyColor(img_path):
    color_thief = ColorThief(img_path)
    dm = color_thief.get_color(quality=1)
    return rgb_to_hex(dm)

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def plot():
    marker_size=15
    xyz=np.array(np.random.random((100,3)))
    plt.scatter(xyz[:,0], xyz[:,1], c=xyz[:,2])
    plt.title("Point observations")
    plt.xlabel("Easting")
    plt.ylabel("Northing")
    cbar= plt.colorbar()
    cbar.set_label("elevation (m)", labelpad=+1)
    print(xyz[:,0])
    print(xyz[:,1])
    print(xyz[:,1])
    plt.show()

if __name__ == '__main__':
    x = identifyColor('/Users/nico/Documents/Images/715a3d6dcdd4225528d79f104e2e0785.gif')
    print(x)
    plot()
