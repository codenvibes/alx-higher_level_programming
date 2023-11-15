#!/usr/bin/node
/*
    Auth: codenvibes
    Desc: A JS script that prints the first argument passed to it:
        - If no arguments are passed to the script, print “No argument”
*/
const cmdArgs = process.argv;
if (cmdArgs[2]) {
    console.log(cmdArgs[2]);
} else {
    console.log('No argument');
}
