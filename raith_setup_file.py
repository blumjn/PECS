def raith_setup(alpha,beta,eta):
#This function sets up the raith and is where the parameters such as pixel size and beamstep get set
#Future plan: make this reference a config file or some proper coding bullshit

    pixel_size = 0.5 #length of 1 pixel in nm, must be <= beamstep
    beamstep = 1 #beam step in nm, must be >= and divisible by pixel_size
    dose = 400 #dose in uC/cm^2
    dose = dose*(beamstep**2) #Accounts for change in area for different beamstep sizes
    exposure = 350 #required exposure in uC/cm^2
    threshold = 0.5 #dose/exposure threshold for full development

    beamstep = int(beamstep/pixel_size) #convert this to be in terms of pixels instead of nm

    raith = [alpha, beta, eta, pixel_size, beamstep, dose, exposure, threshold]
    return raith
