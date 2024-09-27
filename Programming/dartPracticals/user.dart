import 'password.dart';

class User {
  String username;
  String _password = generatePassword(8);
}
