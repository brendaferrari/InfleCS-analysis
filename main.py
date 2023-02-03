import numpy as np
import free_energy_clustering as FEC

data = np.loadtxt('data_c.csv')
print(data)

fec = FEC.FreeEnergyClustering(data, min_n_components=1, max_n_components=10, temperature=300.0, 
                            n_iterations=5, n_grids=80, n_splits=1,stack_landscapes=False)


coords, FE_landscape, FE_points = fec.landscape()

fec.visualize(savefig=True, show_data=False, vmax=7, xlabel='PC1', ylabel='PC2',filename='free_energy_landscape',title='Free energy landscape')

labels, cluster_centers = fec.cluster(coords, FE_points,data, assign_transition_points=False)
print("Cluster center indices: "+str(cluster_centers))
print("Cluster center labels: "+str(labels))

# Computing state populations
state_populations = fec.population_states(n_sampled_points=100000)

# Visualize free energy landscape with cluster labels
fec.pathways_ = None
fec.visualize(savefig=True, vmax=7, show_data=True, xlabel='PC1', ylabel='PC2', filename='InfleCS_clustering', title='InlfeCS clustering')

# Plotting the state populations
import matplotlib.pyplot as plt
plt.figure(figsize=[15,5]);
plt.plot(np.arange(1,state_populations.shape[0]),state_populations[1::]/state_populations.sum(),linewidth=5,color=[0.7,0.7,0.7],zorder=-1)
plt.scatter(np.arange(1,state_populations.shape[0]),state_populations[1::]/state_populations.sum(),s=500,c=np.arange(1,state_populations.shape[0]),cmap='jet',edgecolor='k')
plt.title('State populations',fontsize=30)
plt.xlabel('State',fontsize=28)
plt.ylabel('Probability',fontsize=28)
plt.xticks(np.arange(1,state_populations.shape[0]))
plt.savefig('states.png', bbox_inches='tight')

# Plotting pathways
fec.pathways([cluster_centers[0]],[cluster_centers[1]],max_iter=300,convergence_tol=1e-4,step_size=2e-2,n_points=20)
fec.visualize(savefig=True, vmax=7, show_data=True, xlabel='PC1', ylabel='PC2', filename='pathways', title='')