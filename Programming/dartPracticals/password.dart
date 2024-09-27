import "dart:io";
import "dart:math";

void main(List<String> arguments) {
  int length;
  try {
    length = int.parse(arguments[0]);
  } catch (e) {
    length = 8;
  }
  String password = generatePassword(length);
  print(password);
}

String generatePassword(int length) {
  if (length < 8) {
    length = 8;
  }
  String password = "";
  for (int i = 0; i < length; i++) {
    int random = Random().nextInt(122) + 33;
    password += String.fromCharCode(random);
  }
  return password;
}
