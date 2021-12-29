/*
░░░░░░░█▀▀░█▀█░█▀▄░░░█░░░█▀█░█▀█░█▀█░░░░░░
░░░░░░░█▀▀░█░█░█▀▄░░░█░░░█░█░█░█░█▀▀░░░░░░
░░░░░░░▀░░░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░░░░░░░░
*/

// declare a variable
// pause
let x = 0.24;
const PI = 3.1416;
// pause

function put(text) {
// pause
  console.log(text);
  return true;
}
// pause

for (let i = 0; i < 10; ++i) {
// pause
  if (i % 2 === 0) {
    put('"i" is even');
// pause
  } else {
    put('"i" is odd');
  }
}
