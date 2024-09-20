print("\n")
print("ACT 9 humano")
print("EMILIO GALE RENTERIA RAYO MTL: 22308051281093")

# CLASS ZONE
class humano1093:
    # ATRIBUTE ZONE
    FDN=0
    EDAD=0
    GENERO=0
    ESTATURA=0
    

    #FUNTION IN CLASS ZONE
    def correr1093(self,n):
        print(f"{n} esta corriendo")

    def saltar1093(self,n):
        print(f"{n} esta saltando")

    def comer1093(self,n):
        print(f"{n} esta comiendo")

    def nadar1093(self,n):
        print(f"{n} esta nadando")

# CREATION OBJECTS ZONE
emilio=humano1093()
juana=humano1093()

# USED OBJECT ZONE
print("\n Resultados para emilio \n")

# zona de llenado
emilio.FDN="25/07/2007"
emilio.EDAD=17
emilio.GENERO="masculino"
emilio.ESTATURA=1.71

# Emilio
emilio.correr1093("emilio")
emilio.saltar1093("emilio")
emilio.comer1093("emilio")
emilio.nadar1093("emilio")

print(f"Fecha de nacimiento: {emilio.FDN}")
print(f"Edad: {emilio.EDAD}")
print(f"Genero: {emilio.GENERO}")
print(f"Estatura: {emilio.ESTATURA}")



#------------------------------------------------------------------

print("\n Resultados para juana \n")
# zona de llenado
juana.FDN="27/011/2011"
juana.EDAD=13
juana.GENERO="femenino"
juana.ESTATURA=1.92

# juana
juana.correr1093("juana")
juana.saltar1093("juana")
juana.comer1093("juana")
juana.nadar1093("juana")
print(f"Fecha de nacimiento: {juana.FDN}")
print(f"Edad: {juana.EDAD}")
print(f"Genero: {juana.GENERO}")
print(f"Estatura: {juana.ESTATURA}")

