from tkinter import *


class MileAndKilometreConverter(Tk):
    
    def __init__(self, **kwargs):
        super().__init__()

        self.title(kwargs['title'])
        self.minsize(500,300)
        self.config(padx=100, pady=50, bg=kwargs['backgroundColor'])
        
        # miles
        self.mileInput = Entry(width=30)
        self.mile = Label(text="Miles", font=(kwargs["font"], 10, "bold"))

        self.mileInput.grid(row=0,column=0, padx=15, pady=10 )
        self.mile.grid(row=0,column=1, pady=10)
        
        # Kilometre
        self.kilometreInput = Entry(width=30)
        self.kilometre = Label(text="Kilometres", font=(kwargs["font"], 10, "bold"))

        self.kilometreInput.grid(row=1,column=0, padx=15, pady=10 )
        self.kilometre.grid(row=1,column=1, pady=10)
        
        # Button
        button = Button(
            text="Convert", command = self.convert, fg="white", bg="dark blue", padx=10, pady=5,font=(kwargs["font"], 10, "bold")
        )

        button.place(x=50,y=100)

        reset = Button(
            text="Reset", command = self.Reset, fg="white", bg="blue", padx=10, pady=5,font=(kwargs["font"], 10, "bold")
        )

        reset.place(x=155,y=100)



    def convert(self):
        """To convert the Kms to Miles or Miles to Kms"""
            
        # if no data in both boxes
        if (len(self.kilometreInput.get()) < 1 and len(self.mileInput.get()) < 1):
            print("No data found")

        else:
            
            # If both are already filled, this will create confusion, so resetting
            if(len(self.mileInput.get()) >= 1 and len(self.kilometreInput.get()) >= 1):
                print("Data mixmatch........Resetting")
                self.Reset()
        
            else:
                
                mls = self.mileInput.get()
                kms = self.kilometreInput.get()
            
                self.Reset() # So that we can fill both insert ourselves
                
                
                if(mls):
                    self.convertMilesToKm(mls)
                    
                if(kms):
                    self.convertKmToMiles(kms)
                    
                    
                    
        
    def convertKmToMiles(self,kms):
        
        conversion = round(float(kms) / 1.609, 2)
                    
        # Deleting if there is anything in input box
        self.mileInput.delete(0, 100)   # just in case if there are more digits
        
        # Inserting
        self.kilometreInput.insert(0, float(kms))
        self.mileInput.insert(0,conversion)

        print("converted Kilometres to Miles")



    def convertMilesToKm(self, mls):
        
        conversion = round(float(mls) * 1.609, 2)
                    
        # Deleting if there is anything in input box
        self.kilometreInput.delete(0, 100)   # just in case if there are more digits
        
        # Inserting
        self.mileInput.insert(0, float(mls))
        self.kilometreInput.insert(0,conversion)
        
        print("converted Miles to Kilometres")
        
        
        
        
    def Reset(self):
        """To reset the Inputs"""
        self.kilometreInput.delete(0,1000)
        self.mileInput.delete(0,1000)
        print("reset completed")
