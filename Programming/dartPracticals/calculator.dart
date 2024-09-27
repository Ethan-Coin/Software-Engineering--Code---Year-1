import 'dart:io';

void main(List<String> arguments) {
  String operation = arguments[0];
  int num1 = int.parse(arguments[1]);
  int num2 = int.parse(arguments[2]);

  if (operation == 'add') {
    print(num1 + num2);
  } else if (operation == 'sub') {
    print(num1 - num2);
  } else if (operation == 'mul') {
    print(num1 * num2);
  } else if (operation == 'div') {
    print(num1 / num2);
  } else {
    print('Invalid operation');
  }
}
