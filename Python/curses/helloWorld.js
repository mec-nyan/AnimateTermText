/*
░░░░░░░█▀▀░█▀█░█▀▄░░░█░░░█▀█░█▀█░█▀█░░░░░░
░░░░░░░█▀▀░█░█░█▀▄░░░█░░░█░█░█░█░█▀▀░░░░░░
░░░░░░░▀░░░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░░░░░░░░
*/

// declare a variable
// pause
let x = 0.24;
// pause
const PI = 3.1416;
// pause

function put(text) {
// pause
  console.log(text);
// pause
  return true;
}
// pause

for (let i = 0; i < 10; ++i) {
// pause
  if (i % 2 === 0) {
// pause
    put('"i" is even');
// pause
  } else {
// pause
    put('"i" is odd');
  }
}
