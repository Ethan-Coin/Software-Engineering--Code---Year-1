import 'dart:io';
import 'pract15.dart';

void main() {
  burgerOrder();
}

void burgerOrder() {
  print('Enter price of burgers');
  String? priceInput = stdin.readLineSync();
  double price = double.parse(priceInput!);
  print('How much money are you willing to spend on burgers?');
  String? balInput = stdin.readLineSync();
  double bal = double.parse(balInput!);
  int burgers = howManyBurgers(price, bal);
  displayBurgerOrder(burgers, price);
}
