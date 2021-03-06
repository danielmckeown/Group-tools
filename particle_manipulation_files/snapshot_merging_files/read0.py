import h5py
import numpy as np

#dirname = './halo796_Y13/snapdir_184/'
#dirname = './halo897_Y13/snapdir_184/'
#dirname = './halo897_Y13_stampede/'
#dirname = './halo848_Y13/snapdir_184/'
#dirname = './halo11707_Y13/snapdir_184/'
#dirname = './halo1016_Y13/snapdir_184/'
#dirname = './halo12596_Y13/snapdir_184/'
#dirname = './halo20910_Y13/snapdir_184/'
#dirname = './halo32503_Y13/snapdir_184/'
#dirname = './halo20192_Y13/snapdir_184/'
#dirname = './halo897_Y13/snapdir_184/'
dirname = './snapdir_184/'
import readsnap as reads
# For reading the properties
# Gas
P0=reads.readsnap(dirname,7,0,cosmological=1,loud=1)
# dark matter particles(high res.)
P1=reads.readsnap(dirname,7,1,cosmological=1,loud=1)
# dark matter particles(low res.)
P2=reads.readsnap(dirname,7,2,cosmological=1,loud=1)
P3=reads.readsnap(dirname,7,3,cosmological=1,loud=1)
P5=reads.readsnap(dirname,7,5,cosmological=1,loud=1)
# Stellar particles
P4=reads.readsnap(dirname,7,4,cosmological=1,loud=1)

# This is just for making a copy of the header
file = h5py.File(dirname+'snapshot_184.0.hdf5', 'r')
#stars=file['PartType4']
#coord = stars['Coordinates']
#Masses = stars['Masses']
#Metallicity = stars['Metallicity']
#ParticleIDs = stars['ParticleIDs']
#SFT = stars['StellarFormationTime']
#Vel = stars['Velocities']

#fnew = h5py.File(fname_base+'.'+fname_ext, "w")
fnew = h5py.File(dirname+'snapshot_184'+'.'+'hdf5', "w")
# Creating the header
group_path_S = file['Header'].parent.name
group_id_S = fnew.require_group(group_path_S)
file.copy('Header', group_id_S, name="Header")

# Generating the datasets for the gas 
fnew.create_dataset("PartType0/Coordinates", data=P0['p'])
fnew.create_dataset("PartType0/Velocities", data=P0['v'])
fnew.create_dataset("PartType0/ParticleIDs", data=P0['id'])
fnew.create_dataset("PartType0/Masses", data=P0['m'])
fnew.create_dataset("PartType0/InternalEnergy", data=P0['u'])
fnew.create_dataset("PartType0/Density", data=P0['rho'])
fnew.create_dataset("PartType0/SmoothingLength", data=P0['h'])
fnew.create_dataset("PartType0/ElectronAbundance", data=P0['ne'])
fnew.create_dataset("PartType0/NeutralHydrogenAbundance", data=P0['nh'])
fnew.create_dataset("PartType0/StarFormationRate", data=P0['sfr'])
fnew.create_dataset("PartType0/Metallicity", data=P0['z'])


# Generating the datasets for the hr dark matter particles
fnew.create_dataset("PartType1/Coordinates", data=P1['p'])
fnew.create_dataset("PartType1/Velocities", data=P1['v'])
fnew.create_dataset("PartType1/ParticleIDs", data=P1['id'])
fnew.create_dataset("PartType1/Masses", data=P1['m'])


# Generating the datasets for the lr dark matter particles
fnew.create_dataset("PartType2/Coordinates", data=P2['p'])
fnew.create_dataset("PartType2/Velocities", data=P2['v'])
fnew.create_dataset("PartType2/ParticleIDs", data=P2['id'])
fnew.create_dataset("PartType2/Masses", data=P2['m'])

fnew.create_dataset("PartType3/Coordinates", data=P3['p'])
fnew.create_dataset("PartType3/Velocities", data=P3['v'])
fnew.create_dataset("PartType3/ParticleIDs", data=P3['id'])
fnew.create_dataset("PartType3/Masses", data=P3['m'])

fnew.create_dataset("PartType5/Coordinates", data=P5['p'])
fnew.create_dataset("PartType5/Velocities", data=P5['v'])
fnew.create_dataset("PartType5/ParticleIDs", data=P5['id'])
fnew.create_dataset("PartType5/Masses", data=P5['m'])


# Generaing the datasets for the stelar particles
fnew.create_dataset("PartType4/Coordinates", data=P4['p'])
fnew.create_dataset("PartType4/Masses", data=P4['m'])
fnew.create_dataset("PartType4/Metallicity", data=P4['z'])
fnew.create_dataset("PartType4/ParticleIDs", data=P4['id'])
fnew.create_dataset("PartType4/StellarFormationTime", data=P4['age'])
fnew.create_dataset("PartType4/Velocities", data=P4['v'])


# Just to fix the header ( regarding mass of the dark matter particle )
# This is neccesary for using halo finders, but I think we can skip this fix if we only want to# do post-analysis ( YT ).
header_master2 = fnew["Header"]
header_toparse2 = header_master2.attrs
header_toparse2["NumPart_ThisFile"]=header_toparse2["NumPart_Total"]
# This number is for the particular case of Alex's runs, in case of different resolution level
# it has to be changed
#DM_mass = np.array([ 0.,  1.7439451156263888e-07,  0.,  0.,  0.,  0.])
DM_mass = np.array([ 0.,    3.58481225e-06,  0.,  0.,  0.,  0.])
header_toparse2["MassTable"] = DM_mass
fnew.close()
file.close()

#file2 = h5py.File(dirname+'snapshot_184.hdf5', 'r+')
#header_master2 = file2["Header"]
#header_toparse2 = header_master2.attrs
#header_toparse2["NumPart_ThisFile"]=header_toparse2["NumPart_Total"]
#file2.close()
