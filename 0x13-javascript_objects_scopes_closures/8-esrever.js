#!/usr/bin/node
/*
    Auth: codenvibes
    Desc: JS script - a function that returns the reversed version of a list.
*/
exports.esrever = function (list) {
  let myVar = '';

  for (let i = 0; i < list.length / 2; i++) {
    myVar = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = myVar;
  }
  return list;
};
