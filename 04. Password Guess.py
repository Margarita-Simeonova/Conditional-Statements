def password_guess(password):

    if password == "s3cr3t!P@ssw0rd":
        return "Welcome"
    else:
        return "Wrong password!"


text = input()
result = password_guess(text)
print(result)
