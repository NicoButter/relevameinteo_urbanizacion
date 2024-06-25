document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.form');
    const fields = document.querySelectorAll('.field');
    const submitBtn = document.querySelector('.button');
  
    // Función para aplicar transformación 3D
    const apply3DTransform = (e) => {
      const rect = form.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const distanceX = x - centerX;
      const distanceY = y - centerY;
      const angleX = -distanceY * 0.05; // Invertir el ángulo Y para que siga el puntero
      const angleY = distanceX * 0.05;
  
      form.style.transform = `perspective(1500px) rotateX(${angleX}deg) rotateY(${angleY}deg)`;
    };
  
    // Evento para movimiento del ratón sobre el formulario
    form.addEventListener('mousemove', apply3DTransform);
  
    // Evento para foco en los campos de entrada
    fields.forEach((field) => {
      field.addEventListener('focus', () => {
        form.classList.add('form-animated');
        form.addEventListener('mousemove', apply3DTransform);
      });
  
      field.addEventListener('blur', () => {
        form.classList.remove('form-animated');
        form.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)';
      });
    });
  
    // // Evento para clic en el botón de submit
    // if (submitBtn) {
    //   submitBtn.addEventListener('click', (e) => {
    //     e.preventDefault(); // Prevenir el envío del formulario por defecto
    //     form.submit(); // Enviar el formulario manualmente
    //   });
    // }
});
