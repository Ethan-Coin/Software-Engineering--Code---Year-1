import 'dart:io';
import 'dart:math';

void main() {
  int randomNumber = Random().nextInt(100) + 1;
  while (true) {
    print('Enter a number between 1 and 100:');
    String? input = stdin.readLineSync();
    int guess = int.parse(input!);
    if (guess == randomNumber) {
      print('You guessed correctly!');
      break;
    } else if (guess < randomNumber) {
      print('Too low');
    } else {
      print('Too high');
    }
  }
}
