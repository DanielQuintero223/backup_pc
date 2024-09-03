
// se crea un objeto persona

let persona = {
    nombre: 'Juan',
    apellido: 'Perez',
    edad: 25,
    direccion: {
        calle: 'Av. 123',
        ciudad: 'Lima'

    }
}


function nombreCompleato(persona){
    return persona.nombre + ' ' + persona.apellido
}

// se accede a los atributos del objeto persona
console.log(persona)
console.log(persona.apellido)
console.log(persona.direccion.ciudad)
console.log(nombreCompleato(persona))



// creacion de objeto con new Object
let persona2 = new Object()
persona2.nombre = 'Maria'
persona2.apellido = 'Gomez'
persona2.edad = 30
persona2.direccion = {
    calle: 'Av. 456',
    ciudad: 'Lima'
}

persona.telefono = 123456789
console.log(persona.telefono)

// recoorriendo los atributos de un objeto
for (nombrePropiedad in persona){
    console.log(nombrePropiedad)
    console.log(persona[nombrePropiedad])
}


// eliminando un atributo de un objeto
delete persona.telefono