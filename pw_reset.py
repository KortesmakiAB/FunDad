from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

new_pw = "foxy"

hashed_pw = bcrypt.generate_password_hash(new_pw).decode('UTF-8')


# UPDATE users SET password = '$2b$12$pvK7jTH.hLQV1A8.fkyo7e5kl/EL2JOS6iAa3PYa67JWxYapkS4.q' WHERE id = 7;