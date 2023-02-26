import matplotlib.pyplot as plt
import numpy as np
from Conventions import PMNSDefine
from Conventions import vectors

def main():
    Params()
    #Plot2D()
    Plot3D()
    

def Params():

    Param = PMNSDefine.MixingParams()

    print(Param.theta12)
    Param.updatetheta(theta12=0.5, theta13=0.6)
    print(Param.theta12)
    print(Param.theta23)
    print(Param.theta13)
    print(sum(len(x) for x in Param.PMNS)) 
    print(Param.PMNS[2,0])

def Plot3D():
    # Create a new figure and axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the vector components in a list
    v = []

    v.append(vectors.Vector3D(1, 0, 0, 'x axis')) #x axis 
    v.append(vectors.Vector3D(0, 1, 0, 'y axis')) #y axis
    v.append(vectors.Vector3D(0, 0, 1, 'z axis')) #z axis

    #perform rotations to find e, mu, tau. 

    v.append(vectors.Vector3D(-0.6, 0.4, 0.3, 'placeholder')) #placeholder 
    v.append(vectors.Vector3D(0.9, 0.5, 0.1, 'placeholder')) #placeholder
    v.append(vectors.Vector3D(0.3, -0.4, -0.7, 'placeholder')) #placeholder

   # for j in range(9):
   #     v.append(vectors.Vector3D(j/10, j/10, j/10)) #placeholder TODO:FIX COLOUR ITERATION.


    #plot vectors
    for i in range(len(v)):
        # Plot the vector as an arrow
        ax.quiver(0, 0, 0, v[i].x, v[i].y, v[i].z, arrow_length_ratio=0.1, color=v[i].colour, label=f'{v[i].name}')
        ax.text((v[i].x)*1.1, (v[i].y)*1.1, (v[i].z)*1.1, f'{v[i].name}', color=v[i].colour)

        # Plot lines to touch the x, y, and z planes
        ax.plot([v[i].x, 0], [v[i].y, v[i].y], [v[i].z, v[i].z], linestyle='--', color=v[i].colour) # from vector tip to x
        ax.plot([v[i].x, v[i].x], [v[i].y, 0], [v[i].z, v[i].z], linestyle='--', color=v[i].colour) # from vector tip to y
        ax.plot([v[i].x, v[i].x], [v[i].y, v[i].y], [v[i].z, 0], linestyle='--', color=v[i].colour) # from vector tip to z

        ax.plot([0, 0], [v[i].y, v[i].y], [v[i].z, 0], linestyle='--', color=v[i].colour) # x=0, y=y 
        ax.plot([v[i].x, 0], [0, 0], [v[i].z, v[i].z], linestyle='--', color=v[i].colour) # y=0, z=z 
        ax.plot([v[i].x, v[i].x], [v[i].y, 0], [0, 0], linestyle='--', color=v[i].colour) # z=0, x=x

        ax.plot([0, 0], [v[i].y, 0], [v[i].z, v[i].z], linestyle='--', color=v[i].colour) # x=0, z=z 
        ax.plot([v[i].x, v[i].x], [0, 0], [v[i].z, 0], linestyle='--', color=v[i].colour) # y=0, x=x 
        ax.plot([v[i].x, 0], [v[i].y, v[i].y], [0, 0], linestyle='--', color=v[i].colour) # z=0, y=y

        ax.plot([0, 0], [0, 0], [v[i].z, 0], linestyle='--', color=v[i].colour) # x=0, y=0, 
        ax.plot([v[i].x, 0], [0, 0], [0, 0], linestyle='--', color=v[i].colour) # y=0, z=0 
        ax.plot([0, 0], [v[i].y, 0], [0, 0], linestyle='--', color=v[i].colour) # z=0, x=0


    # Set the x, y, and z limits of the axis
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    #legend
    #ax.legend()


    # Hide the axis
    ax.set_axis_off()

    # Show the plot
    #bbox_inches=10
    plt.margins(1)
    plt.show()
    
if __name__ == "__main__":
    main()