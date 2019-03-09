import math
import Tkinter as tk

def calculate_temp(distance, dist_unit, sun_luminosity, albedo):
	if dist_unit.lower() == "au":
		distance = distance * 149597870700 # There are about 150 billion meters in an AU
	elif dist_unit.lower() == "miles":
		distance = distance * 1609.34 # There are about 1600 meters in a mile
	elif dist_unit.lower() == "kilometer" or dist_unit.lower() == "km":
		distance = distance * 1000 # There are 1000 meters in a kilometer
	elif dist_unit.lower() == "meter" or dist_unit.lower() == "m":
		distance = distance # There is 1 meter in 1 meter.
	else:
		return 0
	
	lum_watts = sun_luminosity * (3.828*(10**26)) # 1 Solar Luminosity is equal to 3.828 x 10^26 Watts
	sb_constant = 5.670373 * (10**-8) # Stefan-Boltzmann Constant
	
	#                           lum * (1 - a)^0.25
	# Equilibrium Temp = ----------------------------------
	#                    16 * sb_constant * pi * distance^2 * emissivity (this number is usually close to one, so we ignore it)
	return ((lum_watts*(1-albedo))/(16*sb_constant*math.pi*(distance**2)))**0.25
	
	
root = tk.Tk()

label = tk.Label(root, text="Note: Does not calculate greenhouse gases",  fg="Red").grid(row=0, columnspan=2)

tk.Label(root, text="Distance").grid(row=1)
entrydistance = tk.Entry(root)
entrydistance.grid(row=1,column=1)

tk.Label(root, text="Distance Unit").grid(row=2)
entrydistance_unit = tk.Entry(root)
entrydistance_unit.grid(row=2,column=1)

tk.Label(root, text="Albedo").grid(row=3)
entryalbedo = tk.Entry(root)
entryalbedo.grid(row=3,column=1)

tk.Label(root, text="Stellar Luminosity").grid(row=4)
entrylum = tk.Entry(root)
entrylum.grid(row=4,column=1)

temp = tk.Label(root)
temp.grid(row=5,column=1)

def calculate():
	d = float(entrydistance.get())
	du = entrydistance_unit.get()
	l = float(entrylum.get())
	a = float(entryalbedo.get())
	
	temp.config(text=str(calculate_temp(d,du,l,a))+" Kelvin")
	
	
	
	
calc_button = tk.Button(root, text="Calculate", command=calculate).grid(row=5, column=0)

root.mainloop()

