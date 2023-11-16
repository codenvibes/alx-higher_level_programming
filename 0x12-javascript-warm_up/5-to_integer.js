#!/usr/bin/node
/*
    Auth: codenvibes
    Desc: JS script: Print 'My number: <first argument converted to integer>' if convertible to integer:
        - If the argument can’t be converted to an integer, print “Not a number”
        - You must use console.log(...) to print all output
        - You are not allowed to use var
        - You are not allowed to use try/catch
*/
const cmdArgs = process.argv;
if (!cmdArgs[2]) {
  console.log('Not a number');
} else {
  if (isNaN(cmdArgs[2])) {
    console.log('Not a number');
  } else {
    console.log('My number:', Math.floor(cmdArgs[2]));
  }
}
