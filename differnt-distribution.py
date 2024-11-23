import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.kdeplot(random.uniform(size=1000))
sns.kdeplot(random.uniform(size=2000))
plt.title("Uniform Distribution")
plt.show()
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.kdeplot(random.rayleigh(size=100))
sns.kdeplot(random.rayleigh (size=1000))
sns.kdeplot(random.rayleigh (size=5000))
plt.title("Rayleigh Distribution")
plt.show()
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import seaborn as sns
sns.kdeplot(bernoulli.rvs(size=1000, p=0.6))
plt.title("Bernoulli Distribution")
plt.show()
from scipy.stats import binom
import matplotlib.pyplot as plt
import seaborn as sns
sns.kdeplot(binom.rvs(n=10, p=0.5, size=10))
plt.title("Binomial Distribution")
plt.show()
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.kdeplot(random.normal(size=1000))
plt.title("Gaussian Distribution")
plt.show()
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.kdeplot(random.exponential (size=1000))
plt.title("Exponential Distribution")
plt.show()
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.kdeplot(random.poisson(lam-50, size=1000))
sns.kdeplot(random.poisson(lam=50,size=2000))
plt.title("Poisson Distribution")
plt.show()
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.kdeplot(random.geometric(p=0.2, size=1000))
plt.title("Geometric Distribution ")
plt.show()