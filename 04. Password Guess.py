def password_guess(password):

    if password == "s3cr3t!P@ssw0rd":
        return "Welcome"
    else:
        return "Wrong password!"


text = input()
print(password_guess(text))
