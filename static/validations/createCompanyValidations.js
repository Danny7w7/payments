function sendDataCompany() {
    form = document.getElementById('formCompany')
    console.log(form)

    const formData = new FormData(form);  // Obtiene los datos del formulario

    fetch('/fetchCreateCompany/', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())  // Procesar la respuesta (si es JSON)
    .then(data => {
        if (data.success){
            Swal.fire({
                title: "Good job!",
                text: "Company successfully saved!",
                icon: "success",
                confirmButtonText: "Save",
            }).then((result) => {
                if (result.isConfirmed) {
                    location.reload();
                }
            });
        }else{
            console.log(data.errors);
            let messages = data.errors; // Obtenemos directamente el objeto de errores
                        
            let formattedMessage = "There seems to be some problems with the form:\n\n";

            for (const [field, errors] of Object.entries(messages)) {
                formattedMessage += `<li><strong>${capitalizeFirstLetter(field)}</strong>:`;
                errors.forEach(error => {
                    formattedMessage += `  ${error}</li>`;
                });
            }

            Swal.fire({
                icon: "error",
                title: "Oops...",
                html: formattedMessage,
            });
        }
    })
    // .catch(error => console.error('Error:', error));  // Manejo de errores
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}