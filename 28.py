
from tkinter import * 

root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="lightblue")

label_planet = Label(root, text="Planet : ", bg="lightblue")
label_planet_name = Label(root,font=("courier",18,"bold"), bg="lightblue")
label_planet_image = Label(root,bg="gold2", highlightthickness=5, borderwidth=2,relief=SOLID)
label_planet_gravity_radius = Label(root,font=("castellar"), bg="lightblue")
label_planet_info = Label(root,font=("courier",10,"bold"), bg="lightblue", wraplength=500)

planets = ["Mercury","Venus","Earth"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = planets, textvariable=selectedval)

def PlanetInfo():
    planet = selectedval.get()
    if planet == "Mercury":
        label_planet_name['text'] = "Mercury"
        label_planet_image['image'] = Mercury
        label_planet_gravity_radius['text'] = "Gravity : 3.7 m/s^2 \n Radius : 2438.7 km"
        label_planet_info['text'] = " Mercury is the smallest planet im our solar system. It is slightly larger than the moon."
    elif planet == "Venus":
        label_planet_name['text'] = "Venus"
        label_planet_image['image'] = Venus
        label_planet_gravity_radius['text'] = "Gravity : 8.87 m/s^2 \n Radius : 6051.8 km"
        label_planet_info['text'] = "Venus is the brightest object in the sky other than the sun and moon."
    elif planet == "Earth":
        label_planet_name['text'] = "Earth"
        label_planet_image['image'] = Earth
        label_planet_gravity_radius['text'] = "Gravity : 9.807 m/s^2 \n Radius : 6371 km"
        label_planet_info['text'] = "Earth is the only place in the known universe capable of sustaining life."
dropdown.place(relx=0.5, rely=0.1 , anchor=CENTER)

btn = Button(root, text="Show Planet Info" , command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

label_planet.place(relx=0.2, rely=0.1 , anchor=CENTER)    
label_planet_name(relx=0.5, rely=0.25 , anchor=CENTER) 
label_planet_image.place(relx=0.5, rely=0.5 , anchor=CENTER) 
label_planet_gravity_radius.place(relx=0.5, rely=0.8 , anchor=CENTER) 
label_planet_info.place(relx=0.5, rely=0.9 , anchor=CENTER) 
    

root.mainloop
    
btn = Button(root, text="Show Planet Info" , command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)


root.mainloop()

