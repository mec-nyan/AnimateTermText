/*
░░░░░░░█▀▀░█▀█░█▀▄░░░█░░░█▀█░█▀█░█▀█░░░░░░
░░░░░░░█▀▀░█░█░█▀▄░░░█░░░█░█░█░█░█▀▀░░░░░░
░░░░░░░▀░░░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░░░░░░░░
*/

// declare a variable
let x = 0.24;
const PI = 3.1416;

function put(text) {
  console.log(text);
  return true;
}

for (let i = 0; i < 10; ++i) {
  if (i % 2 === 0) {
    put('"i" is even');
  } else {
    put('"i" is odd');
  }
}
