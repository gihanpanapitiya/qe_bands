def qe_bands(fname):
    import numpy as np
    
    f = open(fname)
    f = f.readlines()

    nbands = int(f[0].split()[2].split(',')[0])

    tot = 0
    c = 2
    # eigs = []
    while tot < nbands:
        tot+=len(f[c].split())
    #     eigs+=f[i].split()
        c+=1

    eigs_all = []
    for i in range(2,len(f),c-1):
        tot = 0
        j=i
        eigs = []
        while tot < nbands:
            tot+=len(f[j].split())
            eigs+=f[j].split()
            j+=1
        eigs_all.append(eigs)

    kpoints = []
    for j in range(1,len(f),c-1):
    #     print(j)
        x = f[j].split()
        x = [float(x[i]) for i in range(len(x))]
        kpoints.append(x)

    kpoints = np.array(kpoints)

    sumd = 0
    kpath_qe = []
    for i in range(1,len(kpoints)):
        dist = np.sqrt(np.sum((kpoints[i]-kpoints[i-1])**2))
    #     print(kpoints_ai[i])

        sumd+=dist
        kpath_qe.append(sumd)

    kpath_qe.insert(0,0)

    eigs_all = np.array(eigs_all).astype(float)
    kpath_qe = np.array(kpath_qe) 
    
    return([eigs_all, kpath_qe])
