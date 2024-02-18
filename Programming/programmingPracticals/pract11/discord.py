class UnverifiedUser:

    def __init__(self, id):
        self.id = id
        self.messages = []

    def receiveMessage(self, message):
        self.messages.append(message)

    def viewMessages(self):
        output = f"Messages"
        for message in self.messages:
            output += f"\n{message}"
        return output + "\n"

    def __str__(self):
        output = f"User ID: {self.id}\n"
        count = 0
        for message in self.messages:
            count += 1
        output += f"Messages: {count}"
        return output


class VerifiedUser(UnverifiedUser):

    def sendMessage(self, message, recipient):
        if len(message) <= 100:
            recipient.receiveMessage(message)
        else:
            print("Message is too long.")


class NitroUser(VerifiedUser):
    def sendMessage(self, message, recipient):
        recipient.receiveMessage(message)

    def pinMessage(self, message):
        if message in self.messages:
            self.messages.remove(message)
            self.messages.insert(0, message)


def testMessages():
    unverifiedUser = UnverifiedUser("1")
    verifiedUser = VerifiedUser("2")
    nitroUser = NitroUser("3")

    verifiedUser.sendMessage("Hello", unverifiedUser)
    print(unverifiedUser.viewMessages())

    verifiedUser.sendMessage("Alga", nitroUser)
    verifiedUser.sendMessage("Hello", nitroUser)
    print(nitroUser.viewMessages())

    nitroUser.sendMessage("Hello" * 101, verifiedUser)
    print(verifiedUser.viewMessages())

    nitroUser.pinMessage("Hello")
    print(nitroUser.viewMessages())
    print(nitroUser)


testMessages()
