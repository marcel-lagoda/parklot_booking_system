console.log('OK');

const button = document.querySelector('.form__button--js');
console.log(button);

const mouseOverFunction = function() {
  this.style.color = 'orange';
};

const mouseOutFunction = function() {
  this.style.color = '';
};

button.onmouseover = mouseOverFunction;
button.onmouseout = mouseOutFunction;

