import chalk from "chalk";
import * as readline from "node:readline";
import { stdin as input, stdout as output } from "process";

async function animate(text, start = 0) {
  if (start < text.length) {
    process.stdout.write(text[start]);
    setTimeout(() => animate(text, start + 1), 50);
  }
}

const rl = readline.createInterface({ input, output });

const message = "hello console\n";

console.clear();
animate(message).then(
  rl.question("wtf", (answer) => {
    animate(`Yes, ${answer}\n`);
  })
);

rl.close();
