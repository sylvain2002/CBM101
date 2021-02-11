print("Because we assume that the system is inhomogeneous, we have to discretize the membrane in a 2D grid. To simplify we use a rectangular grid of size hX along the X axis and hY along the Y axis, and therefore the (i,j) sub-volume (here, a sub-surface) is located at the x and y coordinates x=i*hX, y=j*hY. Within each of the surface elements (i,j), the reactions are the following:")
print(" Reaction 1ij: dimerization of a molecule P, P(i,j)+P(i,j)->PP(i,j), with propensity kdim/2*n_P(i,j)*(n_P(i,j)-1) where n_P(i,j) is the number of proteins P in the surface element (i,j);")
print(" Reaction 2ij: dissociation of a dimer , with propensity kdiss*n_PP(i,j) where n_PP(i,j) is the number of PP dimers in the surface element (i,j);")
print(" Reaction 3ij: the transport of a protein to the next element along the x axis, P(i,j)->P(i+1,j), with propensity (Dp/hX^2)*n_P(i,j) (where Dp is the diffusion coefficient for proteins)")
print(" Reaction 4ij: the transport of a protein from the next element along the x axis, P(i+1,j)->P(i,j), with propensity (Dp/hX^2)*n_P(i+1,j)")
print(" Reaction 5ij: the transport of a protein to the next element along the y axis, P(i,j)->P(i,j+1), with propensity (Dp/hY^2)*n_P(i,j) ")
print(" Reaction 6ij: the transport of a protein from the next element along the y axis, P(i,j+1)->P(i,j), with propensity (Dp/hY^2)*n_P(i,j+1) ")
print("the exchange of molecules with the neighbor elements (i-1,j) and (i,j-1) are taken into account when we write the transport reactions for the elements (i-1,j) and (i,j-1) so we don't add them to the reaction list for (i,j), otherwise those reactions would be counted twice.")
print(" In addition, we have the transport of the dimers, which we assume can happen at a different propensity governed by a different diffusion coefficient Dpp:")

print(" Reaction 7ij: the transport of a dimer to the next element along the x axis, PP(i,j)->PP(i+1,j), with propensity (Dpp/hX^2)*n_PP(i,j) (where Dpp is the diffusion coefficient for protein dimers")
print(" Reaction 8ij: the transport of a dimer from the next element along the x axis, PP(i+1,j)->PP(i,j), with propensity (Dpp/hX^2)*n_PP(i+1,j) ")
print(" Reaction 9ij: the transport of a dimer to the next element along the y axis, PP(i,j)->PP(i,j+1), with propensity (Dpp/hY^2)*n_PP(i,j) ")
print(" Reaction 10ij: the transport of a dimer from the next element along the y axis, PP(i,j+1)->PP(i,j), with propensity (Dpp/hY^2)*n_PP(i,j+1)")

print("")
print("In summary, all the elementary processes that can happen within the system at the microscopic scale can be accounted for by a list of 10 reactions within each of the small surface elements (i,j) of the discretized surface. For instance, if there are 100 grid points along each axis, that´s a total of 100,000 possible elementary reactions, which could be significantly longer to simulate.")