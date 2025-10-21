const formulario = document.getElementById('formulario')
const inputs = formulario.querySelectorAll('#formulario input')


const expresiones = {
     nombres:/^[a-zA-Z0-9]+$/,
     apellidos:/^[a-zA-Z0-9]+$/,
     cedula:/^[0-9]{10}$/,
     direccion:/^[a-zA-Z0-9\s]+$/,
     celular:/^[0-9]{10}$/,
     fecha_nacimiento:/^\d{4}-\d{2}-\d{2}$/,
     edad:/^\d+$/,
     estado_civil:/^(soltero|casado|divorciado)$/,
     tipo_sangre:/^[A|B|AB|O][+|-]$/,
     apellido_espos:/^[a-zA-Z0-9]+$/,
     canton:/^[a-zA-Z0-9\s]+$/,
     correo:/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
}

const validarFormulario = (e) => {
    switch(e.target.name){
       case "nombres":
           if(expresiones.nombres.test(e.target.value)){
               console.log('Nombre válido');
           }else{
               console.log('Nombre inválido');
           }
           break;
    }
    switch(e.target.name){
       case "apellidos":
           if(expresiones.apellidos.test(e.target.value)){
               console.log('Apellido válido');
           }else{
               console.log('Apellido inválido');
           }
           break;
    }
    switch(e.target.name){
       case "cedula":
           if(expresiones.cedula.test(e.target.value)){
               console.log('Cédula válida');
           }else{
               console.log('Cédula inválida');
           }
           break;
    }
    
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('keyup', validarFormulario);
});
formulario.addEventListener('submit', (e) => {
    e.preventDefault();
});