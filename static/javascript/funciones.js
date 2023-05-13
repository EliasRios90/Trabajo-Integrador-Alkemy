
const checkbox = document.querySelector('input[name="estado"]');
const label = document.querySelector('#estado_label'); //id del label

checkbox.addEventListener('change', function() {
  if (checkbox.checked) {
    label.textContent = 'Activo';
    checkbox.value = 'True';
  } else {
    label.textContent = 'Desactivado';
    checkbox.value = 'False';
  }
});
