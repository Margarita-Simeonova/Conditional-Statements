def password_guess(password):
    # difine function
    if password == "s3cr3t!P@ssw0rd":
        return "Welcome"
    else:
        return "Wrong password!"


# input
text = input()
# result
result = password_guess(text)

print(result)
