# Testing: Si la variable es true se utilizaran los
# sistemas locales creados para pruebas
testing = True

if testing:
    URL = "http://localhost:8080"
else:
    URL = "http://sibila.website:8080"