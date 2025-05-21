def raith_setup(alpha,beta,eta):
#This function sets up the raith and is where the parameters such as pixel size and beamstep get set
#Future plan: make this reference a config file or some proper coding bullshit

    pixel_size = 0.25 #length of 1 pixel in nm
    beamstep = 1 #beam step in nm
    dose = 400 #dose in uC/cm^2
    exposure = 350 #required exposure in uC/cm^2
    threshold = 0.5 #dose/exposure threshold for full development

    alpha = alpha/pixel_size #convert this to be in terms of pixels instead of nm
    beta = beta/pixel_size #convert this to be in terms of pixels instead of nm
    eta = eta/pixel_size #convert this to be in terms of pixels instead of nm

    raith = [alpha, beta, eta, beamstep, dose, exposure, threshold]
    return raith
