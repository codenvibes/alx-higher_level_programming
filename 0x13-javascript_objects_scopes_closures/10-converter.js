#!/usr/bin/node
/*
    Auth: codenvibes
    Desc: JS script - a function that converts a number from base 10 to another base passed as argument.
*/
exports.converter = function (base) {
  return function (dec) {
    return dec.toString(base);
  };
};
