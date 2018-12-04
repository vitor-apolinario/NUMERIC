import numpy as np

A = np.matrix([
               [5     , 14.4  ],
               [14.4  , 249.93]
            ])

Y = np.matrix([[12.4885],
               [249.93]
               ])

ATA = ((A.getT() * A).getI()) * A.getT() * Y
print(ATA)
