#this section sets up the Raith. In the actual program alpha, beta, and eta will be changed by the wrapping program

def raith_setup(alpha,beta,eta):

    pixel_size = 0.25 #length of 1 pixel in nm

    beamstep = 1 #beam step in nm
    dose = 400 #dose in uC/cm^2
    exposure = 350 #required exposure in uC/cm^2
    threshold = 0.5 #dose/exposure threshold for full development

    alpha = alpha/pixel_size
    beta = beta/pixel_size
    eta = eta/pixel_size

    raith = [alpha, beta, eta, beamstep, dose, exposure, threshold]
    return raith

raith = raith_setup(10,200,1.25)
print(raith)