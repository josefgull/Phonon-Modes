# Phonon-Modes (Motion of crystal lattice Atoms)
Hi, here I want to save visualizations of phonon modes in Python.
I have already done 
## acoustic modes: 
![Alt Text](./AcousticPhononModes.gif)
All crystal atoms lay at the planes in the picture above  


The displacement $D$ of those planes in transversal modes is given as:   
D(x,t) = **A** $\sin$(kx - $\omega$ t)  
Where $k$ is the inverse of the length of one oscillation in space  
and $\omega$ is the inverse of the duration of one oscillation in time.


The wavenumber $k(\omega)$ is a function of $\omega$.  
The exact expression follows from the solution of Schrödinger's equation of the potential that is given through the lattice atoms.  
So the function $k(\omega)$ is unique for every material. 


As $k$ gets higher, the point is reached where the spatial period is shorter than the distance between 2 atomic planes.
This means the Nyquist criterion is violated (more than two points/spacial period are needed to identify the frequency of a sinewave through these points) and aliasing effects can be seen.

At this point, the domain of optical phonons is entered. 



now I want to do the optic ones as well. 
